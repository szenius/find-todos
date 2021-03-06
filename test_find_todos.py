import unittest, io
from contextlib import redirect_stdout
from find_todos import find_todos, has_todo

class TestFindTodos(unittest.TestCase):
    def setUp(self):
        self.test_directory = "./test_resources/"
        self.files_with_todos = ["test_dir_1/test11.py", "test_dir_1/test12.py", "test_dir_2/test21.py", "test_dir_2/test22.py", "test_dir_3/test31.py"]
        self.files_without_todos = ["test_dir_2/test23.py"]

    def test_has_todo(self):
        for file in self.files_with_todos:
            self.assertTrue(has_todo(self.test_directory + file), msg="Did not find the TODO in this file!")
        for file in self.files_without_todos:
            self.assertFalse(has_todo(self.test_directory + file), msg="Found TODO in this file, but it doesn't exist!")

    def test_find_todos(self):
        # Capture prints to stdout
        f = io.StringIO()
        with redirect_stdout(f):
            find_todos(self.test_directory)
        output = f.getvalue().strip().splitlines()
        
        self.assertEqual(len(self.files_with_todos), len(output), msg="Numbers of expected and actual output lines are different!")
        for file in output:
            file = file.replace('\\', '/').replace(self.test_directory, '')
            self.assertTrue(file in self.files_with_todos, msg="{} does not have a TODO".format(file))
