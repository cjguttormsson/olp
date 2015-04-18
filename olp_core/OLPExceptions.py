class OLPErrorTemplate(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return repr(self.msg)

class OLPNameTaken(OLPErrorTemplate):
    def __init__(self, name):
        self.msg = "Name " + name + " is already occupied in the global namespace"


        

