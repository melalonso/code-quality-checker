import os

import yaml


class Pmd:
    with open("config/config.yml", "r") as yml_file:
        cfg = yaml.load(yml_file, Loader=yaml.FullLoader)['pmd']

    @staticmethod
    def analyze(project_name, directory):
        output_format = Pmd.cfg["output_format"]
        report_path = Pmd.cfg["report_file_path"]

        if not os.path.exists(report_path):
            os.mkdir(report_path)

        report_file = f'{report_path}/results_{project_name}.{output_format}'
        if not os.path.exists(report_file):
            command = f'{Pmd.cfg["base_command"]} -d {directory} -f {output_format} ' \
                      f'-R {Pmd.cfg["rule_sets_file"]} -l {Pmd.cfg["language"]} ' \
                      f'-v {Pmd.cfg["version"]} -r {report_file} -shortnames -no-cache'

            os.system(command)
            print("\tPMD DONE")
        else:
            print("\tAlready PMD analyzed")
