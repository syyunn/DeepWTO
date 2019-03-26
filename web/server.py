from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

from web.database import Base, GovermentMeasure
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from utils.misc.json import write_json_one_line

# Create session and connect to DB ##
engine = create_engine('sqlite:///gov_measure.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class WebServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith("/gov_measure/submit"):
                self.send_response(200)
                self.send_header('Content-type',
                                 'text/html')
                self.end_headers()
                
                output = ""
                output += "<html>" \
                          "<body>"
                output += "<h1>" \
                          "Government Measure" \
                          "</h1>"
                output += "<form method = 'POST' " \
                          "enctype='multipart/form-data' " \
                          "action = '/gov_measure/submit'>"
                output += "<input name = 'gov_measure' " \
                          "type = 'text' " \
                          "placeholder = 'new_gov_measure_description'> "
                output += "<input type='submit' " \
                          "value='submit'>"
                output += "</form>" \
                          "</html>" \
                          "</body>"
                self.wfile.write(output.encode())
                return
                
            if self.path.endswith("/measures"):
                measures = session.query(GovermentMeasure).all()
                output = ""
                
                self.send_response(200)
                self.send_header('Content-type',
                                 'text/html')
                self.end_headers()
                output += "<html>" \
                          "<body>"
                for measure in measures:
                    output += measure.description
                    output += "</br></br></br>"
                    
                output += "</body></html>"
                self.wfile.write(output.encode())
                return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
       
        if self.path.endswith("/gov_measure/submit"):
            print("here!")
            print(self.headers)
            ctype, pdict = cgi.parse_header(
                self.headers['content-type'])
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            print(pdict.keys())
            pdict['CONTENT-LENGTH'] = self.headers['content-length']
            print(ctype, pdict)
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('gov_measure')
                measure = messagecontent[0]
                print(measure)
                
                ###############################################################
                # Prepare Test Input Json
                from models.citability.data.prep import do_tokenize
                data_to_feed = do_tokenize(measure)
                print(data_to_feed)
                
                json_write_path = "test_data.json"
                write_json_one_line(json_write_path, data_to_feed)
                ###############################################################
                # Test!
                import os
                from data.label.citability.parse import rehash_arts_in_text
                from utils.misc.json import read_json
                from web.tf_serve_pack import test_ann
                word2vec_path = "/Users/zachary/Downloads/" \
                                "GoogleNews-vectors-negative300.bin"
                model_number = 1553177254
                test_ann(word2vec_path,
                         model_number)
                prediction_json_path = os.path.join('results',
                                                    str(model_number),
                                                    'predictions.json')
                prediction = read_json(prediction_json_path)
                keys = ["predict_labels", "predict_scores"]
                prediction_arts = rehash_arts_in_text(
                    prediction[keys[0]],
                    yaml_path='../data/label/citability/labels/GATT.yaml')
                print(prediction_arts)
                ###############################################################
                
                # Create new Restaurant Object
                newRestaurant = GovermentMeasure(
                    description=measure)
                session.add(newRestaurant)
                session.commit()

                self.send_response(301)
                self.send_header('Content-type',
                                 'text/html')
                self.send_header('Location',
                                 '/measures')  # Page Change to /measures
                self.end_headers()
            return

            
def main():
    try:
        server = HTTPServer(('', 8080), WebServerHandler)
        print('Web server running...open localhost:8080/'
              'restaurants in your browser')
        server.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down server')
        server.socket.close()


if __name__ == '__main__':
    main()
