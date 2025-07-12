from telloNav import Drone, Directions, Coordinates
from controller import DroneController

def main():
    try:
        print("Press Q for manual control")
        drone.takeoff()
        
    except KeyboardInterrupt:
        drone.emergency()
    finally:
        controller.stop()


if __name__ == "__main__":
    drone = Drone()
    controller = DroneController(drone)
    monitor_thread = controller.start_monitoring()
    main()