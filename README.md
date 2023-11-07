DESCRIPTION

This is a project for the AirBnB clone console project. It is the first phase of the project. The project is an AirBnB clone that allows you to manage various classes such as users, states, cities and places. It aso provides a command interpreter for creating, retrieving, updating and deleting these classes as well as handling operations on them.

COMMAND INTERPRETER

It is a text-based interface that allows you to interact with the AirBnB clone. You can run the interpreter in both interactive and non-interactive modes.

USING THE COMMAND INTERPRETER

Running the Interpreter

To start the command interpreter, you will have to run the console.py script. You can do this in the following ways:

In interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

In non-interactive mode (using echo or script):

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

How to Use the Command Interpreter

Once the interpreter is running, some commands can be used to manage the objects. For example:

create: used to create a new object e.g 'create <class>'

show: used to retrieve an object from a file or database e.g "User.show('abc')"

all: retrieve a list of all objects in a class e.g "User.all()"

update: updates attributes of an objects e.g "User.update('abc')"

destroy: delete a specified object e.g "User.destroy('abc')"

count: return a count of objects in a class e.g "User.count()"

help: display all the commands available and a detailed info about each command e.g "help"

quit: exit the command interpreter e.g "quit"
