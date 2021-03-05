import os

import yaml


class PmdAnalyzer:
    with open("config/config.yml", "r") as ymlfile:
        cfg = yaml.load(ymlfile)['pmd']

    @staticmethod
    def analyze(project_name, directory):
        print(f'Analyzing {directory}...')

        report_file = f'{PmdAnalyzer.cfg["report_file_path"]}/results_{project_name}.txt'

        command = f'{PmdAnalyzer.cfg["base_command"]} -d {directory} -f {PmdAnalyzer.cfg["output_format"]} ' \
                  f'-R {PmdAnalyzer.cfg["rule_sets"]} -l {PmdAnalyzer.cfg["language"]} -v {PmdAnalyzer.cfg["version"]} ' \
                  f'-r {report_file} -shortnames'

        os.system(command)
