
import time

class AlertEscalator:
    def __init__(self, escalation_policy=None):
        if escalation_policy is None:
            self.escalation_policy = {
                1: {"delay": 10, "message": "Initial alert"},
                2: {"delay": 30, "message": "Escalated alert: Notify supervisor"},
                3: {"delay": 60, "message": "Escalated alert: Notify doctor"}
            }
        else:
            self.escalation_policy = escalation_policy
        self.alert_level = 0
        self.last_alert_time = None

    def escalate_alert(self, alerts):
        if not alerts:
            self.alert_level = 0
            self.last_alert_time = None
            return None

        current_time = time.time()

        if self.alert_level == 0:
            self.alert_level = 1
            self.last_alert_time = current_time
            return self.escalation_policy[1]["message"] + ": " + ", ".join(alerts)

        else:
            time_since_last_alert = current_time - self.last_alert_time
            next_level = self.alert_level + 1

            if next_level in self.escalation_policy and time_since_last_alert >= self.escalation_policy[self.alert_level]["delay"]:
                self.alert_level = next_level
                self.last_alert_time = current_time
                return self.escalation_policy[next_level]["message"] + ": " + ", ".join(alerts)

        return None


if __name__ == '__main__':
    alert_escalator = AlertEscalator()
    alerts1 = ["heart_rate is above the maximum threshold (110 > 100)"]
    escalation_message1 = alert_escalator.escalate_alert(alerts1)
    print(f"Escalation Message 1: {escalation_message1}")
    time.sleep(15)
    alerts2 = ["heart_rate is above the maximum threshold (115 > 100)", "spo2 is below the minimum threshold (90 < 95)"]
    escalation_message2 = alert_escalator.escalate_alert(alerts2)
    print(f"Escalation Message 2: {escalation_message2}")
    time.sleep(35)
    alerts3 = ["heart_rate is above the maximum threshold (120 > 100)", "spo2 is below the minimum threshold (85 < 95)"]
    escalation_message3 = alert_escalator.escalate_alert(alerts3)
    print(f"Escalation Message 3: {escalation_message3}")