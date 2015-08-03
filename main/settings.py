from kombu import Exchange, Queue
from kombu.common import Broadcast

url = "amqp://%s:%s@%s//" % ('guest', 'guest', 'localhost')


class CeleryConfig:
    # CELERY_QUEUES = (
    #     Queue('q1', exchange=My_Exchange),
    #     Queue('q2', exchange=My_Exchange),
    # )
    CELERY_QUEUES = (Broadcast(name='broadcast_tasks', queue='broadcast_q', routing_key='tasks.insert_into_elastic'),
                     Queue('q1', Exchange=Exchange(name='datacapt1', type='fanout', routing_key='tasks.insert_into_elastic1'),
                        routing_key='tasks.insert_into_elastic1'))
    CELERY_ROUTES = {'tasks.insert_into_elastic': {'queue': 'broadcast_q'},
                     'tasks.insert_into_elastic1': {'queue': 'q1'}}
