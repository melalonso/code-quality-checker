import os

import git
import yaml


class GitDownloader:
    with open("config/config.yml", "r") as ymlfile:
        cfg = yaml.load(ymlfile)['git_downloader']

    @staticmethod
    def download_project(name, url):
        target_folder = GitDownloader.cfg['target_folder']
        if not os.path.exists(target_folder):
            os.mkdir(target_folder)

        target_path = f"{target_folder}/{name}"
        if os.path.exists(target_path):
            print(f"Repository {name} already exists. NOT cloning...")
        else:
            git.Git(target_folder).clone(url)
            print(f'Successfully cloned {target_path}')
        return target_path
