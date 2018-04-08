from .Device import Device


class Button(Device):
    def __init__(self, name):
        super().__init__(name)

    def loop(self):
        super().loop()
        print("buttonloop")
