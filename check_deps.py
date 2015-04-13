import os
def check_deps(deps):
    for dep in deps:
        if dep not in os.listdir('.'):
            return False
    return True
