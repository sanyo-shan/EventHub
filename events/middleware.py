import time, logging

from django.http import request

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response # One-time configuration and initialization.

    def __call__(self, request): # Code to be executed for each request before the view (and later middleware) are called.
        start_time = time.time()  # Record the start time
        response   = self.get_response(request) # Code to be executed for each request/response after the view is called.
        duration   = time.time() - start_time # Calculate the duration of the request
        logger.info(f"{request.method} {request.path} - {response.status_code} - {duration:.2f}s") # Log the request method, path, response status code, and duration
        print(f"{request.method} {request.path} - {response.status_code} - {duration:.2f}s") # Print the same information to the console
        return response # Return the response to be sent to the client