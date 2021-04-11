import json
import os

import xmltodict
import yaml

from src.utils.decorators import timed


class CheckStyle:
    with open("config/config.yml", "r") as yml_file:
        cfg = yaml.load(yml_file, Loader=yaml.FullLoader)['check_style']

    @staticmethod
    def _write_json_file(report_file_with_orig_ext, report_file):
        with open(report_file_with_orig_ext) as xml_file:
            data_dict = xmltodict.parse(xml_file.read())
            obj = json.dumps(data_dict)
            with open(f"{report_file}.json", "w") as json_file:
                json_file.write(obj)

    @staticmethod
    @timed
    def cs_analyze(project_name, directory):
        output_format = CheckStyle.cfg["output_format"]
        report_path = CheckStyle.cfg["report_file_path"]

        if not os.path.exists(report_path):
            os.mkdir(report_path)

        report_file = f'{report_path}/results_{project_name}'
        report_file_with_orig_ext = f"{report_file}.{output_format}"
        if not os.path.exists(report_file_with_orig_ext):
            command = f'{CheckStyle.cfg["base_command"]} -c {CheckStyle.cfg["checks_file"]} ' \
                      f'-f {output_format} -o {report_file_with_orig_ext} {directory}'

            os.system(command)
            # CheckStyle._write_json_file(report_file_with_orig_ext, report_file)
            print("\tCheckStyle DONE")
        else:
            print("\tAlready CheckStyle analyzed")
