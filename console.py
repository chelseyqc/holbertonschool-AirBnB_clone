#!/usr/bin/python3
"""command interpreter entry point"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ basic commands """

    prompt = '(hbnb) '

    def if_emptyline(self, arg):
        """ If command line is empty"""
        pass

    def do_quit(self, arg):
        """Exits the program"""
        return True

    do_EOF = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
