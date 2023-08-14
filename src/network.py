import socket, json


class Network:

    def __init__(self, host, port):
        self.host = host
        self.port = port 
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.s.connect((self.host, self.port))
        data = self.s.recv(1024).decode('ascii')
        with open('config.json', 'w') as f:
            f.write(data)

    def send_data(self, keys):
        f = open('config.json', 'r')
        conf = json.loads(f.read())
        f.close()
        self.s.sendall(json.dumps({"keys": [f'snake_{conf["id"]}_{keys[0]}'], "dead": False}).encode('ascii'))


    def get_data(self):
        data = self.s.recv(4096).decode('ascii').replace("'", '"')
        data = json.loads(data)
        return data
