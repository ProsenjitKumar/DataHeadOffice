from http.server import HTTPServer, BaseHTTPRequestHandler

ulta_palta_list = ['Pagla', 'Janina', 'Bangladesh']
name = "someone"


class DataHeadServer(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index1.html'
        try:
            file_to_open = open(self.path[1:]).readlines()
            file_to_open = file_to_open.format(ulta_palta_list=ulta_palta_list, name=name)
            self.send_response(200)
        except:
            file_to_open = "File Not Found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))


httpd = HTTPServer(('localhost', 8080), DataHeadServer)
httpd.serve_forever()
print("Server Running")
