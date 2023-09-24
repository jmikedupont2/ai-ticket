import os
from dotenv import load_dotenv
from github import Github
from github import Auth

# Load environment variables from .env
load_dotenv()

git_hub_pat = os.getenv("GITHUB_PAT")
git_hub_repo = os.getenv("GITHUB_REPO")

print("PAT",git_hub_pat)

# using an access token
auth = Auth.Token(git_hub_pat)

g = Github(auth=auth)

# Then play with your Github objects:
#for repo in g.get_user().get_repos():
#    print(repo.name)
repo = g.get_repo(git_hub_repo)

def get_issues():
    issues = repo.get_issues()
    for issue in issues:
        yield issue

def get_existing_ticket(event):
    return None

def create_new_ticket(event):
    # repo = g.get_repo("PyGithub/PyGithub")
    body = event.get("content")
    title = "Auto issue"
    return repo.create_issue(title=title, body=body)
    #Issue(title="This is a new issue", number=XXX)
    
# To close connections after use
#g.close()
