import falcon
# from main.settings import DB as db
from .helpers import generate_formdata
from .settings import CeleryConfig, url
from celery import Celery

# CLIENT_KEY = {"app": "f9cffda75d853c959f8d6fc58492cbe5",
#               "wap": "5k8se7r4jhrnfmsdhia8avlkfjsdfhjs"}


# def auth(req, resp, params):
#     """request,response and prarams object
#     process requests for auth and raise auth error if not autherised.
#     """
#     if 'wechat' in req.path:
#         pass
#     else:
#         client_key = req.get_header('client-key', None)
#         if client_key is None:
#             description = ('Please provide CLIENT_KEY')
#             raise falcon.HTTPUnauthorized('Authentication failure',
#                                           description,
#                                           href='http://docs.example.com/auth')
#         if not client_key in CLIENT_KEY.values():
#             description = ('The provided client key is invalid')
#             raise falcon.HTTPUnauthorized('Authentication failure',
#                                           description,
#                                           href='http://docs.example.com/auth')

# hooks to be executed on every request before reaching to the endpoint
app = falcon.API(before=[generate_formdata])

# Bootstraping celery application
celery_app = Celery('test_celery', broker=url)
celery_app.config_from_object(CeleryConfig)

# importing all the endpoints
from main.views import *
