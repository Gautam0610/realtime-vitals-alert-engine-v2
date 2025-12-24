# Real-time Vitals Alert Engine v2

This project simulates a real-time vital signs monitoring system. It generates synthetic vital signs data, introduces anomalies, validates data against thresholds, escalates alerts, and publishes data to a Kafka topic.

## Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Gautam0610/realtime-vitals-alert-engine-v2.git
    cd realtime-vitals-alert-engine-v2
    ```
2.  **Build the Docker image:**
    ```bash
    docker build -t vitals-alert .
    ```
3.  **Run the Docker container:**
    ```bash
    docker run -d vitals-alert
    ```

## Project Structure

*   `src/`:
    *   `vitals_generator.py`: Generates synthetic vital signs data.
    *   `anomaly_generator.py`: Introduces anomalies into the generated data.
    *   `threshold_validator.py`: Validates vital signs data against thresholds.
    *   `alert_escalator.py`: Handles alert escalation.
    *   `kafka_producer.py`: Publishes data to Kafka.
    *   `main.py`: Orchestrates the entire process.
*   `Dockerfile`: Defines the Docker image for the project.
*   `requirements.txt`: Lists the project dependencies (kafka-python).
