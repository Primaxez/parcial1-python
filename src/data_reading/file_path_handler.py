import os.path
from datetime import time
from controller.data_handler import DataHandler
from exceptions.incomplete_file_error import IncompleteFileError
from exceptions.not_text_file_error import NotTextFileError

class FileHandler:
    """
    This class handles the validation and reading of files
    """
    def __init__(self, file_dir: str = None, data_handler = DataHandler()):
        if(file_dir):
            self.__file_dir = self.check_file(os.path.abspath(file_dir))
        else:
            self.__file_dir = file_dir
        self.__data_handler = data_handler

    def file_is_binary(self, file_dir) -> bool:
        """
        Returns true if the file is binary
        """
        textchars = bytearray(
            {7, 8, 9, 10, 12, 13, 27} |
            set(range(0x20, 0x100)) - {0x7f}
        )
        def is_binary_string(bytes): return bool(bytes.translate(None, textchars))
        return is_binary_string(open(file_dir, 'rb').read(1024))

    def has_numbers(self, input_str:str) -> bool:
        """
        Returns true if the given str has number(s)
        """
        return any(char.isdigit() for char in input_str)

    def line_is_complete(self, line):
        """
        Returns true if the ammount of columns in the line is correct
        """
        elements = line.replace(' ', '').strip("\n").split(",")
        if(len(elements) != 10):
            return False
        try:
            # Try to convert the elements to check if they have the correct type
            ci = int(elements[0])
            first_surname = str(elements[1])
            second_surname = str(elements[2])
            name = str(elements[3])
            middle_name_initial = str(elements[4])
            sex = str(elements[5])
            age = int(elements[6])
            hours = int(elements[7])
            minutes = int(elements[8])
            seconds = int(elements[9])
            execution_time = time(hours,minutes,seconds)
            if(self.has_numbers(first_surname + second_surname + name + middle_name_initial + sex)):
                return False
            elif(len(middle_name_initial + sex) != 2):
                return False
            elif(sex not in ["M", "F"]):
                return False
            else:
                self.add_data_line([ci, first_surname, second_surname, name, middle_name_initial, sex, age, execution_time])
                return True
        except ValueError:
            return False

    def file_is_complete(self, file_dir) -> bool:
        """
        Returns true if the ammount of columns of the file is correct
        """
        with open(file_dir, "r") as f:
            lines = f.readlines()
        for line in lines:
            if(not self.line_is_complete(line)):
                return False
        return True

    def check_file(self, file_dir) -> str:
        """
        Returns the file path if it is a text file
        """
        if(not os.path.isfile(file_dir)):
            raise FileNotFoundError(f"¡Error: el archivo '{file_dir}' no existe!")
        elif(self.file_is_binary(file_dir)):
            raise NotTextFileError(file_dir)
        elif(not self.file_is_complete(file_dir)):
            raise IncompleteFileError(file_dir)
        else:
            return file_dir
    
    @property
    def file_dir(self):
        return self.__file_dir

    @file_dir.setter
    def file_dir(self, file_dir):
        self.__file_dir = self.check_file(os.path.abspath(file_dir))

    @property
    def data_handler(self):
        return self.__data_handler

    @data_handler.setter
    def data_handler(self, data_handler):
        self.__data_handler = data_handler

    def add_data_line(self, data_line):
        """
        Add line of data to the data_handler
        """
        self.__data_handler.add_contest_line(data_line)