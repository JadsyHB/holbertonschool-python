#!/usr/bin/python3
"""
Model Square that inherits from Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inherits from Rectangle
    Functions: def __init__(self, size, x=0, y=0, id=None)
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initialization
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
        size getter
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        size setter
        """
        self.width = size
        self.height = size

    def __str__(self):
        """
        print string
        """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x, self.y,
            self.size)

    def update(self, *args, **kwargs):
        """
        update using *args
        """
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        else:
            for i in kwargs:
                if i == 'id':
                    self.id = kwargs[i]
                elif i == 'size':
                    self.size = kwargs[i]
                elif i == 'x':
                    self.x = kwargs[i]
                elif i == 'y':
                    self.y = kwargs[i]

    def to_dictionary(self):
        """
        return dictionarry
        """
        dic = {}
        dic['x'] = self.x
        dic['y'] = self.y
        dic['id'] = self.id
        dic['size'] = self.size
        return dic
