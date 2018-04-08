import paho.mqtt.client as mqtt


def loop_control(loop_function):
    def handler(self):
        loop_function(self)
        self.done = True
        self.reset_devices()
    return handler


def reset_control(reset_function):
    def handler(self):
        reset_function(self)
        self.done = False
    return handler


class Device(object):
    device_dict = dict()

    @classmethod
    def reset_devices(cls):
        for name, device in cls.device_dict.items():
            if not device.done:
                return
        for name, device in cls.device_dict.items():
            device.reset()

    @classmethod
    def get_device(cls, name):
        if name in cls.device_dict:
            return cls.device_dict[name]
        else:
            Device(name)
            return cls.get_device(name)

    def __init__(self, name, ip="127.0.0.1", port=1883):
        self.client_id = name
        self.done = False
        self.mqClient = mqtt.Client(client_id=self.client_id)
        self.mqClient.connect_async("127.0.0.1", 1883, 60)
        self.device_dict[name] = self
        self.setup()

    def setup(self):
        # Runs one time at initialization
        pass

    @loop_control
    def loop(self):
        # Runs one time per frame
        print("Device Loop")
        pass

    @reset_control
    def reset(self):
        # Runs one time per frame after logic is applied
        pass
