import os
from subprocess import call

repo_string = "https://" + os.getenv("GITHUB_USER") + ":" + os.getenv("GITHUB_PASS") + "@github.com/indexds/companies_tracker.git"
call(["git", "clone", repo_string])