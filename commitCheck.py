from github import Github
import os

def check_for_new_commits(repo_name, access_token):
    # Initialize PyGithub with access token
    g = Github(access_token)

    try:
        # Get the repository
        repo = g.get_repo(repo_name)

        # Get the latest commit
        latest_commit = repo.get_commits()[0]

        # Get the SHA of the latest commit
        latest_commit_sha = latest_commit.sha

        # Check if 'last_commit.txt' file exists, if not, create it
        if not os.path.exists("last_commit.txt"):
            with open("last_commit.txt", "w") as f:
                f.write("")

        # Get the SHA of the last checked commit from the file
        with open("last_commit.txt", "r") as f:
            last_checked_commit_sha = f.read().strip()

        # Compare the latest commit with the last checked commit
        if latest_commit_sha != last_checked_commit_sha:
            print("New commit found!")
            print(f"Commit SHA: {latest_commit_sha}")
            # Update the last checked commit SHA in the file
            with open("last_commit.txt", "w") as f:
                f.write(latest_commit_sha)
        else:
            print("No new commits since the last check.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace 'your_repo' with the repository name and 'your_access_token' with your GitHub access token
    repo_name = "JyotiChauhan24/CI-CD-PipelineDevops"
    access_token = ""

    check_for_new_commits(repo_name, access_token)

