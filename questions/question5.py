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


if __name__ == '__main__':
    print(Version('3.20') > Version("3.11"))
    print(Version('3.1.1') > Version("3.1"))
    print(Version(3.12) > Version(3.9))
    print(Version("0.1.0") == Version(0.1))
