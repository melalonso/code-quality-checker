from collections import defaultdict

import pandas as pd
import yaml

with open("config/config.yml", "r") as yml_file:
    cfg = yaml.load(yml_file, Loader=yaml.FullLoader)


def get_rules_violations(results_file):
    """
    Returns an object with the following structure
        [
            {
                rule: <rule>,
                violate: [("", n), ("", m), ...,()]
                not_violate: ["", ""]
            },
            ...
        ]

    """
    df = pd.read_csv(results_file)

    result = []

    all_rules = df['Rule'].unique()
    all_files = df['File'].unique()

    for rule in all_rules:
        rule_violations = df.loc[df['Rule'] == rule]
        files_violating = defaultdict(int)

        for index, row in rule_violations.iterrows():
            files_violating[row['File']] += 1

        files_not_violating = [f for f in all_files if f not in files_violating]

        sorted_violations = sorted(files_violating.items(), key=lambda x: x[1], reverse=True)

        result.append({'rule': rule, 'violate': sorted_violations, 'not_violate': files_not_violating})

    return result


def train(rule, project_name):
    rule_name, files_violating, files_not_violating = rule.values()

    print(f"Training Rule=[{rule_name}] Violate=[{len(files_violating)}] NotViolate=[{len(files_not_violating)}]")
    cloned_path = cfg['git_downloader']['target_folder']

    for file in files_not_violating:
        files_path = f'{cloned_path}/{project_name}/{file}'
        # print(files_path)
        # with open(files_path) as f:
        #     lines = f.readlines()
        #     print(lines)

    for file in files_violating:
        files_path = f'{cloned_path}/{project_name}/{file[0]}'
        # print(files_path)
        # with open(files_path) as f:
        #     lines = f.readlines()
        #     print(lines)


def postprocess_pmd(project_names: list):
    # Postprocessing each of the PMD results for every project
    for project in project_names:
        print()
        print(f" Postprocessing {project} ".center(80, "-"))
        results_path = cfg['pmd']['report_file_path']  # cfg['check_style']['report_file_path']
        results_file = f'{results_path}/results_{project}.csv'
        rule_violations_list = get_rules_violations(results_file)

        # For each rule we have the list of files
        # either violating or not violating it
        # This basically means positive and negative examples to train with
        for rule in rule_violations_list:
            """
            This approach would work if training the neural network incrementally, that is 
            adding the rule results for a project at a time.
            """
            train(rule, project)
        print("DONE")


def postprocess_check_style(project_names: list):
    print("To be implemented")


def postprocess(project_names: list):
    print("\n")
    print(" POSTPROCESS: Starting to process results from PMD and CheckStyle ".center(100, "#"))
    postprocess_pmd(project_names)
    postprocess_check_style(project_names)
