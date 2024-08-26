import xml.etree.ElementTree as ET
from base64 import b64decode
import re
from HTTPRequest import HTTPRequest

def parse_burp_file(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    requests = []
    for item in root:
        request_body = b64decode(item[8].text.encode())
        requests.append(request_body)

    return requests


def parse_requests(requests):

    index = 0
    req_objs = []
    for request in requests:

        request_splited = request.split(b'\r\n\r\n')

        head = request_splited[0].decode().split('\r\n')[1:]
        body = request_splited[1]

        headers = {}
        for h in head:
            tmp = h.split(':')
            headers[tmp[0]] = tmp[1][1:]


        r = re.findall(r'^([A-Z]+) (.*) HTTP/1.1', request_splited[0].decode().split('\r\n')[0])
        method = r[0][0]
        url = r[0][1]
        
        if method != 'OPTIONS':
            req_obj = HTTPRequest(method=method, url=url, headers=headers, body=body)
            req_objs.append(req_obj)
        
    return req_objs

requests_0 = parse_burp_file('./requests.0.xml')
requests_1 = parse_burp_file('./requests.1.xml')
requests_2 = parse_burp_file('./requests.2.xml')


reqs = parse_requests(requests_0)

for req in reqs:
    print(req.method)