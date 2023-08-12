#!/usr/bin/python3
"""a program that contains the entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

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



if __name__ == '__main__':
    HBNBCommand().cmdloop()
