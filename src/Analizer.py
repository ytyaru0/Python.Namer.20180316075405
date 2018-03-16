from abc import ABCMeta, abstractmethod
class Analizer(metaclass=ABCMeta):
    @abstractmethod
    def TargetIs(self): pass
    @abstractmethod
    def RuleIs(self): pass
    @abstractmethod
    def Split(self): pass
    @abstractmethod
    def To(self, words): pass
