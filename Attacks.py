from time import sleep

class Attack:

    def __init__(self, category, name, mode, reqs) -> None:
        
        self.category = category
        self.name = name
        self.reqs = reqs
        self.mode = mode


    def run(self):

        if self.name == 'IDOR': # Insecure Direct Object/API Referenc
            for req in self.reqs:
                if 'Authorization' in req.request_headers:
                    req.request_headers.pop('Authorization')
                    req.send()
                    print(f'{req.url} : {req.status_code} -> {req.response_headers}')
                    sleep(2)

        elif self.name == 'AC': # ACCESS Control Check for
            pass
