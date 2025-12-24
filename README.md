# Realtime Vitals Alert Engine v2

This project simulates real-time human vitals, detects anomalies, validates thresholds, and escalates alerts to a Kafka topic.

## Getting Started

### Prerequisites

-   Python 3.9+
-   Kafka
-   Docker (optional)

### Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/Gautam0610/realtime-vitals-alert-engine-v2.git
    cd realtime-vitals-alert-engine-v2
    ```

2.  Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Configuration

-   Set the Kafka bootstrap servers and topic name as environment variables:

    ```bash
    export KAFKA_BOOTSTRAP_SERVERS="localhost:9092"
    export KAFKA_TOPIC="vitals-alerts"
    ```

-   **Patient Aggregation Configuration:**

    -   `AGGREGATION_WINDOW`: The time window (in seconds) to aggregate alerts for a patient. Default is 60 seconds.
    -   `MAX_BREACHES`: The maximum number of threshold breaches allowed within the aggregation window before escalating the alert. Default is 3.

    ```bash
    export AGGREGATION_WINDOW=60
    export MAX_BREACHES=3
    ```

### Running the Application

-   Run the `main.py` script:

    ```bash
    python src/main.py
    ```

### Running with Docker

1.  Build the Docker image:

    ```bash
    docker build -t realtime-vitals-alert-engine .
    ```

2.  Run the Docker container, passing the environment variables:

    ```bash
    docker run -e KAFKA_BOOTSTRAP_SERVERS="localhost:9092" -e KAFKA_TOPIC="vitals-alerts" -e AGGREGATION_WINDOW=60 -e MAX_BREACHES=3 realtime-vitals-alert-engine
    ```

## Project Structure

```
realtime-vitals-alert-engine-v2/
├── src/
│   ├── vitals_generator.py
│   ├── anomaly_generator.py
│   ├── threshold_validator.py
│   ├── alert_escalator.py
│   ├── kafka_producer.py
│   ├── main.py
├── Dockerfile
├── README.md
└── requirements.txt
```

## Modules

-   `vitals_generator.py`: Generates realistic human vitals with unique patient IDs.
-   `anomaly_generator.py`: Injects anomalies into the generated vitals.
-   `threshold_validator.py`: Validates vitals against predefined thresholds.
-   `alert_escalator.py`: Escalates alerts based on a predefined policy.
-   `kafka_producer.py`: Sends messages to a Kafka topic.
-   `main.py`: Main application script that orchestrates the entire process and implements patient-level aggregation.

## Contributing

Feel free to contribute to this project by submitting pull requests.
