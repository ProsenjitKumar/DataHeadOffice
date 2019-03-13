from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write("""
            <html><head></head>
            <body>
            <form method="POST">
            your mood:
            <textarea name="mood">
            </textarea>
            <input type="submit" name="submit" value="submit">
            </form>
            </body>
            </html>
            """)


    # def do_POST(self):
    #     form = cgi.FieldStorage(
    #         fp=self.rfile,
    #         headers=self.headers,
    #         environ={'REQUEST_METHOD':'POST',
    #                  'CONTENT_TYPE':self.headers['Content-Type'],
    #                  })
    #     themood = form["mood"]
    #     hap=['amused','beaming','blissful','blithe','cheerful','cheery','delighted']
    #     sad=['upset','out','sorry','not in mood','down']
    #     sad_count=0
    #     happy_count=0
    #     happy_count=len(filter(lambda x:x in themood.value,hap))
    #     sad_count=len(filter(lambda x:x in themood.value,sad))
    #     if(happy_count>sad_count):
    #         self.wfile.write("Hey buddy...your mood is HAPPY :-)")
    #     elif(sad_count>happy_count):
    #         self.wfile.write("Ouch! Your Mood is Sad :-(")
    #     elif(happy_count==sad_count):
    #         if(happy_count>0 and sad_count>0):
    #             self.wfile.write("oops! You are in CONFUSED mood :o")
    #         else:
    #             self.wfile.write("Sorry,No mood found :>")
    #     return


# server = HTTPServer(('localhost', 8080), Handler)
# print("before execute")
# server.serve_forever()
# print("After execute")


httpd = HTTPServer(('localhost', 8080), Handler)
print("before execute")
httpd.serve_forever()
print("After execute")


