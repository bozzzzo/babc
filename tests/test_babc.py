import pytest
from babc import BABC, abstractmethod


def test_simple_concrete_subclass():
    class Base(BABC):
        @abstractmethod
        def findmefindme(self):
            ...

    class Check(Base):
        def findmefindme(self):
            pass

    Check()


def test_simple_abstract_subclass():
    class Base(BABC):
        @abstractmethod
        def findmefindme(self):
            ...

    class Check(Base):
        pass

    with pytest.raises(TypeError, match=".*findmefindme.*"):
        Check()


class Base(BABC):
    @abstractmethod
    def findmefindme(self, a, *b, c, d=42, **f):
        ...


def test_remove_positional_arg():
    with pytest.raises(TypeError, match=".*findmefindme.*"):
        class Check(Base):
            def findmefindme(self, *b, c, d=42, **f):
                ...


def test_correct_subclassing():
    class Check(Base):
        def findmefindme(self, a, *b, c, d=42, **f):
            return a, b, c, d, f

    c = Check()
    expected = (1,(2,3),4,42,{})
    actual = c.findmefindme(1,2,3,c=4)
    assert expected == actual


def test_remove_keyword_arg():
    with pytest.raises(TypeError, match=".*findmefindme.*"):
        class Check(Base):
            def findmefindme(self, a, *b, c, **f):
                ...


def test_remove_named_arg():
    with pytest.raises(TypeError, match=".*findmefindme.*"):
        class Check(Base):
            def findmefindme(self, a, *b, d=42, **f):
                ...


def test_add_positional_arg():
    with pytest.raises(TypeError, match=".*findmefindme.*"):
        class Check(Base):
            def findmefindme(self, a, x, *b, d=42, **f):
                ...


def test_add_keyword_arg():
    with pytest.raises(TypeError, match=".*findmefindme.*"):
        class Check(Base):
            def findmefindme(self, a, *b, c, d=42, x='x', **f):
                ...


def test_change_arg_default():
    with pytest.raises(TypeError, match=".*findmefindme.*"):
        class Check(Base):
            def findmefindme(self, a, *b, c, d=43, **f):
                ...


def test_add_named_arg():
    with pytest.raises(TypeError, match=".*findmefindme.*"):
        class Check(Base):
            def findmefindme(self, a, *b, c, x, d=42, **f):
                ...
