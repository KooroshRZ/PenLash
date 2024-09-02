from time import sleep
import re

class Attack:

    def __init__(self, category, name, mode, reqs0, reqs1=None) -> None:
        
        self.category = category
        self.name = name
        self.reqs0 = reqs0
        self.reqs1 = reqs1
        self.mode = mode


    def run(self):

        if self.name == 'IDOR': # Insecure Direct Object/API Referenc
            for req in self.reqs0:
                if 'Authorization' in req.request_headers:
                    req.request_headers.pop('Authorization')
                    req.send()
                    print(f'{req.url} : {req.status_code} -> {req.response_headers}')
                    sleep(2)

        elif self.name == 'AC': # ACCESS Control Check for two different user (requires reqs0 and req1)
            
            reqs0 = []
            reqs1 = []

            for req0 in self.reqs0:
                url = ''
                if '?' in req0.url:
                    reqs0.append(req0.request_headers['Host'] + re.findall(r'^(.*)\?', req0.url)[0])
                else:
                    url = req0.url
                    reqs0.append(req0.request_headers['Host'] + url)

            for req1 in self.reqs1:
                url = ''
                if '?' in req1.url:
                    reqs1.append(req1.request_headers['Host'] + re.findall(r'^(.*)\?', req1.url)[0])
                else:
                    url = req1.url
                    reqs1.append(req1.request_headers['Host'] + url)

            reqs0 = set(reqs0)
            reqs1 = set(reqs1)

            token0 = 'Bearer '
            token1 = 'Bearer '
            token2 = 'Bearer '

            diff01 = reqs0.difference(reqs1)
            diff10 = reqs1.difference(reqs0)


            for req in self.reqs0:
                url = req.request_headers['Host']+req.url
                if url in diff01:
                    req.request_headers['Authorization'] = token0
                    req.send()

                    print(f"{req.status_code} : {req.method} https://{url}")

            # for req in self.reqs1:
            #     url = req.request_headers['Host']+req.url
            #     if url in diff10:
            #         req.request_headers['Authorization'] = token0
            #         req.send()

            #         print(f"{req.status_code} : {url}")