class OLPErrorTemplate(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return repr("OLP : " + self.msg)

class OLPNameTaken(OLPErrorTemplate):
    def __init__(self, name):
        self.msg = "Name " + name + " is already occupied in the global namespace"

class OLPNeedOverrideToDefine(OLPErrorTemplate):
    def __init__(self, definition_name):
        self.msg = "Name " + definition_name + " is occupied in the global namespace, but you can override its definition by using the -df paramter"

class OLPNoCommand(OLPErrorTemplate):
    def __init__(self):
        self.msg = "No command given"

class OLPInaccessibleModule(OLPErrorTemplate):
    def __init__(self, module_name):
        self.msg = "Module " + module_name + " is inaccessible"

class OLPUnrecognisedParameter(OLPErrorTemplate):
    def __init__(self, parameter):
        self.msg = "Unrecognised paramter " + parameter

class OLPInvalidDefinition(OLPErrorTemplate):
    def __init__(self, definition):
        self.msg = "Invalid definition: " + definition

class OLPInvalidModuleName(OLPErrorTemplate):
    def __init__(self, module_name):
        self.msg = "Invalid module name: " + module_name
