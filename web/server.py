from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

from web.database import Base, GovermentMeasure
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create session and connect to DB ##
engine = create_engine('sqlite:///gov_measure.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class WebServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith("/index"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html>" \
                          "<body>"
                output += "<h1>" \
                          "Enter Textual Description of Government Measure" \
                          "</h1>"
                output += "<form method = 'POST' " \
                          "enctype='multipart/form-data' " \
                          "action = '/gov_measure/new'>"
                output += "<input name = 'gov_measure' " \
                          "type = 'text' " \
                          "placeholder = 'new_gov_measure_description'> "
                output += "<input type='submit' " \
                          "value='Create'>"
                output += "</form>" \
                          "</html>" \
                          "</body>"
                self.wfile.write(output.encode())

            if self.path.endswith("/measures"):
                measures = session.query(GovermentMeasure).all()
                output = ""
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output += "<html>" \
                          "<body>"
                for measure in measures:
                    output += measure.description
                    output += "</br></br></br>"
                    
                output += "</body></html>"
                self.wfile.write(output)
                return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    # Objective 3 Step 3- Make POST method
    def do_POST(self):
        try:
            if self.path.endswith("/gov_measure/new"):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('gov_measure')
                    print(messagecontent[0])

                    # Create new Restaurant Object
                    newRestaurant = GovermentMeasure(measure=messagecontent[0])
                    session.add(newRestaurant)
                    session.commit()

                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()
                    
        except:
            pass


def main():
    try:
        server = HTTPServer(('', 8080), WebServerHandler)
        print('Web server running...open localhost:8080/restaurants in your '
              'browser')
        server.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down server')
        server.socket.close()


if __name__ == '__main__':
    main()
