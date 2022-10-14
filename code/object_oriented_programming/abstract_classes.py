from enum import Enum
from abc import ABCMeta, abstractmethod


class Gender(Enum):
    MALE = 'male'
    FEMALE = 'female'


class Human(metaclass=ABCMeta):
    """ Base class for all humans """

    def __init__(self, name: str, age: int, height: float, weight: float) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    @abstractmethod
    def walk(self) -> None:
        ...

    @abstractmethod
    def speak(self) -> None:
        ...


class Male(Human):
    """ A male specie of the human race """

    def __init__(self, name: str, age: int, height: float, weight: float) -> None:
        super().__init__(name, age, height, weight)
        self.sex = Gender.MALE


class Female(Human):
    """ A female specie of the human race """

    def __init__(self, name: str, age: int, height: float, weight: float) -> None:
        super().__init__(name, age, height, weight)
        self.sex = Gender.FEMALE

