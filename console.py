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
            class_name = arg_list[0]
            if class_name not in classes.keys():
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
            class_name = arg_list[0]
            instance_id = arg_list[1]
            instance_key = "{}.{}".format(class_name, instance_id)
            all_instances = storage.all()
            if instance_key not in all_instances:
                print("** no instance found **")
            else:
                print(all_instances[instance_key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        arg_list = arg.split(" ")
        if arg == "" or arg is None:
            print("** class name missing **")
        elif arg_list[0] not in classes:
            print("** class doesn't exist **")
        elif (len(arg_list) < 2):
            print("** instance id missing **")
        else:
            class_name = arg_list[0]
            instance_id = arg_list[1]
            instance_key = "{}.{}".format(class_name, instance_id)
            all_instances = storage.all()
            if instance_key in all_instances:
                del all_instances[instance_key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based
        or not on the class name"""
        arg_list = arg.split(" ")
        all_instances = storage.all()
        output = []
        if arg == "" or arg is None:
            print("** class name missing **")
        if len(arg) == 0:
            for instance in all_instances.values():
                output.append(str(instance))
                print(output)
        else:
            if arg_list[0] not in classes:
                print("** class doesn't exist **")
            else:
                for instance_key in all_instances:
                    if arg_list[0] in instance_key:
                        output.append(str(all_instances[instance]))
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
            class_name = arg_list[0]
            instance_id = arg_list[1]
            attribute_name = arg_list[2]
            attribute_value = arg_list[3]
            all_instances = storage.all()
            for instance in all_instances.values():
                if instance.__class__.__name__ == class_name:
                    if instance.id == instance_id:
                        setattr(instance, attribute_name, attribute_value)
                        storage.save()
                        return
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
