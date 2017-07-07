#!/usr/bin/python
import SimpleHTTPServer
import SocketServer
import commands
import Flight_No
import Flight_Price
class SETHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
        def createHTML(self):
            html = file("index.html", "r")
            for line in html:
                self.wfile.write(line)
            #self.send_response(200)

        def do_GET(self):
            print "GET"
            print self.headers
            #print self.headers.dict
            # info2 are the date

            commands.getoutput("python circle.py "+self.headers['info1']+" "+self.headers['info2']+" "+self.headers['info3'])
            self.createHTML()

Handler=SETHandler
PORT=8080
httpd=SocketServer.TCPServer(("",PORT),Handler)
print PORT
httpd.serve_forever()

