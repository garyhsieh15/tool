import pathlib

class LookUpFile:

    def __init__(self, _path_string):
        self.path_string = _path_string

    def get_files_path(self):
        path = pathlib.Path(self.path_string)
        print("show path: %s", path)
        for pass_obj in path.iterdir():
            #print("show pass obj:", pass_obj)
            if pass_obj.match("*.py") and not pass_obj.match(".*.*"):
                print("show pass_obj.match('*.py'): %s" % pass_obj)


if __name__ == "__main__":
    new_obj = LookUpFile("../")
    
    new_obj.get_files_path()
