from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread


def main():

    class FileTransferHandler(Thread):
        def __init__(self, cclient):
            super().__init__()
            self.cclient = cclient
        
        
        def run(self):
            my_dict = {}
            my_dict['filename'] = '一脸懵逼.jpg'
            my_dict['filedata'] = data
            json_str = dumps(my_dict)
            self.cclient.send(json_str.encode('utf-8'))
            self.cclient.close()

    server = socket()
    server.bind(('192.168.1.6', 5555))
    server.listen(520)
    print('服务器开始监听...')
    with open('一脸懵逼.jpg', 'rb') as f:
        data = b64encode(f.read()).decode('utf.8')
    while True:
        client, addr = server.accept()
        FileTransferHandler(client).start()


if __name__ == "__main__":
    main()
