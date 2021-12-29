from app.core.kafka import Kafka
from app.core.error_success_result import ErrorResult


class AdminController:

    def create_topic(self, topic='credit_card3', num_partitions=2):
        try:
            kafka = Kafka()
            kafka.create_topics(topic=topic, num_partitions=num_partitions)
        except Exception as err:
            return ErrorResult(message=err.__doc__)
