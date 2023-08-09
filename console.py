#!/usr/bin/python3
"""a program that contains the entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """used to quit the program"""
        return True

    def do_EOF(self, line):
        """allows end of file function"""
        return True

    def emptyline(self):
        """prevents the prompt from executing the last command"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
