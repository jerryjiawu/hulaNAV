from djitellopy import Tello

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
    def __init__(self):
        self.speed = 100
        self.tello = Tello()

        self.tello.connect()
        self.tello.takeoff()

    def set_speed(self, speed):
        if speed < 10 or speed > 100:
            raise ValueError("Speed must be between 10 and 100.")
        self.speed = speed

    def move(self, direction: Directions, distance: float):
        self.tello.move(direction, distance, self.speed)

    def move_relative(self, coordinates: Coordinates):
        self.tello.go_xyz_speed(coordinates.x, coordinates.y, coordinates.z, self.speed)

    def curve(self, p1: Coordinates, p2: Coordinates):
        self.tello.curve_xyz_speed(p1.x, p1.y, p1.z, p2.x, p2.y, p2.z, self.speed)

    def takeoff(self):
        self.tello.takeoff()

    def land(self):
        self.tello.land()

    def get_speed(self):
        return self.tello.get_speed_x(), self.tello.get_speed_y(), self.tello.get_speed_z()

    def get_height(self):
        return self.tello.get_distance_tof()
    
    def emergency(self):
        self.tello.emergency()

    def rotate(self, angle: float):
        if angle < 1 and angle > -1:
            raise ValueError("Angle must be greater than 1 or less than -1.")
        if angle > 0:
            self.tello.rotate_clockwise(angle)
        else:
            self.tello.rotate_counter_clockwise(-angle)


