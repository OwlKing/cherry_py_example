import os
from git import Repo

repo_string = "https://github.com/OwlKing/cherry_py_example.git"

Repo.clone_from(repo_string, "server")
