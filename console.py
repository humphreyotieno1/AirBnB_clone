#!/usr/bin/python3
"""Command interpreter for the project"""
import cmd
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel

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

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
        if not arg:
            print("** class name missing **")
        elif arg not in storage.classes:
            print("** class doesn't exist **")
        else:
            new_instance = storage.classes[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_dict = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in obj_dict:
                print(obj_dict[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_dict = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in obj_dict:
                del obj_dict[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of instances"""
        if not arg:
            obj_dict =storage.all()
        elif arg not in storage.classes:
            print("**class doesn't exist**")
            return
        else:
            obj_dict = storage.all(storage.classes[arg])

        result = [str(obj) for obj in obj_dict.values()]
        print(result)

    def do_update(self, arg):
        """Updates an instance based on class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_dict = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in obj_dict:
                if len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    setattr(obj_dict[key], args[2], args[3])
                    obj_dict[key].save()
            else:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
