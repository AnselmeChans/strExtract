#!/usr/bin/python3.5
# coding:UTF8

#------------------------------> import librairies <----------------------------
import os
import re
import sys
import argparse
#-------------------------------------------------------------------------------

def recursive_recovery_files (args) :
    """
    Functions that recursively recovers all files in current repertory

    :param :args
    :return :None
    """

    for roots, _, filenames in os.walk(args.dir) :
        root = str(roots)
        for fileName in  filenames :
            filePath = os.path.join(root, fileName)
            print(filePath)
            str_extract(filePath, args)


def str_extract (filepath, args) :
    """
    Fuction that extract str in files

    :param :args :filepath
    :return :None
    """

    searchPattern = re.compile('\".*?\"|\'.*?\'')
    with open (filepath, 'r') as fileRead :
        for line in fileRead :
            for matchLine in searchPattern.finditer(line) :
                if args.path :
                    print(filepath, "\t", matchLine.group())
                else :
                    print(matchLine.group())


def check_arguments() :
    """
    The argparse module allows command line interface writing. The program defines
    which arguments are needed, and Argparse will understand how to parse those
    out of sys.argv.Argparse module will automatically pass help and usage messages

    :param file stdin : None
    :returns : None
    """

    parser = argparse.ArgumentParser(description="Read strings on quotes and double quotes from system files using python scripting")
    # =================>            dir argument        <========================
    parser.add_argument("dir")
    # ==========>      Optional argument : -p : --path     <====================
    parser.add_argument("-p", "--path", help="Display the path file", action='store_true')
    # =========>      Optional argument : -a : --all       <====================
    parser.add_argument("-a", "--all", help="all file", action='store_true')
    # ==========>         Optional argument : --suffix    <=====================
    parser.add_argument("--suffix", help= "select all suffix file")
    arguments = parser.parse_args()

    recursive_recovery_files (arguments)



# ---------------------------Main principal---------------------------------
if __name__ == "__main__" :

    check_arguments() # Call check_arguments
