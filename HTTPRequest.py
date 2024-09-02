import requests

class HTTPRequest:

    def __init__(self, method, url, headers, body=None, use_proxy=None) -> None:

        self.method = method
        self.url = url
        self.request_headers = headers
        self.request_body = body

        self.status_code = None
        self.response_headers = None
        self.response_body = None
        self.use_proxy = use_proxy
        
        self.proxies = {
            'http': 'http://localhost:8080',
            'https': 'http://localhost:8080',
        } if use_proxy else None

    def send(self) -> None:

        resp = None
        URL = 'https://' + self.request_headers['Host'] + self.url

        if self.method == 'GET':
            resp = requests.get(url=URL, headers=self.request_headers, proxies=self.proxies, verify=False)
        elif self.method == 'POST':
            resp = requests.post(url=URL, headers=self.request_headers, data=self.request_body, proxies=self.proxies, verify=False)
        elif self.method == 'PUT':
            resp = requests.put(url=URL, headers=self.request_headers, data=self.request_body, proxies=self.proxies, verify=False)
        elif self.method == 'PATCH':
            resp = requests.patch(url=URL, headers=self.request_headers, data=self.request_body, proxies=self.proxies, verify=False)
        elif self.method == 'DELETE':
            resp = requests.delete(url=URL, headers=self.request_headers, proxies=self.proxies, verify=False)

        self.status_code = resp.status_code
        self.response_headers = resp.headers
        self.response_body = resp.content

