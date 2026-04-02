import socket
import threading
import json

class P2PNode:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.peers = []
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def start(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        print(f"🌐 P2P节点启动: {self.host}:{self.port}")
        threading.Thread(target=self.accept_peers).start()

    def accept_peers(self):
        while True:
            conn, addr = self.socket.accept()
            self.peers.append(conn)
            print(f"✅ 新节点连接: {addr}")
            threading.Thread(target=self.handle_peer, args=(conn,)).start()

    def handle_peer(self, conn):
        while True:
            try:
                data = conn.recv(1024).decode()
                if data:
                    msg = json.loads(data)
                    print(f"📩 接收消息: {msg}")
            except:
                break

    def broadcast(self, message):
        for peer in self.peers:
            peer.send(json.dumps(message).encode())

if __name__ == "__main__":
    node = P2PNode("localhost", 8888)
    node.start()
