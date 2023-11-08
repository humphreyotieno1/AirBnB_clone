#!/usr/bin/python3
"""Command interpreter for the project"""
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Exit using CTRL+D"""
        print()
        return True
    
    def emptyline(self):
        """Repeat last command"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
