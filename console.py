#!/usr/bin/python3
"""
that contains the entry point of the command interpreter
"""
import cmd
import json
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    class definition
    """
    prompt = "(hbnb) "

    __classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Amenity",
            "Place",
            "Review"
            }

    def default(self, line):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", line)
        if match is not None:
            argl = [line[:match.span()[0]], line[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(line))
        return False

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it
        (to the JSON file)
        """
        arg = line.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        kwargs = {}
        args = arg[1:]
        for param in args:
            parts = param.split("=")
            if len(parts) != 2:
                continue
            key = parts[0]
            value = parts[1]
            if value.startswith('"'):
                value = value[1:-1].replace('_', ' ').replace('\\"', '"')
            elif '.' in value:
                try:
                    value = float(value)
                except ValueError:
                    continue
            else:
                try:
                    value = int(value)
                except ValueError:
                    continue
            kwargs[key] = value
        else:
            print(eval(arg[0])().id)
            storage.save()

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        arg = line.split()
        obj_dict = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in obj_dict:
            print("** instance id missing **")
        else:
            print(obj_dict["{}.{}".format(arg[0], arg[1])])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        arg = line.split()
        obj_dict = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif arg[1] == 0:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in obj_dict:
            print("** no instance found **")
        else:
            obj_dict = "{}.{}".format(arg[0], arg[1])
            del obj_dict
            storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        arg = line.split()
        dict_str = []
        obj_dict1 = storage.all()
        if arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 0:
            dict_str1 = [str(obj) for obj in obj_dict1.values()]
            print(dict_str1)
        else:
            if arg[0] in HBNBCommand.__classes:
                for key, values in obj_dict1.items():
                    if arg[0] in key:
                        dict_str.append(str(values))
                print(dict_str)

    def do_count(self, line):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class.
        """
        arg = line.split()
        if len(line) == 0:
            print("** class name missing **")
        else:
            if args[0] not in self.__class:
                print("** class doesn't exist **")
            else:
                obj_dict3 = storage.all()
                cunt = 0
                for key in obj_dict3.keys():
                    if line in key:
                        cunt += 1
                print(cunt)

    def do_update(self, line):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary.
        """
        arg = line.split()
        obj_dict = storage.all()

        if len(arg) == 0:
            print("** class name missing **")
            return False
        if arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arg) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg[0], arg[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(arg) == 2:
            print("** attribute name missing **")
            return False
        if len(arg) == 3:
            try:
                type(eval(arg[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arg) == 4:
            obj = obj_dict["{}.{}".format(arg[0], arg[1])]
            if arg[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[arg[2]])
                obj.__dict__[arg[2]] = valtype(arg[3])
            else:
                obj.__dict__[arg[2]] = arg[3]
        elif type(eval(arg[2])) == dict:
            obj = obj_dict["{}.{}".format(arg[0], arg[1])]
            for key, values in eval(arg[2]).items():
                if (key in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[key])
                        in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = valtype(values)
                else:
                    obj.__dict__[key] = values
        storage.save()

    def emptyline(self):
        """
        Do nothing upon recieving an empty command
        """
        pass

    def do_quit(self, line):
        """
        An instance to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        to exit the program
        """
        print("")
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
