#!/usr/bin/python

#IMPORTS
try :
    from OLPExtensions import *
except SyntaxError:
    print("OLP : There is a syntax error in the OLPExtensions. OLPExtensions \
           will be ignored. Run olp -c to reset the file, or olp -e to edit it")
except ImportError:
    open('OLPExtensions', 'a').close()
from OLPExceptions import *
from OLPModules import *

def main():
    #DEFINTIONS
    #These have been moved in here to decrease clutter in the global namespace

    extensions_location = "OLPExtensions.py"
    modules_location = "OLPModules.py"


    #IO
    def stdin_reader():
        '''
        Reads from stdin and yields every line as a string
        '''
        for line in sys.stdin.read().split('\n'):
            yield line

    def print_help_msg():
        print("Welcome to OLP! To use it, run olp \"your-python-command\" \n" + \
        "To define a new variable or lambda for permanent storage, use -d or -df. \n" + \
        "To import and expose a new module, use -i. \n" + \
        "If you want to manually edit these, run olp -e \"your-favourite-text-editor\"")

    def get_command():
        '''
        Stringify and return the command or definition given to OLP
        '''

        return " ".join([str(arg) for arg in sys.argv][1:]).strip()
    
    def run_command():
        '''
        Eval and stringify the command, then return the result.
        This function does not write to stdout.
        '''

        command = get_command()
        if command.strip() == "":
            print_help_msg()
        else:
            return str(eval(command))

    #EXTENSIONS
    def add_module(module_name):
        '''
        Adds a module import to OLPModules
        '''
        module_regex = re.compile("(\w)+$")
        if re.match(module_regex, module_name.strip()):
            with open(modules_location, "a") as modules:
                if module_name in globals():
                    print("OLP : Name " + module_name + " is already occupied in \
                    the global namespace")
                    print("OLP : Ignoring import attempt")
                else:
                    modules.write("import " + module_name + '\n')
        else:
            print("OLP : Not a valid module name")

    def define(some_input, force = False):
        '''
        Defines some variable or function for later use in OLP.
        This is made availabe through the import of OLPExtensions
        the next time the script is called.
        Will not overwrite existing definitions unless force is set
        to True
        '''

        definition_regex = re.compile('^((\w)+)( |=)*( |.)+')
        match_groups = re.match(definition_regex, some_input.strip())
        if match_groups:
            name = match_groups.group(2).strip()
            with open(extensions_location, "a") as definitions:
                if name in globals() and force == False:
                    print("OLP : Name " + name + " already in use. Use -df to ignore this warning")
                else:
                    definitions.write(some_input + '\n')
        else:
            print("Not a valid definition")

    def edit(editor):
        '''
        Opens a text editor to let you edit OLPs extensions
        '''
        os.system("/usr/bin/" + editor + " " +  extensions_location)



    #END DEFINITIONS


    #CONTROL FLOW
    command = get_command()
    command_params_regex = re.compile("^(-(df|d|i|e|h))+(.*)$")
    match = re.match(command_params_regex, command)
    if match:
        param = match.group(1).lower()
        if param == '-df':
            #Forced define
            define(match.group(3).strip(), force = True)
        elif param == "-d":
            #Define
            define(match.group(3).strip())
        elif param == "-i":
            #Import module
            add_module(match.group(3).strip())
        elif param == "-e":
            #Manually edit definitions
            edit(match.group(3).strip())
        elif param == "-h":
            #Print help msg
            print_help_msg()
        else:
            print("OLP : Unrecognised parameter")
    else:
        # OLP was passed no new definition or import, so we assume it's a regular command.
        result = run_command()
        if result:
            print(result)

if __name__ == "__main__":
    main()
