import requests
import pprint
import git
import os


class GithubApi:

    def _base_url(self):
        return 'https://api.github.com/'

    def get_repos(self):
        pass


def analyze_repos():
    # /Users/melvin.elizondo/pmd-bin-6.24.0/bin/run.sh pmd -d /Users/melvin.elizondo/Documents/UNIVERSIDAD/TESIS/code-quality-checker/repos/elasticsearch/buildSrc/src/main/java/org/elasticsearch/gradle/ResolveAllDependencies.java -f text -R rulesets/java/quickstart.xml
    pass

"""
There's no official API for the Trending Repos
url != 'https://api.github.com/trending/java?since=monthly&spoken_language_code=en'

GitHub Trending API · Apiary - DOES NOT WORK


Projects
https://github.com/andygrunwald/go-trending - FOR GO LANG
https://github.com/sheharyarn/github-trending - FOR RUBY
https://github.com/rochefort/git-trend - FOR RUBY
https://github.com/andygrunwald/TrendingGithub - A TWITTER BOT
https://github.com/sikang99/hub-trend/ - FOR GO 

Using search repositories endpoint with customized query
https://docs.github.com/en/github/searching-for-information-on-github/searching-for-repositories

size:50..120 matches repositories that are between 50 KB and 120 KB.

followers:>=10000
forks:>=205
stars:>=500 fork:true language:php matches repositories with the at least 500 stars, including forked ones, that are written in PHP.
"""

if __name__ == '__main__':

    pages_to_get = 1
    results_per_page = 5  # per_page max is 100
    sort_criteria = 'stars'
    order = 'desc'

    for page in range(1, pages_to_get + 1):

        url = f"https://api.github.com/search/repositories?sort={sort_criteria}&order={order}&per_page={results_per_page}&page={page}&q=language:java"
        resp = requests.get(url)

        if resp.status_code != 200:
            raise Exception(f'GET {url} {resp.status_code} for page {page}')

        json_response = resp.json()
        print(f"There are a total of {json_response['total_count']} results")

        repositories = json_response['items']

        for i, repo in enumerate(repositories):
            # size, watchers, created_at, name, forks
            print(i, repo['html_url'], repo['stargazers_count'])
            if os.path.exists(f"../repos/{repo['name']}"):
                print("Repo exists not cloning")
            else:
                git.Git("../repos/").clone(repo['clone_url'])

    analyze_repos()
