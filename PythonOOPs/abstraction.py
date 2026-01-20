from abc import ABC , abstractmethod
class demo(ABC):
        @abstractmethod
        def method1(self):
            print("abstract method")
            return
        def method2(self):
            print ("concrete method")

class concreteclass(demo):
     def method1(self):
          super().method1()
          return
     
obj = concreteclass()
obj.method1()
obj.method2()