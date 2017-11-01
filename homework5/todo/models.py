# -*- coding: utf-8 -*-


class Storage(object):  # storage = Storge()
    """
    Singleton storage.

    Read more about singleton design pattern:
    https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
    https://en.wikipedia.org/wiki/Singleton_pattern

    It is used to emulate in-memory storage.
    It should be replaced with a database in a real application.
    """

    obj = None

    items = None

    @classmethod
    def __new__(cls, *args):
        if cls.obj is None:
            cls.obj = object.__new__(cls)
            cls.items = []
        return cls.obj


class BaseItem(object):
    def __init__(self, heading):
        self.heading = heading
        self.done = False  # TODO: make sure we can use it...

    def __repr__(self):
        return self.__class__

    @classmethod
    def construct(cls):
        raise NotImplemented()


class ToDoItem(BaseItem):
    def __str__(self):
<<<<<<< HEAD
        if self.done:
            done = '+'
        else:
            done = '-'
        return '{} ToDo: {}'.format(done, self.heading)
=======
        return 'ToDo: {}'.format(self.heading)
>>>>>>> upstream/master

    @classmethod
    def construct(cls):
        heading = input('Input heading: ')
        return cls(heading)


class ToBuyItem(BaseItem):
    def __init__(self, heading, price):
        super().__init__(heading)
        self.price = price

    def __str__(self):
<<<<<<< HEAD
        if self.done:
            done = '+'
        else:
            done = '-'
        return '{} ToBuy: {} for {}'.format(
            done,
=======
        return 'ToBuy: {} for {}'.format(
>>>>>>> upstream/master
            self.heading,
            self.price,
        )

    @classmethod
    def construct(cls):
        heading = input('Input heading: ')
        price = input('Input price: ')
        return cls(heading, price)
<<<<<<< HEAD


class ToReadItem(BaseItem):
    def __init__(self, heading, url):
        super().__init__(heading)
        self.url = url

    def __str__(self):
        if self.done:
            done = '+'
        else:
            done = '-'
        return '{} ToRead: {} {}'.format(
            done,
            self.heading,
            self.url,
        )

    @classmethod
    def construct(cls):
        heading = input('Input heading: ')
        url = input('Input url: ')
        return cls(heading, url)
=======
>>>>>>> upstream/master
