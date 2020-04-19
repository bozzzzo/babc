import abc
import inspect
import logging


class BABCMeta(abc.ABCMeta):
    def __new__(mcls, name, bases, namespace, **kwargs):
        cls = super().__new__(mcls, name, bases, namespace, **kwargs)
        for base in bases:
            for name in getattr(base, "__abstractmethods__", set()):
                value = getattr(cls, name, None)
                if not getattr(value, "__isabstractmethod__", False):
                    is_more_restrictive(getattr(base, name), value)
        return cls


class BABC(abc.ABC, metaclass=BABCMeta):
    __slots__ = ()


def is_more_restrictive(abstract, concrete):
    a = inspect.signature(abstract)
    c = inspect.signature(concrete)
    if a != c:
        raise TypeError("abstractmethod {}{} is overridden as {}{}".format(
            abstract.__name__, a,
            concrete.__name__, c))
