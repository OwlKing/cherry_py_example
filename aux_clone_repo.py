import os
from subprocess import call

repo_string = "https://" + os.environ["GITHUB_USER"] + ":" + os.environ["GITHUB_PASS"] + "@github.com/indexds/companies_tracker.git"
call(["git", "clone", repo_string])