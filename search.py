import os
import sys

class Searcher:
    def __init__(self, parent):
        self.subdirectories = []
        self.duplicate = {}
        self.destionation = parent
        self.go_to_directory(self.destionation)

    def go_to_directory(self, destination):
        os.chdir(destination)

    def get_sub_directories(self):
        print("\tGet Subdirectories")
        for entry in os.scandir(self.destionation):
            if (os.DirEntry.is_dir(entry)):
                self.subdirectories.append(entry.path)

    def explore_subdirectory(self):
        print("\tFind Duplicates")
        for entry in self.subdirectories:
            self.go_to_directory(entry)
            self.explore_duplicates()
        self.go_to_directory(self.destionation)

    def explore_duplicates(self):
        print("\t\tFinding Duplicates Under " + os.getcwd() + " ...")
        for entry in os.scandir(os.getcwd()):
            if (os.DirEntry.is_file(entry)):
                prefix = entry.name.split('.')[0]
                if (self.duplicate.get(prefix) == None):
                    self.duplicate[prefix] = []
                self.duplicate[prefix].append(entry.path)
        print("\t\t\tDone")

    def write_output(self):
        with open("duplicates.txt", 'w') as f: 
            for key, value in self.duplicate.items(): 
                f.write('%s:%s\n' % (key, value))


if __name__ == '__main__':

    arg = sys.argv
    arg_num = len(arg)
    if (arg_num > 2):
        print('Invalid Arguments')
        sys.exit(1)
    elif (arg_num == 2):
        searcher = Searcher(arg[1])
    else:
        searcher = Searcher(os.getcwd())
    
    print("Program Starts")

    searcher.get_sub_directories()

    searcher.explore_subdirectory()

    searcher.write_output()

    print("Program Ends\n\n")

    print(searcher.duplicate)


