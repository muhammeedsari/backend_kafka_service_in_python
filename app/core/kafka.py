from app.core.messages import Messages
from app.core.error_success_data_result import ErrorDataResult
from confluent_kafka.admin import AdminClient, NewTopic
from confluent_kafka import Producer, Consumer

#! kafka logları da kayıt edilecek
class Kafka:

    def __init__(self):
        self.adminClient = AdminClient(
            {'bootstrap.servers': '165.232.152.207:9092'})

    def delivery_report(self, err, msg):
        message = Messages()
        try:
            if err is not None:
                print(message.failed_message_delivery.format(err))
            else:
                print(message.success_message_delivery.format(msg.topic(),
                                                            msg.partition(), msg.value().decode('utf-8')))
        except Exception as err:
            return ErrorDataResult(message=err.__doc__)
        
    def create_topics(self, topic: str, num_partitions: int):
        new_topics = [
            NewTopic(topic=topic, num_partitions=num_partitions, replication_factor=1)]
        fs = self.adminClient.create_topics(new_topics)
        for topic, f in fs.items():
            try:
                f.result()
                print("Topic {} created".format(topic))
            except Exception as e:
                print("Failed to create topic {}: {}".format(topic, e))

    def list_topics(self):
        print(self.adminClient.list_topics().topics)

    def produce_message(self, topic: str, key, value):
        producer = Producer({'bootstrap.servers': '165.232.152.207:9092'})
        producer.poll(0)
        try:
            producer.produce(topic=topic, key=key, value=value,
                            callback=self.delivery_report)
            producer.flush()
        except Exception as err:
            print("Error:  {}".format(err.__doc__))
            
    def create_consumer(self, topic: str, group_id: str):
        consumer = Consumer({
            'bootstrap.servers': '165.232.152.207:9092',
            'group.id': group_id,
            'auto.offset.reset': 'earliest'})

        consumer.subscribe([topic])
        return consumer
