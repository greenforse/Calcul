from abc import ABCMeta, abstractmethod

class State(metaclass=ABCMeta):
  def __init__(self, calculator):
    self.calculator = calculator

  @abstractmethod
  def input_digit(self, digit):
    pass

  @abstractmethod
  def input_operation(self, operator):
    pass

  @abstractmethod
  def input_equals(self):
    pass
