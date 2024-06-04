# print_arguments/main.py
import argparse
from pathlib import Path
import json
import os
import sys

def print_arguments(arguments: list[str]):
    for argument in arguments:
        print(argument)

def get_file_content(file_path):
    return json.loads(Path(file_path).read_text())

def kernelspec_extraction(content):
    return content["metadata"]["kernelspec"]["name"]

def python38_kernel_fixer(file_path):
    original_content = get_file_content(file_path)
    new_content = get_file_content(file_path)
    new_content["metadata"]["kernelspec"]["name"] = "python38"
    if original_content != new_content:
        with open(file_path, "w") as json_file:
            json.dump(new_content, json_file, indent=2, ensure_ascii=False)
        return 1
    else:
        return 0
    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filepaths", nargs="*")
    args = parser.parse_args()

    exit_code = 0

    for filepath in args.filepaths:
        if not filepath.endswith(".ipynb"): continue
        return_value = python38_kernel_fixer(filepath)
        print(return_value)
        if return_value != 0:
            print(f'Fixing kernel in {filepath}')
        exit_code |= return_value

    return exit_code

if __name__ == "__main__":
    raise SystemExit(main())