# from cgi import parse_qs
# from xsendfile import XSendfileApplication
#
# DOCUMENT_SENDING_APP = XSendfileApplication("/srv/my-app/uploads/documents")
#
# def application(environ, start_response):
#     is_user_authenticated = "REMOTE_USER" in environ
#     if is_user_authenticated:
#         response_body = download_document(environ, start_response)
#     else:
#         response_body = request_authentication(environ, start_response)
#
#     return response_body
#
# def download_document(environ, start_response):
#     new_environ = environ.copy()
#     new_environ['SCRIPT_NAME'] = environ.get("SCRIPT_NAME", "") + environ['PATH_INFO']
#
#     query_string = parse_qs(environ['QUERY_STRING'])
#     document_path = "/%s.pdf" % query_string.get("document_name")
#     new_environ['PATH_INFO'] = document_path
#
#     response = DOCUMENT_SENDING_APP(new_environ, start_response)
#     return response
#
# def request_authentication(environ, start_response):
#     start_response(
#         "401 WE DON'T KNOW WHO YOU ARE",
#         [("WWW-Authenticate", 'Basic realm="Document download"')]
#         )
#     return []

# def simple_app(environ, start_response):
#     status = '200 OK'
#     response_headers = [('Content-type','text/plain')]
#     start_response(status, response_headers)
#     return ['Hello world!\n']

from wsgiref.simple_server import make_server
from cgi import parse_qs, escape

html = """
<html>
<body>
   <form method="get" action="">
        <p>
           Age: <input type="text" name="age" value="%(age)s">
        </p>
        <p>
            Hobbies:
            <input
                name="hobbies" type="checkbox" value="software"
                %(checked-software)s
            > Software
            <input
                name="hobbies" type="checkbox" value="tunning"
                %(checked-tunning)s
            > Auto Tunning
        </p>
        <p>
            <input type="submit" value="Submit">
        </p>
    </form>
    <p>
        Age: %(age)s<br>
        Hobbies: %(hobbies)s
    </p>
</body>
</html>
"""

def application (environ, start_response):

    # Returns a dictionary in which the values are lists
    d = parse_qs(environ['QUERY_STRING'])

    # As there can be more than one value for a variable then
    # a list is provided as a default value.
    age = d.get('age', [''])[0] # Returns the first age value
    hobbies = d.get('hobbies', []) # Returns a list of hobbies

    # Always escape user input to avoid script injection
    age = escape(age)
    hobbies = [escape(hobby) for hobby in hobbies]

    response_body = html % { # Fill the above html template in
        'checked-software': ('', 'checked')['software' in hobbies],
        'checked-tunning': ('', 'checked')['tunning' in hobbies],
        'age': age or 'Empty',
        'hobbies': ', '.join(hobbies or ['No Hobbies?'])
    }

    status = '200 OK'

    # Now content type is text/html
    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ]

    start_response(status, response_headers)
    return [response_body]

httpd = make_server('localhost', 8080, application)

# Now it is serve_forever() in instead of handle_request()
httpd.serve_forever()