import time


class ReqTimer:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        time_start = time.monotonic()
        response = self.get_response(request)
        response.headers["X-Request-Timing"] = str(time.monotonic() - time_start)[0:5]
        return response
