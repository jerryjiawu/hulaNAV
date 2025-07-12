from hulaNav.hulaNav import Drone

def main():
    drone = Drone()
    
    # Take off
    drone.takeoff()
    
    # Get current position
    x, y, z = drone.get_position()
    print(f"Current position: ({x}, {y}, {z})")
    
    # Fly to a new position
    drone.fly_to_coordinates(10, 10, 5)
    
    # Rotate the drone
    drone.rotate(90)
    
    # Land the drone
    drone.land()

if __name__ == "__main__":
    main()