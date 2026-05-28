from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def execute(self):
        pass


class TurnOnCommand(Command):

    def __init__(self, light):
        self.light = light

    def execute(self):
        return self.light.turn_on()


class TurnOffCommand(Command):

    def __init__(self, light):
        self.light = light

    def execute(self):
        return self.light.turn_off()