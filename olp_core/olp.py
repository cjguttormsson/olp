try :
    from OLPExtensions import *
except SyntaxError:
    print("OLP : There is a syntax error in the OLPExtensions. OLPExtensions will be ignored")
from OLPExceptions import *
from OLPModules import *

extensions_location = "/usr/local/bin/OLPExtensions.py"
modules_location = "/usr/local/bin/OLPModules.py"

def stdin_reader():
    for line in sys.stdin.read().split('\n'):
        yield line

def get_command():
    '''
    Stringify and return the command or definition given to OLP
    '''

    return " ".join([str(arg) for arg in sys.argv][1:]).strip()

def add_module(module_name):
    '''
    Adds a module import to OLPModules
    '''
    module_regex = re.compile("(\w)+$")
    if re.match(module_regex, module_name.strip()):
        with open(modules_location, "a") as modules:
            if module_name in globals():
                print("OLP : Name " + module_name + " is already occupied in the global namespace")
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

def edit():
    '''
    Opens vi to let you edit OLPs extensions
    '''
    os.system("/usr/bin/vi " + extensions_location)

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

def main():
    command = get_command()
    command_params_regex = re.compile("^(-(df|d|i))+(.*)$")
    match = re.match(command_params_regex, command)
    if match:
        param = match.group(1)
        if param == '-df':
            print("Forced define")
            define(match.group(3).strip(), force = True)
        elif param == "-d":
            define(match.group(3).strip())
        elif param == "-i":
            add_module(match.group(3).strip())
        else:
                print("OLP : Unrecognised parameter")
    else:
        result = run_command()
        if result:
            print(result)

if __name__ == "__main__":
    main()
