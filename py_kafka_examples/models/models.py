

class Car:
    def __init__(self, brand, hp):
        self.__brand = brand
        self.__hp = hp


    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand


    def get_hp(self):
        return self.__hp

    def set_hp(self, hp):
        self.__hp = hp


    def __repr__(self):
        return str(self.__dict__)
