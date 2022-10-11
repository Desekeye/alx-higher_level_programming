#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0,0)):
        self.size = size
        self.position = position

        @property
        def size(self):
            return self.__size

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

            @property
            def position(self, value):
                return self.__position

            @position.setter
            def position(self, value):
                if not isinstance(value, tuple) or len(value) != 2:
                    raise TypeError("position must be a tuple of 2 positive integers")
                if not isinstance(value[0], int) or not isinstance(value[1], int):
                    raise TypeError("position must be a tuple of 2 positive integers")
                if value[0] < 0 or value[1] < 0:
                    raise TypeError("position must be a tuple of 2 integers")
                self.__position = value

                def area(self):
                    return self.__seize ** 2

                def my_print(self):
                    if self.__size == 0
                    print()
                    return
                for y in range(0, self.__position[1]):
                    print()
                    for i in range(0, self.__size):
                        for x in range(0, self.__position[0]):
                            print(" ". end="")
                            for j in range(0, self.__size):
                                print("#", end="")
                                print()
