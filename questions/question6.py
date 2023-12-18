"""
We are using an external Key-Value storage (MSTore) that has a very high performance,
but has limitations in terms what can be stored:
 - Keys have to be alphanumeric strings only, plus "_" character. They have to start with a letter.
 - Values have to ASCII strings only.

However, the business requirement is to use it as a storage for values that can be:
integers, floats, booleans or strings with any possible unicode character.
Luckily keys would always be a single word strings with ASCII-only characters

The goal is to implement .get() and .set() methods in a StorageClient class
that will allow to use the MSTore internally but support the requirements from business.

"""
import base64
from collections.abc import MutableMapping
from typing import Union, Any
import re

AcceptedValueTypes = Union[int, float, str, bool]


class MSTore(MutableMapping):
    """
    This is an external class, that cannot be modified.
    It is here only to understand its implementation and test the StorageClient.
    """

    def __init__(self):
        self._internal_storage = {}

    @staticmethod
    def validate_key(key: Any) -> None:
        # Must be a string ...
        if not isinstance(key, str):
            raise KeyError("Key has to be string")
        # ... matching the specified requirements
        pattern = r"^[A-Za-z]\w*$"
        if not re.match(pattern, key):
            raise KeyError(f"Key has to to match regex pattern: {pattern}")

    @staticmethod
    def validate_value(value: Any) -> None:
        # Must be a string ...
        if not isinstance(value, str):
            raise ValueError("Value has to be string")
        # ... with ascii only characters
        if not value.isascii():
            raise ValueError("Value has to contain ascii only characters")

    def __setitem__(self, k, v) -> None:
        self.validate_key(k)
        self.validate_value(v)
        self._internal_storage[k] = v

    def __delitem__(self, k) -> None:
        del self._internal_storage[k]

    def __getitem__(self, k) -> str:
        self.validate_key(k)
        return self._internal_storage[k]

    def __len__(self) -> int:
        return len(self._internal_storage)

    def __iter__(self):
        return iter(self._internal_storage)


class StorageClient:
    """
    Client that uses MSTore as an internal storage, but it supports following types of input values:
    """

    _accepted_types = (str, bool, float, int)
    _encoding = "utf-8"

    def __init__(self, storage_engine: MSTore = None):
        """

        :param storage_engine: it can be initialized with already existing storage,
         otherwise a new empty one will be used.
        """
        self.storage = storage_engine if storage_engine else MSTore()

    def get(self, key: str, default: Any = None) -> Any:
        """
        This method allows to get the value from the internal MSTore based on provided key.
        It also supports the default value parameter. If not provided, the default is None.
        :param key: Key as a string
        :param default: Optional Default value to be returned if key was not found.
        :return: Value stored under the 'key' in it's original type.
        """

        # TODO update naive implementation that won't work for all cases
        if key in self.storage:
            return self.storage[key]

    def set(self, key: str, value: Any) -> None:
        """
        This method allows to set the value in the internal MSTore under the provided key.
        It preserves the type of provided value, if it is one of the values in _accepted_types.
        Otherwise, it raises an error.
        :param key: Key as a string
        :param value: Value as a string, boolean, float or int.
        :return:
        """
        # TODO update naive implementation that won't work for all cases
        self.storage[key] = value


if __name__ == '__main__':
    sc = StorageClient()

    # For simple stuff it works out of the box
    sc.set("SimpleString", "Mama")
    print(sc.get("SimpleString"))

    # But not for those examples
    sc.set("abbCapitalizationUSD", 13231412)
    sc.set("lengthOfMyArm", 3.332)
    sc.set("PolishAddress", "ul. żółta łódź!")
    sc.set("isEverythingOK", False)

    print(sc.get("abbCapitalizationUSD"))
    print(sc.get("lengthOfMyArm"))
    print(sc.get("PolishAddress"))
    print(sc.get("isEverythingOK"))
    print(sc.get("ThisKeyDoesNotExist"))
    print(sc.get("ThisKeyDoesNotExistButItHasADefault", default=1))

    sc.set("nonSupportedType", [1, 2, 3])
