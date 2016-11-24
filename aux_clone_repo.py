import os
from git import Repo

repo_string = "git@github.com:indexds/alexa_cherrypy.git"

Repo.clone_from(repo_string, "cherrypy_server")
