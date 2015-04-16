#This module holds all the functions for managing extensions and modules
#as well as executing scripts.
#It exists primarily to avoid cluttering up the global namespace, while
#also abstracting away the internatl workings of OLP from the control
#flow, managed the olp file
try :
    from OLPExtensions import *
    import OLPExtensions
except SyntaxError:
    print("OLP : There is a syntax error in the OLPExtensions. OLPExtensions \
           will be ignored. Run olp -e insert-text-editor to edit it")
except ImportError:
    open('OLPExtensions.py', 'a').close()
    import OLPExtensions
from OLPExceptions import *
from OLPModules import *
import OLPModules

#DEFINTIONS
#These have been moved in here to decrease clutter in the global namespace

#For some reason, sometimes the .py is loaded and other times the .pyc is loaded.
#I need access to the .py, so we need some regex magic
pyc_regex = re.compile("(.)+(\.pyc)$")
loaded_extensions = OLPExtensions.__file__
loaded_modules = OLPModules.__file__
if re.match(pyc_regex, loaded_extensions):
    extensions_location = loaded_extensions[0:len(loaded_extensions) - 1]
else:
    extensions_location = loaded_extensions

if re.match(pyc_regex, loaded_modules):
    modules_location = loaded_modules[0:len(loaded_modules) -1]
else:
    modules_location = loaded_modules

#IO
def print_help_msg():
    print("Welcome to OLP! To use it, run olp \"your-python-command\" \n" + \
    "To define a new variable or lambda for permanent storage, use -d or -df. \n" + \
    "To import and expose a new module, use -i. \n" + \
    "If you want to manually edit these, run olp -e \"your-favourite-text-editor\"")

def print_modules():
    with open(modules_location) as modules:
        for line in modules:
            module_name_regex = re.compile('^import (\w+)')
            module_name = re.match(module_name_regex, line.strip('\n')).group(1)
            print(module_name)

def get_command():
    '''
    Stringify and return the command or definition given to OLP
    '''

    return " ".join([str(arg) for arg in sys.argv][1:]).strip()

def run_command(command, _ = None):
    '''
    Eval and stringify the command, then return the result.
    This function does not write to stdout.
    '''
    if command.strip() == "":
        raise OLPNoCommand()
    else:
        return str(eval(command))


def stdin_reader():
    '''
    Reads from stdin and yields every line as a string
    '''
    for line in sys.stdin.read().split('\n'):
        if line.strip() != '':
            yield line.strip()

def run_command_on_stdin(command):
    results = []
    for line in stdin_reader():
        _ = line
        print(run_command(command, _))

def build_module_name_list():
    return [module[1] for module in pkgutil.iter_modules()]

def module_is_available(module_name):
    return module_name in build_module_name_list()

#EXTENSIONS
def add_module(module_name):
    '''
    Adds a module import to OLPModules
    '''
    module_regex = re.compile("(\w)+$")
    if re.match(module_regex, module_name.strip()):
        with open(modules_location, "a") as modules:
            if module_is_available(module_name):
                if module_name in globals():
                    raise OLPNameTaken(module_name)
                else:
                    modules.write("import " + module_name + '\n')
            else:
                raise OLPInaccessibleModule(module_name)
    else:
        raise OLPInvalidModuleName(module_name.strip())

def define(definition, force = False):
    '''
    Defines some variable or function for later use in OLP.
    This is made availabe through the import of OLPExtensions
    the next time the script is called.
    Will not overwrite existing definitions unless force is set
    to True
    '''

    definition_regex = re.compile('^(([a-zA-Z_])+)( |=)*( |.)+')
    match_groups = re.match(definition_regex, definition.strip())
    if match_groups:
        name = match_groups.group(1).strip()
        with open(extensions_location, "a") as definitions:
            if name in globals() and force == False:
                raise OLPNeedOverrideToDefine(name)
            else:
                definitions.write(definition + '\n')
    else:
        raise OLPInvalidDefinition(definition)

def edit(editor):
    '''
    Opens a text editor to let you edit OLPs extensions
    First tries to use specified editor, then value of $EDITOR
    environment variable, then vi.
    '''
    try:
        os.system((editor if editor else os.environ['EDITOR']) \
                  + " " +  extensions_location)
    except KeyError:
        print "No editor was specified. Attempting to open in vi..."
        os.system("vi " + extensions_location)

def clean(files_to_remove):
    '''
    Removes everything that has been added to OLPExtensions or OLPModules
    NOTE: This feature is not fully implemented yet! The little stub here 
    is basically just a note to myself showing kind of how it will work. 
    As you might see, it needs a redesign, all those 'with open' statements
    are kind of nasty.
    '''
    are_they_sure = raw_input("This action is irreversible. Are you sure? Y/N \n")
    default_extensions = "from OLPModules import * \n #That top line necessary, so please don't touch it!"
    default_modules = "import re \n import sys \n import os \n import pkgutil \n import string \n import subprocess"
    if are_they_sure:
        if files_to_remove.lower() == "extensions":
            os.remove(extensions_location)
            with open(extensions_location) as extensions:
                extensions.write(default_extensions)
        elif files_to_remove.lower() == "modules":
            os.remove(modules_location)
            with open(modules_location) as modules:
                modules.write(default_modules)
        elif files_to_remove.lower() == "both":
            os.remove(modules_location)
            os.remove(extensions_location)
            with open(extensions_location) as extensions:
                extensions.write(default_extensions)
            with open(modules_location) as modules:
                modules.write(default_modules)
