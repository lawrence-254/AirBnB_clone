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
        largs = len(arg)

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
        largs = len(arg)
        args = arg.split(" ")
        if largs == 0:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.__baseClass:
            print("** class doesn't exist **")
            return
        else:
            if len(arg) >= 2:
                id = "{}.{}".format(arg[0], str(arg[1]))
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
        largs = len(arg)
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
                    if type(val).__name__ == arg[0]:
                        inst_list.append(str(val))
            else:
                print("** class doesn't exist **")
                return
        else:
            for key, val in storage.all().items():
                inst_list.append(str(val))
        print(inst_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        pattern = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        a_match = re.search(regx, args)
        uid_match = a_match.group(2)
        cls_name_match = a_match.group(1)
        attr_match = a_match.group(3)
        val_match = a_match.group(4)
        if a_match:
            if cls_name_match in HBNBCommand.__baseClass:
                if uid_match:
                    id = "{}.{}".format(cls_name_match, uid_match)
                    if id in storage.all():
                        if attr_match:
                            if val_match:
                                datatype = None
                                if not re.search('^".*"$', val_match):
                                    if '.' in val_match:
                                        datatype = float
                                    else:
                                        datatype = int
                                else:
                                    val_match = val_match.replace('"', '')
                                    attrs = attributes[cls_name_match]
                                    if attr_match in attrs:
                                        val_match = attrs[attr_match](val_match)
                                    elif datatype:
                                        try:
                                            val_match = datatype(val_match)
                                        except ValueError:
                                            pass
                                        setattr(storage.all()[id], attr_match,
                                                val_match)
                                        storage.all()[id].save()
                                    else:
                                        print("** value missing **")
                            else:
                                print("** attribute name missing **")
                        else:
                            print("** no instance found **")
                    else:
                        print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
            else:
                print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
