# print_arguments/main.py
import argparse
from pathlib import Path
import json
import os

def print_arguments(arguments: list[str]):
    for argument in arguments:
        print(argument)

def get_file_content(file_path):
    return json.loads(Path(file_path).read_text())

def kernelspec_extraction(content):
    return content["metadata"]["kernelspec"]["name"]

def python38_kernel_fixer(file_path):
    original_content = get_file_content(file_path)
    # original_content["metadata"]["kernelspec"]["name"] = "python38"
    with open(file_path, "w") as json_file:
        json.dump(original_content, json_file, indent=2, ensure_ascii=False)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filepaths", nargs="*")
    args = parser.parse_args()

    print_arguments(args.filepaths)
    for filepath in args.filepaths:
        if not filepath.endswith(".ipynb"): continue
        kernelspec = kernelspec_extraction(get_file_content(filepath))
        if kernelspec == "python38": continue
        python38_kernel_fixer(filepath)

if __name__ == "__main__":
    main()