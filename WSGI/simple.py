from wsgiref.simple_server import make_server
from jinja2 import FileSystemLoader, Environment


class WebApp:

    def __init__(self, environment, response):
        self.environment = environment
        self.response = response

    def __iter__(self):
        status = '200 OK'
        response_headers = [('Content-type', 'text/html')]
        self.response(status, response_headers)

        yield b"<h1>Hello Python Wsgi web Application"


with make_server('', 8080, WebApp) as server:
    print("serving on port 8080 ... \n Visit http://127.0.0.1:8080 or localhost:8080"
          "\nTo kill the server ctrl+c from terminal")

    server.serve_forever()
