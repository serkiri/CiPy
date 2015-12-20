import sys
from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse
import os
from mimetypes import types_map
import ast
import urllib
import config
import json

class CipyHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        try:
            if self.path == '/':
                self.path = '/index.html'
            if self.path.startswith('/getdata'):
                self.send_response(200)
                self.end_headers()
                self.wfile.write(json.dumps(DataProvider().getData()))
                return
            fname,ext = os.path.splitext(self.path)
            filename = self.path[1:]
            cwd = os.getcwd()
            fullFileName = os.path.join(cwd, filename)
            with open(fullFileName) as f:
                self.send_response(200)
                self.send_header('Content-type', types_map[ext])
                self.end_headers()
                self.wfile.write(f.read())
            return
        except IOError:
            self.send_error(404)
    

class DataProvider():
    
    def getData(self):
        outputJobs = []
        for configJob in config.jobs:
            jenkinsJob = self.fetchJob(configJob['url'] + '/api/python?tree=name,builds[number,actions[parameters[name,value]],result]')
            convertedJob = {}
            convertedJob['name'] = configJob['cipyPrettyName']
            for jenkinsBuild in jenkinsJob['builds']:
                if 'parameters' in configJob and not self.actionParametersMatch(jenkinsBuild['actions'], configJob['parameters']):
                    continue
                if not 'result' in jenkinsBuild or jenkinsBuild['result'] == None:
                    continue
                convertedJob['number'] = jenkinsBuild['number']
                convertedJob['result'] = self.converStatus(jenkinsBuild['result'])
                break
            outputJobs.append(convertedJob)
        return outputJobs

    def fetchJob(self, joburl):
            responceFile = urllib.urlopen(joburl)
#            responceFile = open('d:\cipy\examples\jenk.py', 'r')
            responceRaw = responceFile.read()
            responce = ast.literal_eval(responceRaw)
            return responce
    
    def converStatus(self, jenkinsStatus):
        if jenkinsStatus == 'SUCCESS':
            return 'GREEN'
        else:
            return 'RED'
    
    def actionParametersMatch(self, jenkinsActions, configParameters):
        for action in jenkinsActions:
            if 'parameters' in action and configParameters in action['parameters']:
                return True
        return False

   
    
 
if __name__ == '__main__':
    print ('starting cipy server')
    print (sys.version)
    

    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost', 8000), CipyHandler)
    server.serve_forever()