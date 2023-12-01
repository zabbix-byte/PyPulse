import socketserver
from pypulse.Socket.handler import Request
from pypulse.Aplication import Vars


httpd = socketserver.TCPServer(
    ("", Vars.INTERNAL_HTTP_SERVER_PORT), Request)


def run_socket():
    httpd.serve_forever()

def stop_server():
    httpd.shutdown()
    httpd.server_close()