import fnmatch
import os



class path(str):
    def __init__(self, part):
        self.super().__init__(part)
    def structure(self):
        return self.split("/")
    def isAbsolute(self):
        return self.isRoot() or self.isHome()
    def isRelative(self):
        return not self.isAbsolute()
    def isRoot(self):
        if self.structure[0] is "":
            return True
    def isHome(self):
        if self.structure[0] is "~":
            return True
    def isdir(self):
        return os.path.isdir(self.fullpath())
    def isfile(self):
        return os.path.isfile(self.fullpath())
    def dirfile(self):
        if self.isdir():
            directory = self.__repr__()
            filename = ""
        if self.isfile():
            directory = os.path.dirname(self.__repr__())
            filename =  
        return directory, filename
    def directory(self):
        directory, filename = self.dirfile()
        return directory
    def file(self): #return last structure
        directory, filename = self.dirfile()
        return filename
    def fullpath(self):
        return self.__repr__()
    def findfile(self, findname):
        if self.isdir():
            return findFromDir(findname, location=self.directory())
        elif self.isfile():
            raise Exception("Path is not directory")




def findFromDir(findname, location='.', verbose=False):
    return findFormList(os.listdir(location), findname, verbose=verbose)

def findFormList(motherlist, findname, verbose=False):
    namelist = list()
    for f in motherlist:
        if fnmatch.fnmatch(f, findname):
            if verbose is True:
                print(f)
            namelist.append(f)
    return namelist

def main():
    pass

if __name__ == "__main__":
    main()
