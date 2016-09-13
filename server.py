import cherrypy
import os


class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        hello = os.getenv("GITHUB_USER")
        return hello


if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 443})
    cherrypy.quickstart(HelloWorld())
