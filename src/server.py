import http.server
import json
import logging
import os

import renderer

logging.basicConfig(level=logging.INFO)

class RequestHandler(http.server.BaseHTTPRequestHandler):

    def do_POST(self):
        content_len = int(self.headers['Content-Length'])
        post_body = self.rfile.read(content_len)
        data = json.loads(post_body)
        logging.info('POST request, Path: {}\n'.format(self.path))

        image = None
        try:
            image = renderer.generate_map(data)
        except:
            pass

        if image:
            self.send_response(200)
            self.send_header('Content-type', 'image/png')
            self.end_headers()
            self.wfile.write(image)
        else:
            self.send_error(500)


if __name__ == '__main__':
    server_class = http.server.HTTPServer
    httpd = server_class(('', 8000), RequestHandler)
    logging.info('Server is ready')
    try:
        httpd.serve_forever()
    except:
        pass
