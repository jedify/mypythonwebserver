import socketserver
import http.server
import re

PORT = 8081

class CustomHandler(http.server.SimpleHTTPRequestHandler):
	def do_POST(self):
		content_len = int(self.headers.get('content-length', 0))
		post_body = self.rfile.read(content_len)
		print(post_body)
		self.send_response(200)
		self.send_header('Content-type','application/text')
		self.end_headers()
		self.wfile.write(post_body) 

	def do_GET(self):
		if None != re.search('/api/message', self.path):
			self.send_response(200)
			self.send_header('Content-type','application/json')
			self.end_headers()
			self.wfile.write("{\"message\": \"Hello World\"}".encode()) 
			return
		if None != re.search('/api/sum/*', self.path):
			num1 = float(self.path.split('/')[-1])
			num2 = float(self.path.split('/')[-2])
			self.send_response(200)
			self.send_header('Content-type','application/json')
			self.end_headers()
			self.wfile.write("{\"data\": " + str(num1+num2) + "}") 
			return
		else:
			http.server.SimpleHTTPRequestHandler.do_GET(self)

httpd = socketserver.ThreadingTCPServer(('', PORT),CustomHandler)

print("serving at port", PORT)
httpd.serve_forever()
