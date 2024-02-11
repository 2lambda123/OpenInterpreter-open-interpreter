import inspect
import os

from aifs import search


class Docs:
    def __init__(self, computer):
        self.computer = computer

    def search(self, query, module=None, paths=None):
        if paths:
            return search(query, file_paths=paths, python_docstrings_only=True)

        if module is None:
            module = self.computer

        # Get the path of the module
        module_path = os.path.dirname(inspect.getfile(module.__class__))

        # Use aifs to search over the files in the module path
        results = search(query, path=module_path, python_docstrings_only=True)
        return results
