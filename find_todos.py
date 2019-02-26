from os import listdir, getcwd
from os.path import isfile, join, isdir

def find_todos(dir_path):
    for f in listdir(dir_path):
        file_path = join(dir_path, f)
        if isfile(file_path) and has_todo(file_path):
            print(file_path)
        elif isdir(file_path):
            find_todos(file_path)

def has_todo(file_path):
    try:
        with open(file_path, 'r', encoding="utf8") as f:
            content = f.read()
    except Exception as e:
        return False
    return 'todo' in content.lower()

def run():
    cwd = getcwd()
    find_todos(cwd)

if __name__ == '__main__':
    run()