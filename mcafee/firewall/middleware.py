from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")

class LoggingMiddleware(MiddlewareMixin):
    def process_request(self,request):
        logging.info("Request Method : "+str(request.META["REQUEST_METHOD"]))
        logging.info("URL Requested : "+str(request.path))
        logging.info("Request Body Contents : "+str(request.body))
        logging.info("Content Length : "+str(request.META["CONTENT_LENGTH"]))
        logging.info("Client IP Address : "+str(request.META["REMOTE_ADDR"]))
        logging.info("Host Name of Client : "+str(request.META["REMOTE_HOST"]))
        logging.info("Host Name of the Server : "+str(request.META["SERVER_NAME"]))
        logging.info("Port of the Server : "+str(request.META["SERVER_PORT"]))
        return None

    def process_response(self,request,response):
        logging.info("Response Content : "+str(response.content))
        logging.info("Response Code : "+str(response.status_code))
        return response