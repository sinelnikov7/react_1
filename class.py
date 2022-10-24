from abc import ABC, abstractmethod

class MyABC(ABC):

    @abstractmethod
    def sayHy(self):
        pass

    @abstractmethod
    def sayBy(self):
        pass

class User(MyABC):
    def sayHy(self):
        pass

    def sayBy(self):
        pass

    def gora(self):
        print("I'm Gora")

user = User()
print(user)