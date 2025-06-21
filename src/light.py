class Light:
    class Modes:
        STEADY = 1
        OFF = 2
        RGB_CYCLE = 4
        RAINBOW = 16
        BLINK = 32
        BREATHING = 64

    class Colours:
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 255)
        YELLOW = (255, 255, 0)
        CYAN = (0, 255, 255)
        MAGENTA = (255, 0, 255)
        WHITE = (255, 255, 255)

    def __init__(self, colour=Colours.GREEN):
        self.colour = colour

    def set_colour(self, r:int, g:int, b:int, mode=1):
        self.colour['r'] = r
        self.colour['g'] = g
        self.colour['b'] = b
        self.colour['mode'] = mode

        pyhula.UserApi().set_light(self.colour)
        print(f"Light set to colour: {self.colour}")

    def set_mode(self, mode: 'Light.Modes'):
        self.colour['mode'] = mode
        pyhula.UserApi().set_light(self.colour)
        print(f"Light mode set to: {mode}")

    def get_dict(self):
        return self.colour
