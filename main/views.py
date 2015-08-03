import falcon
from .tasks import insert_into_elastic, insert_into_elastic1
from main import app


class CaptureData:
    def on_get(self, req, resp, form={}, files={}):
        insert_into_elastic.apply_async(args=[form], routing_key='tasks.insert_into_elastic')
        insert_into_elastic1.apply_async(args=[form], routing_key='tasks.insert_into_elastic1')
        resp.status = falcon.HTTP_200
        resp.content_type = "text/plain"
        resp.body = ''

    def on_post(self, req, resp, form={}, files={}):
        insert_into_elastic.apply_async(args=[form], routing_key='tasks.insert_into_elastic')
        insert_into_elastic1.apply_async(args=[form], routing_key='tasks.insert_into_elastic1')
        resp.status = falcon.HTTP_200
        resp.content_type = "text/plain"
        resp.body = ''


capturedata = CaptureData()
app.add_route('/api/v1/core/capturedata/', capturedata)
