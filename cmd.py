#!/usr/bin/env python3

import cmd

class Command(cmd.cmd):
    """Interprete"""
    prompt = "hbnb:"

    def do_command1(self, args):
        """command help"""
        print("first command has been executed")

    def do_command2(self, args):
        """Second command"""
        print("Second command has been executed")

    def do_exit(self, args):
        """exit from the interpreter"""
        print("see you")
        return(True)

    if __name__ == '__main__':
        interpreter = Command()
        interpreter.cmdloop()
