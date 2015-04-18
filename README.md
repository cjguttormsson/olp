# OLP
One-liner Python

Execute arbitary python one-liners in the terminal

# Installation
Clone the repo and run ```sh setup.sh```
If you don't want me messing around in your /usr/local/bin ofcourse, you can just use good old ```chmod +x olp``` and then ```export PATH=$PATH:path-to-repo```

# Features
Execute arbitrary functions in the CLI
```
olp "sum(range(10))"
>>> 45
```

However, that's been done a million times before, so here's some neat stuff that OLP can do that similar projects can't.

## Extensibility
Let's make it get binary values of characters!
```
olp -d "get_bin = lambda s: str(bin(ord(s)))[2:]"
olp "get_bin('a')"
>>> 1100001
```

## Exposed modules
OLP lets you reference any module of your choosing in your one-liners. OLP is configured to provide os, re, and sys. To add another module run ```olp "edit()"``` and add the import to the top of the file.
This means you can do stuff like count the amount of recurrences of a file-extension in a file-tree fromt where you called OLP:
```
olp -d "amount_of_files = lambda ext: sum([1 for file in os.walk('.') if re.match(ext + '$', file)])
olp "amount_of_files('.pdf')"
```
