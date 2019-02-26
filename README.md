# Find Todos
A simple script to list paths of all files with the keyword `TODO` in their content. This script starts looking for files in its current working directory, and also explores all sub-directories.

## User Guide
To use this project, simply place the `find_todos.py` script in any directory from which you want to start looking for files with `TODO`. Then run the following:

```
python find_todos.py
```

Please note that all of the following will be detected:
* Files with the word `TODO`, regardless of case
* Files with the word `TODO`, regardless of usage (even those represent in the code will be detected)

## Developer's Guide

### Installation
This project was developed in `Python 3.6.5`. Please install an equivalent version.

No external dependencies were used. All libraries used are built-in Python libraries.

### Running Unit Tests
The default `test_resources/` have test files set up for us to run unit tests on. However, if you wish to run unit tests on your own test files, please modify the `setUp()` method in `test_find_todos.py`:

```python
def setUp(self):
    self.test_directory = "./test_resources/" # The source directory where we will start looking for files with TODOs
    self.files_with_todos = ["test_dir_1/test11.py", "test_dir_1/test12.py", "test_dir_2/test21.py", "test_dir_2/test22.py", "test_dir_3/test31.py"] # File paths leading to files with TODOs. Should be relative to the source directory.
    self.files_without_todos = ["test_dir_2/test23.py"] # File paths leading to files without TODOs. Should be relative to the source directory.
```

Once done, run the following.
```
python -m unittest discover
```

## Future Work
* Testing via dynamic creation of directories and files
* Make into pip package for easy installation
* Integration tests