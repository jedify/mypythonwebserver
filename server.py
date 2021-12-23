from http.server import HTTPServer, BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/json')
		self.end_headers()
		self.wfile.write("{\"message\": \"Hello World\"}")
		
#Server Initialization
server = HTTPServer(('127.0.0.1',8080), RequestHandler)
server.serve_forever()
