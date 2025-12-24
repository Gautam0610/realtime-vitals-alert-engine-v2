
import time
import os
from src.vitals_generator import VitalsGenerator
from src.anomaly_generator import AnomalyGenerator
from src.threshold_validator import ThresholdValidator
from src.alert_escalator import AlertEscalator
from src.kafka_producer import KafkaProducerWrapper


def main():
    kafka_topic = os.environ.get("KAFKA_TOPIC", "vitals-alerts")
    aggregation_window = int(os.environ.get("AGGREGATION_WINDOW", 60))  # Time window in seconds
    max_breaches = int(os.environ.get("MAX_BREACHES", 3))  # Max breaches within the window
    vitals_generator = VitalsGenerator()
    anomaly_generator = AnomalyGenerator()
    threshold_validator = ThresholdValidator()
    alert_escalator = AlertEscalator()
    kafka_producer = KafkaProducerWrapper(kafka_topic)

    patient_alerts = {}

    while True:
        vitals = vitals_generator.generate_vitals()
        patient_id = vitals["patient_id"]
        vitals = anomaly_generator.inject_anomaly(vitals)
        alerts = threshold_validator.validate_vitals(vitals)
        escalation_message = alert_escalator.escalate_alert(alerts)

        if patient_id not in patient_alerts:
            patient_alerts[patient_id] = []

        if alerts:
            patient_alerts[patient_id].append({"timestamp": time.time(), "alerts": alerts})

            # Remove old alerts outside the aggregation window
            patient_alerts[patient_id] = [
                alert for alert in patient_alerts[patient_id]
                if time.time() - alert["timestamp"] <= aggregation_window
            ]

            # Check if the number of breaches exceeds the maximum within the window
            if len(patient_alerts[patient_id]) >= max_breaches:
                #Escalate the alert
                escalation_message = f"Patient {patient_id} has breached critical thresholds multiple times. " + escalation_message if escalation_message else f"Patient {patient_id} has breached critical thresholds multiple times."
                print(escalation_message)
                kafka_producer.send_message({"message": escalation_message, "vitals": vitals})

        if escalation_message and patient_id not in escalation_message:
            print(escalation_message)
            kafka_producer.send_message({"message": escalation_message, "vitals": vitals})
        else:
            kafka_producer.send_message({"vitals": vitals})

        time.sleep(1)

if __name__ == "__main__":
    main()