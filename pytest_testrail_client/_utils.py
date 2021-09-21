from os import listdir, path

from gherkin.token_scanner import TokenScanner
from gherkin.parser import Parser


def _get_feature(file_path: str):
    """ Read and parse given feature file"""
    print('Reading feature file ', file_path)
    file_obj = open(file_path, 'r')
    steam = file_obj.read()
    parser = Parser()
    return parser.parse(TokenScanner(steam))


def _write_feature(file_path: str, line, column, value):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        origin = lines[line-1]
        lines[line - 1] = ''
        for i in range(1, column):
            lines[line-1] += ' '
        lines[line-1] += value + origin.strip() + '\n'

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)


def _get_list_of_files(absolute_path):
    if path.isdir(absolute_path):
        list_of_file = listdir(absolute_path)
    else:
        list_of_file = [absolute_path]
    all_files = list()
    for entry in list_of_file:
        full_path = path.join(absolute_path, entry)
        if path.isdir(full_path):
            all_files = all_files + _get_list_of_files(full_path)
        else:
            if full_path.endswith('.feature'):
                all_files.append(full_path)
    return all_files
