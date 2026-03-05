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

```bash
mkdir -p /home/{username}/kafka_2.13-4.0.1/kraft-combined-logs
```