from src.repositories.git_downloader import GitDownloader
from src.repositories.github_api import GithubApi
from src.static_analyzers.check_style import CheckStyle
from src.static_analyzers.pmd import Pmd
from src.utils.timer import Timer


def run_static_analizers(p_repo_name: str, p_directory: str):
    print(f'Analyzing {p_directory}...')
    Pmd.analyze(p_repo_name, p_directory)
    CheckStyle.analyze(p_repo_name, p_directory)


def preprocess():
    project_names = []
    pages_to_get = 1
    timer = Timer()

    print(" PREPROCESS: Starting to get repositories from GitHub APIs ".center(100, "#"))
    for page in range(1, pages_to_get + 1):
        response = GithubApi.get_popular_repositories(page, results_per_page=5)
        print()
        print(f" Got page [{page}] of [{pages_to_get}] ".center(80, "="), end='\n\n')

        json_response = response.json()
        repositories = json_response['items']
        # print(f"There are a total of {json_response['total_count']} results")

        # repo -> size, watchers, created_at, name, forks
        # print(i, repo['html_url'], repo['stargazers_count'])
        for i, repo in enumerate(repositories):
            timer.start()
            repo_name = repo['name']
            directory = GitDownloader.download_project(repo_name, repo['clone_url'])
            run_static_analizers(repo_name, directory)
            timer.stop()
            print("-" * 70)
            project_names.append(repo_name)

    return project_names
