import sys
def get_command():
    return " ".join([str(arg) for arg in sys.argv][1:])

def main():
    print(eval(get_command()))

if __name__ == "__main__":
    main()
