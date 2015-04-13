import sys, os, itertools, re
from OLPExtensions import *

def get_command():
    '''
    Stringify and return the command or definition given to OLP
    '''

    return " ".join([str(arg) for arg in sys.argv][1:]).strip()

def define(some_input, force = False):
    '''
    Defines some variable or function for later use in OLP.
    This is made availabe through the import of OLPExtensions
    the next time the script is called.
    Will not overwrite existing definitions unless force is set
    to True
    '''

    definition_regex = re.compile('^((.)+=(.)+)+')
    if re.match(definition_regex, some_input):
        with open("/usr/local/bin/OLPExtensions.py", "wr") as definitions:
            definitions.write(some_input + '\n')
    else:
        print("Not a valid definition")

def run_command():   
    '''
    Eval and stringify the command, then return the result.
    This function does not write to stdout.
    '''

    command = get_command()

    try:
        return str(eval(command))
    except SyntaxError:
        if command.strip() == "":
            return "OLP : No command given"
        else:
            return "OLP : There was a syntax error in your command!"

def run_command_from_pipe():
    '''
    Takes a set of values passed in from stdin, running the command on
    each element, and yields the results
    '''

    stdin = sys.stdin
    

def main():
    command = get_command()
    if command[0:2] == "-d":
        define(command[3:])
    else:
        result = run_command()
        if result:
            print(result)

if __name__ == "__main__":
    main()
