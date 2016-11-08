import os
from git import Repo

# repo_string = "https://" + os.getenv("GITHUB_USER") + ":" + os.getenv("GITHUB_PASS") + "@github.com/indexds/companies_tracker.git"
repo_string = "https://github.com/" + os.getenv("GITHUB_USER") +"/cherry_py_example.git"
Repo.clone_from(repo_string, "cherry_py_example")
