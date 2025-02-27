import requests
import os
from dotenv import load_dotenv

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def get_github_repos_and_commits(user_id):
    try:
        headers = {"Authorization": f"token {GITHUB_TOKEN}"}
        
        repos_url = f"https://api.github.com/users/{user_id}/repos"
        repos_response = requests.get(repos_url, headers=headers)

        # Handle errors by returning a string instead of raising an exception
        if repos_response.status_code != 200:
            return f"Error: {repos_response.status_code} - {repos_response.reason}"
        
        repos_data = repos_response.json()
        results = []

        for repo in repos_data:
            repo_name = repo.get("name")
            commits_url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
            commits_response = requests.get(commits_url, headers=headers)

            if commits_response.status_code != 200:
                return f"Error: {commits_response.status_code} - {commits_response.reason}"

            commits_data = commits_response.json()
            results.append(f"Repo: {repo_name} Number of commits: {len(commits_data)}")

        return "\n".join(results)

    except requests.exceptions.RequestException as e:
        return f"Error: {e}"  # Return an error message instead of raising an exception
