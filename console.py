#!/usr/bin/python3
"""command interpreter entry point"""
import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """basic commands """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exits the program"""
        return True

    def emptyline(self):
        """If command line is empty"""
        pass

    do_EOF = do_quit

    def do_create(self, arg):
        """Creates a new instance of BaseModel & saves to json"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            instance = BaseModel()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
