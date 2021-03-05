import os


class PmdAnalyzer:
    _base_command = '/Users/melvin.elizondo/pmd-bin-6.24.0/bin/run.sh pmd'
    _output_format = 'csv'
    _rule_sets = '/Users/melvin.elizondo/Documents/UNIVERSIDAD/TESIS/code-quality-checker/PMD/my_ruleset.xml'
    _language = 'java'
    _version = 8

    @staticmethod
    def analyze(project_name, directory):
        print(f'Analyzing {directory}...')

        report_file = f'results_{project_name}.txt'

        command = f'{PmdAnalyzer._base_command} -d {directory} -f {PmdAnalyzer._output_format} ' \
                  f'-R {PmdAnalyzer._rule_sets} -l {PmdAnalyzer._language} -v {PmdAnalyzer._version} ' \
                  f'-r {report_file} -shortnames'

        os.system(command)
