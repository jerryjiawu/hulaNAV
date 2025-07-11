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

    def __init__(self, colour=None):
        if colour is None:
            colour = self.Colours.GREEN
        self.colour = {
            'r': colour[0],
            'g': colour[1], 
            'b': colour[2],
            'mode': self.Modes.STEADY
        }

    def set_colour(self, colour_tuple=None, r=None, g=None, b=None, mode=None):
        if colour_tuple is not None:
            self.colour['r'] = colour_tuple[0]
            self.colour['g'] = colour_tuple[1]
            self.colour['b'] = colour_tuple[2]
        elif r is not None and g is not None and b is not None:
            self.colour['r'] = r
            self.colour['g'] = g
            self.colour['b'] = b
        
        if mode is not None:
            self.colour['mode'] = mode

        print(f"Light set to colour: {self.colour}")

    def set_mode(self, mode):
        self.colour['mode'] = mode
        print(f"Light mode set to: {mode}")

    def get_dict(self):
        return self.colour
