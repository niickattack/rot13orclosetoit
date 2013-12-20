import webapp2

form = """
<form method = "post">
<head>
    <title>Unit 2 Rot 13</title>
</head>
 <body>
 	<h2>Enter some text to ROT13:</h2>
    <input type = 'textarea' name='text' value='%(text)s' style="height: 100px; width: 400px;">
    <br>
      <input type="submit">
   </body>
</form>
"""
import cgi
def escape_html(s):
	return cgi.escape(s, quote = True)

def rot13(text):
	text = text.encode('rot13')
	return text

class MainHandler(webapp2.RequestHandler):

	def write_form(self, text=""):
		self.response.out.write(form % {"text": escape_html(text)})

	def get(self):
		self.write_form()

	def post(self):
		text = self.request.get('text')
		self.write_form(rot13(text))

class DataHandler(webapp2.RequestHandler):
	def get(self):
		response.out.write(text)

app = webapp2.WSGIApplication([
    ('/', MainHandler), ('/data', DataHandler)
], debug=True)


#Things I didn't use.

#import jinja2
#import os

#jinja_environment = jinja2.Environment(
#    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
#    extensions=['jinja2.ext.autoescape'])
