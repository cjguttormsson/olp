import sys, os, itertools
def get_command():
    return " ".join([str(arg) for arg in sys.argv][1:])

def main():
    try : 
        print(eval(get_command()))
    except SyntaxError:
        if get_command().strip() == "":
            #We presume the call was an error and just pass the error silently
            pass
        else:
            print("There was a syntax error in your command, please check for typos!")

if __name__ == "__main__":
    main()
