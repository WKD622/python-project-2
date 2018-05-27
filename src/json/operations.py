import json
import src.common as c
from json import JSONDecodeError
from pprint import pprint


class JsonOperations:
    """
    This class has his own data field for json and allows to parse json from path, print it at screen or delete.
    """
    data = None

    def parse(self, path):
        """
        Parses json to data field.
        :param path:
        :return:
        """
        self.delete()
        try:
            file = open(path)
            self.data = json.load(file)
        except (FileNotFoundError, IsADirectoryError):
            c.handle_error("Path to json is not correct.")
        except (JSONDecodeError):
            c.handle_error("There are some wrong `types` in json.")
        file.close()

    def print_(self):
        """
        Prints json from data field.
        :return:
        """
        if self.data is not None:
            pprint(self.data)
        else:
            print("You haven't parsed json. First use method parse_json(path) to parse choosen json.")

    def delete(self):
        """
        Clears data field.
        :return:
        """
        self.data = None
