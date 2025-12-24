
from kafka import KafkaProducer
import os
import json

class KafkaProducerWrapper:
    def __init__(self, topic_name):
        self.topic_name = topic_name
        self.kafka_bootstrap_servers = os.environ.get("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
        self.producer = KafkaProducer(
            bootstrap_servers=self.kafka_bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

    def send_message(self, message):
        try:
            self.producer.send(self.topic_name, value=message)
            self.producer.flush()
            print(f"Message sent to Kafka topic {self.topic_name}: {message}")
        except Exception as e:
            print(f"Error sending message to Kafka: {e}")


if __name__ == '__main__':
    kafka_topic = "vitals-alerts"
    producer_wrapper = KafkaProducerWrapper(kafka_topic)
    message = {"test": "This is a test message"}
    producer_wrapper.send_message(message)