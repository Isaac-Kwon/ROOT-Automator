import sys, os, subprocess
from automation import runMacro
from pattern import findFromDir

MacroName = "Hitmap.C"
DefaultOutputRoot = "output.root"

#
# path seperator
# will contain following procedure.
#
# 1. seperate directory and filename
# 2. if relative path > return relative directory path and filename
# 3. if absolute path > return absolute path and directory 
#
# Flow
# 1. Judge Absolute path or Relative path
# >> "path".find("/") if 0 or "path".find("~/") is 0
#
# 2-1 relative path 
# a. split by slash, seperate by directory
# b. 
#

def receiveName(msg):
    user_input = input(msg)
    if user_input is "":
        return False
    else:
        return user_input

def confirmYN(msg, truemsg="", falsemsg=""):
    while True:
        user_qa = input(msg)
        if not user_qa in ["Y", "y", "N", "n"]:
            print("unidentified answer, re-input")
            continue
        else:
            if user_qa in ["N", "n"]:
                print(falsemsg)
                return False
            elif user_qa in ["Y", "y"]:
                print(truemsg)
                return True
            else:
                raise Exception

if __name__ == "__main__":
    print(
    """HIC Digital Scan Analysis Automation Script
    Input object to analysis.
    You can use in input wildcard like * (asterisk) and ? (Question Mark)""")
    while True:
        user_input_location = input("Input (put blank if you want quit): ") 
        if user_input_location is '':
            exit()
        findloc = '/'.join(user_input_location.split("/")[:-1])
        if user_input_location.find('/') is 0:
            findloc = '/' + findloc
        if findloc is "":
            findloc = '.' 
        print("finding %s \n at %s" %(findloc,  
        user_list = findFromDir(, location=findloc)
        print(user_list) 
    user_input_name = input("Input outpot ROOT file (If blank, it will be searching name): ")
    user_input_location_temp = user_input_location.split("/")[-1].replace("*","").replace("?","")
    if not user_input_name is "":
        pass
    elif user_input_location_temp is "":
        user_input_name = DefaultOutputRoot 
    user_list = [user_input_name, len(user_list)] + user_list
    a = runMacro(MacroName, arglist = user_list, once=False)
    a.wait()


