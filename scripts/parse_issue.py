import os
import sys
import argparse
import requests

def get_issue(github_token, repo, issue_number):
    api_url = f"https://api.github.com/repos/{repo}/issues/{issue_number}"
    headers = {"Authorization": f"token {github_token}"}
    resp = requests.get(api_url, headers=headers)
    resp.raise_for_status()
    return resp.json()

def extract_fields(issue_body):
    # Very basic parsing for demonstration; use regex or yaml for robustness
    data = {}
    for line in issue_body.splitlines():
        if "Repository URL" in line:
            data["repo_url"] = line.split(":", 1)[-1].strip()
        if "Root Path Name" in line:
            data["root_path"] = line.split(":", 1)[-1].strip()
    return data

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--issue_number", required=True)
    parser.add_argument("--github_token", required=True)
    parser.add_argument("--repo", default=os.environ.get("GITHUB_REPOSITORY"))
    args = parser.parse_args()

    issue = get_issue(args.github_token, args.repo, args.issue_number)
    fields = extract_fields(issue["body"])
    # Set as outputs for GitHub Actions
    print(f"::set-output name=repo_url::{fields.get('repo_url','')}")
    print(f"::set-output name=root_path::{fields.get('root_path','')}")