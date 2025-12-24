
class ThresholdValidator:
    def __init__(self, thresholds=None):
        if thresholds is None:
            self.thresholds = {
                "heart_rate": {"min": 50, "max": 100},
                "resp_rate": {"min": 12, "max": 20},
                "temperature": {"min": 36.0, "max": 38.0},
                "spo2": {"min": 95, "max": 100}
            }
        else:
            self.thresholds = thresholds

    def validate_vitals(self, vitals):
        alerts = []
        for vital, value in vitals.items():
            if vital not in self.thresholds:
                continue

            if value < self.thresholds[vital]["min"]:
                alerts.append(f"{vital} is below the minimum threshold ({value} < {self.thresholds[vital]['min']}) ")
            elif value > self.thresholds[vital]["max"]:
                alerts.append(f"{vital} is above the maximum threshold ({value} > {self.thresholds[vital]['max']}) ")

        return alerts


if __name__ == '__main__':
    threshold_validator = ThresholdValidator()
    vitals = {"heart_rate": 110, "resp_rate": 22, "temperature": 38.5, "spo2": 92}
    alerts = threshold_validator.validate_vitals(vitals)
    if alerts:
        print("Alerts:")
        for alert in alerts:
            print(f"- {alert}")
    else:
        print("No alerts.")