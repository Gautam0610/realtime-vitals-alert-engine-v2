
import random
import time

class VitalsGenerator:
    def __init__(self, baseline_heart_rate=70, baseline_resp_rate=16, baseline_temperature=37.0, baseline_spo2=98):
        self.heart_rate = baseline_heart_rate
        self.resp_rate = baseline_resp_rate
        self.temperature = baseline_temperature
        self.spo2 = baseline_spo2

    def generate_vitals(self):
        # Simulate slight variations in vitals
        self.heart_rate += random.randint(-2, 2)
        self.resp_rate += random.randint(-1, 1)
        self.temperature += random.uniform(-0.1, 0.1)
        self.spo2 += random.randint(-1, 1)

        # Ensure vitals stay within realistic bounds
        self.heart_rate = max(30, min(self.heart_rate, 220))
        self.resp_rate = max(5, min(self.resp_rate, 40))
        self.temperature = max(35.0, min(self.temperature, 42.0))
        self.spo2 = max(70, min(self.spo2, 100))

        return {
            "heart_rate": round(self.heart_rate, 2),
            "resp_rate": round(self.resp_rate, 2),
            "temperature": round(self.temperature, 2),
            "spo2": round(self.spo2, 2)
        }

if __name__ == '__main__':
    vitals_generator = VitalsGenerator()
    for _ in range(5):
        vitals = vitals_generator.generate_vitals()
        print(vitals)
        time.sleep(1)
