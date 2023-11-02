#!/usr/bin/python3
"""command interpreter entry point"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


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
        arg_list = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
        else:
            if arg_list[0] not in classes.keys():
                print("** class doesn't exist **")
            else:
                instance = classes[arg_list[0]]()
                instance.save()
                print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""

        arg_list = arg.split(" ")
        if arg == "" or arg is None:
            print("** class name missing **")
        elif arg_list[0] not in classes:
            print("** class doesn't exist **")
        elif (len(arg_list) < 2):
            print("** instance id missing **")
        else:
            command = "{}.{}".format(arg_list[0], arg_list[1])
            current_dict = storage.all()
            if command not in current_dict:
                print("** no instance found **")
            else:
                print(current_dict[command])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        arg_list = arg.split(" ")
        current_dict = storage.all()
        if arg == "" or arg is None:
            print("** class name missing **")
        elif arg_list[0] not in classes:
            print("** class doesn't exist **")
        elif (len(arg_list) < 2):
            print("** instance id missing **")
        else:
            instance = "{}.{}".format(arg_list[0], arg_list[1])
            current_dict = storage.all()
            if instance in current_dict:
                del current_dict[instance]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based
        or not on the class name"""
        arg_list = arg.split(" ")
        current_dict = storage.all()
        output = []
        if arg == "" or arg is None:
            print("** class name missing **")
        if len(arg) == 0:
            for instance in current_dict.values():
                output.append(str(instance))
                print(output)
        else:
            if arg_list[0] not in classes:
                print("** class doesn't exist **")
            else:
                for instance in current_dict:
                    if arg_list[0] in instance:
                        output.append(str(current_dict[instance]))
                    print(output)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute"""
        arg_list = arg.split(" ")
        current_dict = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg_list[0] not in classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif len(arg_list) == 2:
            print("** attribute name missing **")
        elif len(arg_list) == 3:
            print("** value missing **")
        else:
            update_id = arg_list[1]
            for instance in current_dict.values():
                if instance.__class__.__name__ == arg_list[0]:
                    if instance.id == update_id:
                        setattr(instance, arg_list[2], arg_list[3])
                        storage.save()
                        return
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
