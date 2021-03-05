from src.git_downloader import GitDownloader
from src.github_api import GithubApi
from src.pmd_analyzer import PmdAnalyzer

if __name__ == '__main__':
    pages_to_get = 1

    for page in range(1, pages_to_get + 1):
        response = GithubApi.get_repositories(page)

        json_response = response.json()
        print(f"There are a total of {json_response['total_count']} results")

        repositories = json_response['items']
        # repo -> size, watchers, created_at, name, forks
        # print(i, repo['html_url'], repo['stargazers_count'])
        for i, repo in enumerate(repositories):
            repo_name = repo['name']
            directory = GitDownloader.download_project(repo_name, repo['clone_url'])
            PmdAnalyzer.analyze(repo_name, directory)
