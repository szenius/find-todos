from os import listdir, getcwd
from os.path import isfile, join, isdir

def find_todos(dir_path):
    '''
    Recursively finds files in the given dir_path and its sub-directories. 
    When a file with the keyphrase TODO is found, print its file path. This is done regardless of case or usage.

    Input Arguments:
        dir_path: the directory in which we look for files with the keyphrase TODO.
    '''
    for f in listdir(dir_path):
        file_path = join(dir_path, f)
        if isfile(file_path) and has_todo(file_path):
            print(file_path)
        elif isdir(file_path):
            find_todos(file_path)

def has_todo(file_path):
    '''
    Returns True if the given file_path corresponds to a file with the keyphrase TODO in its content. Otherwise return False.
    If any Exception is raised, it is assumed that there is no TODO in the content, and False is returned.

    Input Arguments:
        file_path: corresponds to a file which we want to check the content for TODO.
    '''
    try:
        with open(file_path, 'r', encoding="utf8") as f:
            content = f.read()
        return 'todo' in content.lower()
    except Exception as e:
        return False

def run():
    '''
    Find the TODO keyphrase in files in the current working directory and its sub-directories.
    Print the file paths of such files.
    '''
    cwd = getcwd()
    find_todos(cwd)

if __name__ == '__main__':
    run()