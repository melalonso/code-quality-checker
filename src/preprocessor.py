from src.git_downloader import GitDownloader
from src.github_api import GithubApi
from src.static_analyzer.check_style import CheckStyle
from src.static_analyzer.pmd import Pmd
from src.util.timer import Timer


def analyze(p_repo_name: str, p_directory: str):
    print(f'Analyzing {directory}...')
    Pmd.analyze(p_repo_name, p_directory)
    CheckStyle.analyze(p_repo_name, p_directory)


if __name__ == '__main__':
    pages_to_get = 1
    timer = Timer()

    print("Starting to get repositories from GitHub APIs")
    for page in range(1, pages_to_get + 1):
        response = GithubApi.get_popular_repositories(page)
        print(f"=> Got page [{page}]")

        json_response = response.json()
        # print(f"There are a total of {json_response['total_count']} results")

        repositories = json_response['items']
        # repo -> size, watchers, created_at, name, forks
        # print(i, repo['html_url'], repo['stargazers_count'])
        for i, repo in enumerate(repositories):
            timer.start()
            repo_name = repo['name']
            directory = GitDownloader.download_project(repo_name, repo['clone_url'])
            analyze(repo_name, directory)
            timer.stop()
            print("-" * 70)
