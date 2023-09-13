import socketserver
from .request_handler import RequestHandler
from pypulse.Aplication import Vars


httpd = socketserver.TCPServer(
    ("", Vars.INTERNAL_HTTP_SERVER_PORT), RequestHandler)


def run_socket():
    httpd.serve_forever()

def stop_server():
    httpd.shutdown()
    httpd.server_close()