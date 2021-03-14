import requests


class GithubApi:
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

    @staticmethod
    def _base_url():
        return 'https://api.github.com'

    @staticmethod
    def get_popular_repositories(page_number, results_per_page=5, sort_criteria='stars', order='desc', lang='java'):
        """
        Searches and returns the repositories based on the search criteria
        """
        try:
            search_params = f'sort={sort_criteria}&order={order}&per_page={results_per_page}&page={page_number}&q=language:{lang}'
            url = f"{GithubApi._base_url()}/search/repositories?{search_params}"
            return requests.get(url)
        except Exception:
            print('There was an exception getting the repositories')
