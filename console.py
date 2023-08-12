#!/usr/bin/python3
"""a program that contains the entry point of the command interpreter"""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    __baseClass = {"BaseModel",}

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """allows end of file signal exiting the command interface
        """
        return True

    def emptyline(self):
        """prevents the prompt from executing the last command
        """
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel,  saves it as JSON,
        and prints the id
        """
        args = arg.split(" ")
        largs = len(args)

        if largs == 0:
            """checks If the class name is missing"""
            print("**class name missing**")
            return
        elif args[0] not in HBNBCommand.__baseClass:
            """checks If the class name doesn’t exist"""
            print("** class doesn't exist **")
            return
        else:
            """creates new instance of base model"""
            obj = eval(args[0] + "()")
            a_id = getattr(obj, 'id')
            print(a_id)
            storage.save()
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
