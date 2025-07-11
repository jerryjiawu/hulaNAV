import pyhula
from src import Light

class Drone:
    class Directions:
        FORWARD = 1
        BACKWARD = 2
        LEFT = 3
        RIGHT = 4
        UP = 5
        DOWN = 6
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

        self.pitch = 0
        self.roll = 0
        self.yaw = 0
        
        self.light = Light()
        self.api = pyhula.UserApi() 

        if not self.api.connect():
            print("Failed to connect to the drone.") 
        else:
            print('connected to drone!')

    def get_position(self):
        self.x, self.y, self.z = self.api.get_coordinates()
        return self.x, self.y, self.z
    
    def fly_to_coordinates(self, x, y, z, curved=False):
        self.light.set_colour(Light.Colours.GREEN)
        d_x = x - self.x
        d_y = y - self.y
        d_z = z - self.z

        if curved:
            self.api.single_fly_curvilinearFlight(d_x, d_y, d_z, led=self.light.get_dict())
        else:
            self.api.single_fly_straight_flight(d_x, d_y, d_z, led=self.light.get_dict())

        print(f"Flying to coordinates: ({d_x}, {d_y}, {d_z})")

    def fly_relative(self, x, y, z, curved=False):
        self.light.set_colour(Light.Colours.GREEN)
        if curved:
            self.api.single_fly_curvilinearFlight(x, y, z, led=self.light.get_dict())
        else:
            self.api.single_fly_straight_flight(x, y, z, led=self.light.get_dict())

        print(f"Flying to coordinates: ({x}, {y}, {z})")

    def rotate(self, angle):
        self.light.set_colour(Light.Colours.GREEN)
        self.api.single_fly_autogyration360(1 / angle, led=self.light.get_dict())

    def move(self, direction: Directions, distance: float):
        self.light.set_colour(Light.Colours.GREEN)
        if direction == self.Directions.FORWARD:
            self.api.single_fly_straight_flight(distance, 0, 0, led=self.light.get_dict())
        elif direction == self.Directions.BACKWARD:
            self.api.single_fly_straight_flight(-distance, 0, 0, led=self.light.get_dict())
        elif direction == self.Directions.LEFT:
            self.api.single_fly_straight_flight(0, -distance, 0, led=self.light.get_dict())
        elif direction == self.Directions.RIGHT:
            self.api.single_fly_straight_flight(0, distance, 0, led=self.light.get_dict())
        elif direction == self.Directions.UP:
            self.api.single_fly_straight_flight(0, 0, distance, led=self.light.get_dict())
        elif direction == self.Directions.DOWN:
            self.api.single_fly_straight_flight(0, 0, -distance, led=self.light.get_dict())

    def takeoff(self):
        self.light.set_colour(Light.Colours.RED, mode=Light.Modes.BLINK)
        self.api.single_fly_takeoff(led=self.light.get_dict())
        print("Taking off...")

    def land(self):
        self.light.set_colour(Light.Colours.RED, mode=Light.Modes.BLINK)
        self.api.single_fly_touchdown(led=self.light.get_dict())
        print("Landing...")

    

        



