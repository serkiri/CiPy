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
            jenkinsJob = self.fetchJob(configJob['url'] + '/api/python?tree=name,builds[number,result,building,url,actions[parameters[name,value]],subBuilds[buildNumber,result,building,jobName,url]]')
            convertedJob = {}
            convertedJob['name'] = configJob['cipyPrettyName']
            for jenkinsBuild in jenkinsJob['builds']:
                if 'parameters' in configJob and not self.actionParametersMatch(jenkinsBuild['actions'], configJob['parameters']):
                    continue
                if jenkinsBuild['building'] == True:
                    continue
                convertedJob['number'] = jenkinsBuild['number']
                convertedJob['result'] = self.converStatus(jenkinsBuild['result'])
                convertedJob['url'] = jenkinsBuild['url']
                if 'subBuilds' in configJob:
                    convertedJob['subBuilds'] = []
                    for jenkinsSubBuild in jenkinsBuild['subBuilds']:
                        if jenkinsSubBuild['jobName'] in configJob['subBuilds']:
                            convertedSubBuild = {}
                            convertedSubBuild['name'] = jenkinsSubBuild['jobName']
                            convertedSubBuild['number'] = jenkinsSubBuild['buildNumber']
                            convertedSubBuild['result'] = self.converStatus(jenkinsSubBuild['result'])
                            convertedSubBuild['url'] = config.jenkins_url + jenkinsSubBuild['url']
                            convertedJob['subBuilds'].append(convertedSubBuild)
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
    server = HTTPServer(('', 8000), CipyHandler)
    server.serve_forever()