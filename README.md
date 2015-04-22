# OLP
One-liner Python

Execute arbitary python one-liners in the terminal

OLP is reasonably stable but still needs testing.
# Installation
OLP is installed through python distutils, like so:
```
git clone https://github.com/audun-/olp
cd olp/olp_core
python setup.py sdist
python setup.py install
```


# Features
Execute arbitrary functions in the CLI
```
olp "sum(range(10))"
>>> 45
```

However, that's been done a million times before, so here's some more neat things OLP can do! 

### Extensibility
OLP lets you define functions and values that can be stored for use later.
Let's make it get binary values of characters!
```
olp -d "get_bin = lambda c: str(bin(ord(c)))[2:]"
olp "get_bin('a')"
>>> 1100001
```

### Exposed modules
OLP lets you reference any module of your choosing in your one-liners.
This means that you can do stuff like programmatically remove files down an entire file tree, like so:
```
olp -d "remove_files_with_ext = lambda ext: [os.remove(file) for file in os.walk('.') if re.match('(.)+\.' + ext + '$', file)]"

#Say for example you want o remove all the .pyc files in a project
#cd to your project root and...
olp "remove_files_with_ext('pyc')
#Voila
```
OLP is configured to provide access to ```os```, ```sys```, ```re```, ```pkgutil```, and ```subprocess``` by default, but you can add any module you want!
To expose another module, run ```olp -i "module-name"``` and you're set!

### Pipes
OLP supports reading from the STDIN pipe. You command is then run once per line in STDIN, and the value of each line is assigned to '_' at run-time.
To use OLP with STDIN, use the '-p' parameter.

Example use:
```
cat test.txt
>>> 'Python is awesome!
>>> So little code, so much power.'
olp -d "get_bin_of_char = lambda c: str(bin(ord(c)))[2:]"
olp -d "get_bin_of_string = lambda s: "".join([get_bin_of_char(c) for x in s])
cat test.txt | olp -p "get_bin_of_string(_)"
>>> 101000011110011110100110100011011111101110100000110100111100111000001100001111011111001011110011110111111011011100101100001
>>> 10100111101111100000110110011010011110100111010011011001100101100000110001111011111100100110010110110010000011100111101111100000110110111101011100011110100010000011100001101111111011111001011110010101110
```
#API
- -i "module-name" : Exposes a module for use in one-liners
- -d | -df "defintion" : Defines a variable or lambda, and exposes it to OLP, with an optional force paramater which will override existing uses of that name.
- -modules : Lists the modules exposed to OLP
- -e "text-editor" : Manually edit the custom defintions set with -d/-df, with your favourite text-editor!
- -h : print the help message.
- -p : Read from STDIN pipe.

#### Follow me on twitter, @\_audun\_
