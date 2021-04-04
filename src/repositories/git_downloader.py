import os

import git
import yaml


class GitDownloader:
    with open("config/config.yml", "r") as yml_file:
        cfg = yaml.load(yml_file, Loader=yaml.FullLoader)['git_downloader']

    @staticmethod
    def download_project(name, url):
        target_folder = GitDownloader.cfg['target_folder']
        if not os.path.exists(target_folder):
            os.mkdir(target_folder)

        target_path = f"{target_folder}/{name}"
        if os.path.exists(target_path):
            print(f"Repository {name} already exists. NOT cloning...")
        else:
            print(f'Cloning {target_path}', end='...')
            git.Git(target_folder).clone(url)
            print('SUCCESS')
        return target_path
