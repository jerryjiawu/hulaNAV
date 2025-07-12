from djitellopy import Tello
from datetime import datetime
import colorama
colorama.init(autoreset=True)

class Directions:
        FORWARD = "forward"
        BACKWARD = "backward"
        LEFT = "left"
        RIGHT = "right"
        UP = "up"
        DOWN = "down"

class Coordinates:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Coordinates(x={self.x}, y={self.y}, z={self.z})"        

class Drone:
    @staticmethod
    def print(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(colorama.Fore.GREEN + f"[{timestamp}]", *args, **kwargs)

    def __init__(self):
        self.speed = 100
        self.tello = Tello()

        Drone.print("Drone initialized")
        self.tello.connect()

        self.tello.takeoff()

    def set_speed(self, speed):
        if speed < 10 or speed > 100:
            raise ValueError("Speed must be between 10 and 100.")
        self.speed = speed

    def move(self, direction: Directions, distance: float):
        self.tello.move(direction, distance, self.speed)
        Drone.print(f"Moved {direction} by {distance} cm at speed {self.speed}")

    def move_relative(self, coordinates: Coordinates):
        self.tello.go_xyz_speed(coordinates.x, coordinates.y, coordinates.z, self.speed)
        Drone.print(f"Moved to coordinates: {coordinates}")

    def curve(self, p1: Coordinates, p2: Coordinates):
        self.tello.curve_xyz_speed(p1.x, p1.y, p1.z, p2.x, p2.y, p2.z, self.speed)
        Drone.print(f"Curved to coordinates: {p1} -> {p2}")

    def takeoff(self):
        Drone.print("Drone taking off")
        self.tello.takeoff()

    def land(self):
        Drone.print("Drone landing")
        self.tello.land()
    def get_speed(self):
        return self.tello.get_speed_x(), self.tello.get_speed_y(), self.tello.get_speed_z()

    def get_height(self):
        return self.tello.get_distance_tof()
    
    def emergency(self):
        Drone.print("Emergency stop initiated")
        self.tello.emergency()

    def rotate(self, angle: float):
        Drone.print(f"Rotating drone by {angle} degrees")
        if angle < 1 and angle > -1:
            raise ValueError("Angle must be greater than 1 or less than -1.")
        if angle > 0:
            self.tello.rotate_clockwise(angle)
        else:
            self.tello.rotate_counter_clockwise(-angle)


