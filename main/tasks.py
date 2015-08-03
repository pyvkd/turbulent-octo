from . import celery_app


@celery_app.task()
def insert_into_elastic(data):
    print data


@celery_app.task()
def insert_into_elastic1(data):
    print data
