import requests

class HTTPRequest:
    def __init__(self, method, url, headers, body=None):

        self.method = method
        self.url = url
        self.request_headers = headers
        self.request_body = body

        self.status_code = None
        self.response_headers = None
        self.response_body = None

    def send(self):

        resp = None
        if self.method == 'GET':
            resp = requests.get(url=self.url, headers=self.request_headers)
        elif self.method == 'POST':
            resp = requests.post(url=self.url, headers=self.request_headers)
        elif self.method == 'PUT':
            resp = requests.put(url=self.url, headers=self.request_headers)
        elif self.method == 'PATCH':
            resp = requests.patch(url=self.url, headers=self.request_headers)
        elif self.method == 'DELETE':
            resp = requests.delete(url=self.url, headers=self.request_headers)

        self.response_headers = resp.headers
        self.response_body = resp.content

