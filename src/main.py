
import time
import os
from src.vitals_generator import VitalsGenerator
from src.anomaly_generator import AnomalyGenerator
from src.threshold_validator import ThresholdValidator
from src.alert_escalator import AlertEscalator
from src.kafka_producer import KafkaProducerWrapper


def main():
    kafka_topic = os.environ.get("KAFKA_TOPIC", "vitals-alerts")
    vitals_generator = VitalsGenerator()
    anomaly_generator = AnomalyGenerator()
    threshold_validator = ThresholdValidator()
    alert_escalator = AlertEscalator()
    kafka_producer = KafkaProducerWrapper(kafka_topic)

    while True:
        vitals = vitals_generator.generate_vitals()
        vitals = anomaly_generator.inject_anomaly(vitals)
        alerts = threshold_validator.validate_vitals(vitals)
        escalation_message = alert_escalator.escalate_alert(alerts)

        if escalation_message:
            print(escalation_message)
            kafka_producer.send_message({"message": escalation_message, "vitals": vitals})
        else:
            kafka_producer.send_message({"vitals": vitals})

        time.sleep(1)

if __name__ == "__main__":
    main()