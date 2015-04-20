# OLP
One-liner Python

Execute arbitary python one-liners in the terminal

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
olp -d "get_bin = lambda s: str(bin(ord(s)))[2:]"
olp "get_bin('a')"
>>> 1100001
```

### Exposed modules
OLP lets you reference any module of your choosing in your one-liners.
This means you can do stuff like count the amount of recurrences of a file-extension in a file-tree fromt where you called OLP:
```
olp -d "amount_of_files = lambda ext: sum([1 for file in os.walk('.') if re.match('(.)+' + ext + '$', file)])
olp "amount_of_files('.pdf')"
>>> 23
```
OLP is configured to provide access to ```os```, ```sys```, ```re```, ```pkgutil```, and ```subprocess``` by default, but you can add any module you want!
To expose another module, run ```olp -i "module-name"``` and you're set!

#API
- -i "module-name" : Exposes a module for use in one-liners
- -d | -df "defintion" : Defines a variable or lambda, and exposes it to OLP, with an optional force paramater which will override existing uses of that name.
- -modules : Lists the modules exposed to OLP
- -e "text-editor" : Manually edit the custom defintions set with -d/-df, with your favourite text-editor!
- -h : print the help message.

#### Follow me on twitter, @_audun_
