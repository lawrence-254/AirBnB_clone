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

    def do_show(self, arg=None):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        largs = len(args)
        args = arg.split(" ")
        if largs == 0:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.__baseClass:
            print("** class doesn't exist **")
            return
        else:
            if args >= 2:
                id = "{}.{}".format(args[0], str(args[1]))
                obj_str = storage.all()
                if id in obj_str.keys():
                    obj_id = obj_str[id]
                    print(obj_id)
                    return
                else:
                    print("** no instance found **")
                    return

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        largs = len(args)
        args = arg.split(" ")
        if largs == 0:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.__baseClass:
            print("** class doesn't exist **")
            return
        else:
            if args == 2:
                id = "{}.{}".format(args[0], str(args[1]))
                obj_str = storage.all()
                if id in obj_str.keys():
                    del (obj_str[id])
                    return
                else:
                    print("** no instance found **")
                    return
            else:
                print("** instance id missing **")
                return

    def do_all(self, arg):
        """ Prints all string representation of all instances based
        or not on the class name"""
        inst_list = []
        args = arg.split(" ")
        if arg != "":
            if args[0] in HBNBCommand.__baseClass:
                for key, val in storage.all().items():
                    if type(val).__name__ == arg[0]
                    inst_list.append(str(val))
            else:
                print("** class doesn't exist **")
                return
        else:
            for key, val in storage.all().items()
            inst_list.append(str(val))
        print(inst_list)



if __name__ == '__main__':
    HBNBCommand().cmdloop()
