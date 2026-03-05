- download Kafka
```bash
wget https://archive.apache.org/dist/kafka/4.0.1/kafka_2.13-4.0.1.tgz
```

- untar the Kafka archive, and cd to the kafka directory:
```bash
tar -xzf kafka_2.13-4.0.1.tgz
```

- change directory
```bash
cd kafka_2.13-4.0.1
```
```bash
vim ~/kafka_2.13-4.0.1/config/server.properties
```

-add
```bash
metadata.log.dir=/home/{username}/kafka_2.13-4.0.1/kraft-combined-logs
controller.quorum.voters=1@localhost:9093
```

- while in the kafka directory you changed to above, run the following:
```bash
bin/kafka-storage.sh format -t $(bin/kafka-storage.sh random-uuid) -c config/server.properties
```

- do not forget to create the below directory for logs
```bash
mkdir -p /home/{username}/kafka_2.13-4.0.1/kraft-combined-logs
```

- start the server
```bash
bin/kafka-server-start.sh config/server.properties
```

-create your first topic
```bash
bin/kafka-topics.sh --create --topic quickstart-events --partitions 1 --replication-factor 1 --bootstrap-server localhost:9092
```

- list the topics
```bash
bin/kafka-topics.sh --list --bootstrap-server localhost:9092
```

- in another terminal create a consumer to consumer the messages
```bash
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic quickstart-events --from-beginning
```

- python example producer, after `pip install kafka-python`
```python

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
producer.send('test', b'hello worldssssss')
producer.flush()
```

- run a consumer in python:
```python
from kafka import KafkaConsumer
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("KafkaConsumer")

# Kafka Consumer setup
consumer = KafkaConsumer(
    'test',                        # topic name
    bootstrap_servers=['localhost:9092'],  # Kafka broker
    auto_offset_reset='earliest',  # read from beginning if no offsets yet
    group_id='file-consumer-group' # consumer group id
)

def consume():
    """
    Consume messages from Kafka and print them.
    If messages are chunks of a file, they can be written to disk.
    """
    logger.info("Starting Kafka consumer...")
    for message in consumer:
        # message.value is a bytes object
        data = message.value
        # For simple strings:
        try:
            text = data.decode('utf-8')
            logger.info(f"Received message: {text}")
        except UnicodeDecodeError:
            # For binary files:
            logger.info(f"Received {len(data)} bytes of binary data")
            # Example: append to a file
            with open("output_file.bin", "ab") as f:
                f.write(data)

if __name__ == "__main__":
    consume()
```