import cherrypy
import os
from subprocess import call

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        hello = os.getenv("GITHUB_USER")
        return hello

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 80})
    cherrypy.quickstart(HelloWorld())


# docker -H localhost:2374 service create --replicas 2 --name cherrypy --publish 443:443 arturosaco/cherrypy_example python server.py