import os
import re
import json
from dotenv import load_dotenv
from github import Github
from github import Auth
from ai_ticket import find_name

# FIXME move this to a context object
# Load environment variables from .env
load_dotenv()
git_hub_pat = os.getenv("GITHUB_PAT")
git_hub_repo = os.getenv("GITHUB_REPO")
auth = Auth.Token(git_hub_pat)
g = Github(auth=auth)
repo = g.get_repo(git_hub_repo)


def get_issues():
    issues = repo.get_issues()
    for issue in issues:
        yield issue

def get_existing_ticket(event):
    """Find the first ticket that matches"""
    body = event.get("content")
    #print("DEBUG get ",event)
    for issue in get_issues():
        data = issue.body
        #print("DEBUG check ",data)
        name = find_name(data)
        if name:
            return issue

    return None

def create_new_ticket(event):

    # repo = g.get_repo("PyGithub/PyGithub")
    body = event.get("content")
    title = "Auto issue"
    try:
        body = "```" + json.dumps(json.loads(body),indent=2)  + "```"
    except Exception as e:
        print(e)
    return repo.create_issue(title=title, body=body)
    #Issue(title="This is a new issue", number=XXX)
    
def create_new_comment(ticket, event):
    body = event.get("content")
    print("DEBUG",body)
    #try:
    body = "```" + json.dumps(json.loads(body),indent=2)  + "```"
    #except Exception as e:
    #print(e)
    ticket_object = ticket#repo.get_issue(int(ticket.split("/")[-1]))
    comment =  ticket_object.create_comment(body)
    print(comment)

    #Issue(title="This is a new issue", number=XXX)
    
# To close connections after use
#g.close()
