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

        arg_list = arg.split()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] != "BaseModel":
            print("** class doesn't exist **")
        elif (len(arg_list) < 2):
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arg_list[0], arg_list[1])
            class_dict = storage.all()
            if key not in class_dict:
                print("** no instance found **")
            else:
                print(class_dict[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        arg_list = arg.split()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] != "BaseModel":
            print("** class doesn't exist **")
        elif (len(arg_list) < 2):
            print("** instance id missing **")
        else:
            this_key = "{}.{}".format(arg_list[0], arg_list[1])
            class_dict = storage.all()
            if this_key in class_dict:
                class_dict.remove(this_key)
            else:
                print("** no instance found **")
"""
    def do_all(self, arg):
        # Prints all string representation of all instances based
        # or not on the class name
        arg_list = arg.split(" ")
        class_dict = storage.all()
        new_list = []
        if len(arg) == 0:
            for value
            """

if __name__ == '__main__':
    HBNBCommand().cmdloop()
