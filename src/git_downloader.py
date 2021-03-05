import os

import git


class GitDownloader:
    _target_folder = '/Users/melvin.elizondo/Documents/repos'

    @staticmethod
    def download_project(name, url):
        if not os.path.exists(GitDownloader._target_folder):
            os.mkdir(GitDownloader._target_folder)

        target_path = f"{GitDownloader._target_folder}/{name}"
        if os.path.exists(target_path):
            print(f"Repository {name} already exists. NOT cloning...")
        else:
            git.Git(GitDownloader._target_folder).clone(url)
            print(f'Successfully cloned {target_path}')
        return target_path
