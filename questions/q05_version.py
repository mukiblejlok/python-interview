"""
Create a class for handling Version numbers.
It has to take number or as string as an input and allow correct comparisons, eg.
3.20 > 3.11
3.1.1 > 3.1
3.12 > 3.9
"""
from numbers import Number
from typing import Union, Sequence
import re


class Version:

    def __init__(self, input_value: Union[Number, str], **kwargs):
        self._input_value = input_value
        self._input_string = str(input_value)
        self.delimiters = kwargs.get("delimiters", (".", "b", ","))
        self.version_tuple = self.decode_input(input_string=self._input_string,
                                               delimiters=self.delimiters)

    @staticmethod
    def decode_input(input_string: str, delimiters: Sequence[str]) -> Sequence[int]:
        _delimiters = " |".join(delimiters)
        elements = re.split(f"[{_delimiters}]", input_string)
        int_elements = [int(e) for e in elements]
        return int_elements

    def __repr__(self):
        return ".".join(str(e) for e in self.version_tuple)

    def __eq__(self, other):
        return self.version_tuple == other

    def __ne__(self, other):
        return self.version_tuple != other

    def __lt__(self, other):
        return self.version_tuple < other

    def __le__(self, other):
        return self.version_tuple <= other

    def __gt__(self, other):
        return self.version_tuple > other

    def __ge__(self, other):
        return self.version_tuple >= other


if __name__ == '__main__':
    print(Version('3.20') > Version("3.11"))
    print(Version('3.1.1') > Version("3.1"))
    print(Version(3.12) > Version(3.9))
    print(Version("0.1.0") == Version(0.1))
