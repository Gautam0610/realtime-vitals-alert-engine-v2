
import random

class AnomalyGenerator:
    def __init__(self, anomaly_probability=0.05):
        self.anomaly_probability = anomaly_probability

    def inject_anomaly(self, vitals):
        if random.random() < self.anomaly_probability:
            # Choose a vital to modify
            vital_to_modify = random.choice(list(vitals.keys()))

            # Generate a random anomaly value
            if vital_to_modify == "heart_rate":
                anomaly_value = vitals[vital_to_modify] + random.randint(-30, 30)
                anomaly_value = max(30, min(anomaly_value, 220))
            elif vital_to_modify == "resp_rate":
                anomaly_value = vitals[vital_to_modify] + random.randint(-10, 10)
                anomaly_value = max(5, min(anomaly_value, 40))
            elif vital_to_modify == "temperature":
                anomaly_value = vitals[vital_to_modify] + random.uniform(-2, 2)
                anomaly_value = max(35.0, min(anomaly_value, 42.0))
            elif vital_to_modify == "spo2":
                anomaly_value = vitals[vital_to_modify] + random.randint(-20, 0)
                anomaly_value = max(70, min(anomaly_value, 100))
            else:
                return vitals  # No valid vital to modify

            vitals[vital_to_modify] = round(anomaly_value, 2)
            print(f"Anomaly injected in {vital_to_modify}: {vitals[vital_to_modify]}")
        return vitals

if __name__ == '__main__':
    anomaly_generator = AnomalyGenerator()
    vitals = {"heart_rate": 75, "resp_rate": 15, "temperature": 37.0, "spo2": 99}
    anomalous_vitals = anomaly_generator.inject_anomaly(vitals)
    print(f"Original Vitals: {{\"heart_rate\": 75, \"resp_rate\": 15, \"temperature\": 37.0, \"spo2\": 99}}")
    print(f"Anomalous Vitals: {anomalous_vitals}")