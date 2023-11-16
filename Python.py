class Turtle(object):

    def __init__(self, x = 0, y = 0, s = 1):
        self.__x = x
        self.__y = y
        self.__s = s    

    def go_up(self):
        self.__y += self.__s

    def go_down(self):
        self.__y -= self.__s
    
    def go_left(self):
        self.__x -= self.__s
    
    def go_right(self):
        self.__x += self.__s

    def evolve(self):
        self.__s += 1

    def degraade(self):
        if self.__s >= 1:
            self.__s -= 1
        else:
            raise Exception()
        
    def count_moves(self, x2, y2):
        count = 0

        count_x = x2 - self.__x
        count_y = y2 - self.__y
        if count_x % self.__s == 0:
            count += abs((count_x) // self.__s)
        else:
            count += abs((count_x) // self.__s)
            count += 1

        if count_y % self.__s == 0:
            count += abs((count_y) // self.__s)
        else:
            count += abs((count_y) // self.__s)
            count += 1

        return count