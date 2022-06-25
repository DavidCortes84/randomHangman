from unicodedata import name


class W:
    def __init__(self,name):
        self.name = name

    def show_instance_name(self):
        print(self.name)

    @staticmethod
    def show_name(name):
        print(name)

W.show_name("Sheldon")
w = W("Dave")
w.show_instance_name()