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

- python example producer
```python

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
producer.send('test', b'hello worldssssss')
producer.flush()
```

```

```