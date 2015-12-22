import sys
from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse
import os
from mimetypes import types_map
import ast
import urllib
import config
import json
import threading
import time

class CipyHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        try:
            if self.path == '/':
                self.path = '/index.html'
            if self.path.startswith('/getdata'):
                self.send_response(200)
                self.end_headers()
                global current_jenkins_data
                self.wfile.write(current_jenkins_data)
                return
            fname,ext = os.path.splitext(self.path)
            filename = self.path[1:]
            cwd = os.getcwd()
            fullFileName = os.path.join(cwd, filename)
            with open(fullFileName,'rb') as f:
                self.send_response(200)
                self.send_header('Content-type', types_map[ext])
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
            return
        except IOError:
            self.send_error(404)
    

class DataProvider():
    
    def getData(self):
        outputJobs = []
        for configJob in config.jobs:
            jenkinsJob = self.fetchJob(configJob['url'] + '/api/python?tree=name,builds[number,result,building,url,estimatedDuration,timestamp,actions[parameters[name,value]],subBuilds[buildNumber,result,building,jobName,url]]')
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
                    for configSubBuild in configJob['subBuilds']:
                        convertedSubBuild = {}
                        convertedSubBuild['name'] = configSubBuild['cipyPrettyName']
                        convertedSubBuild['number'] = ''
                        convertedSubBuild['result'] = 'GRAY'
                        convertedSubBuild['url'] = ''
                        for jenkinsSubBuild in jenkinsBuild['subBuilds']:
                            if jenkinsSubBuild['jobName'] == configSubBuild['jobName']:
                                convertedSubBuild['number'] = jenkinsSubBuild['buildNumber']
                                convertedSubBuild['result'] = self.converStatus(jenkinsSubBuild['result'])
                                convertedSubBuild['url'] = config.jenkins_url + jenkinsSubBuild['url']
                                break
                        convertedJob['subBuilds'].append(convertedSubBuild)
                self.addInprogressInformationToBuild(configJob, jenkinsJob, convertedJob)
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
        
    def addInprogressInformationToBuild(self, configJob, jenkinsJob, convertedJob):
        progress = -1
        for jenkinsBuild in jenkinsJob['builds']:
            if 'parameters' in configJob and not self.actionParametersMatch(jenkinsBuild['actions'], configJob['parameters']):
                continue
            if jenkinsBuild['building'] == False:
                continue
            newProgress = self.calculateProgress(jenkinsBuild['timestamp'], jenkinsBuild['estimatedDuration'])
            if newProgress > progress:
                progress = newProgress
        if progress > -1:
            convertedJob['progress'] = str(progress) + '%'
    
    def calculateProgress(self, timestamp, estimatedDuration):
        return round((time.time()*1000 - timestamp) * 100 / estimatedDuration, 2)

current_jenkins_data = ''
   
def jenkins_updater():
    print 'Update data from jenkins'
    global current_jenkins_data 
    current_jenkins_data = json.dumps(DataProvider().getData())
    t = threading.Timer(15.0, jenkins_updater)
    t.start()
    return    

    
if __name__ == '__main__':
    print ('starting cipy server')
    print (sys.version)

    jenkins_updater()

    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('', 8000), CipyHandler)
    server.serve_forever()