from telloNav import Drone, Directions
import threading
import time
import sys

class DroneController:
    def __init__(self, drone):
        self.drone = drone
        self.control_active = False
        self.running = True
        self.move_distance = 2

    def get_key(self):
        if sys.platform == 'win32':
            import msvcrt
            if msvcrt.kbhit():
                return msvcrt.getch().decode('utf-8').lower()
        else:
            import select, tty, termios
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                if select.select([sys.stdin], [], [], 0.1) == ([sys.stdin], [], []):
                    return sys.stdin.read(1).lower()
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return None

    def emergency_monitor(self):
        while self.control_active and self.running:
            if self.drone.get_height() < 5:
                print("EMERGENCY: Height too low!")
                self.drone.emergency()
                self.control_active = False
                break
            time.sleep(0.1)

    def keyboard_control(self):
        self.control_active = True
        emergency_thread = threading.Thread(target=self.emergency_monitor, daemon=True)
        emergency_thread.start()
        
        print("WASD: move, QE: rotate, RF: up/down, SPACE: emergency, X: exit")
        
        while self.control_active and self.running:
            key = self.get_key()
            if key is None:
                continue
                
            if key == 'w':
                self.drone.move(Directions.FORWARD, self.move_distance)
            elif key == 's':
                self.drone.move(Directions.BACKWARD, self.move_distance)
            elif key == 'a':
                self.drone.move(Directions.LEFT, self.move_distance)
            elif key == 'd':
                self.drone.move(Directions.RIGHT, self.move_distance)
            elif key == 'r':
                self.drone.move(Directions.UP, self.move_distance)
            elif key == 'f':
                self.drone.move(Directions.DOWN, self.move_distance)
            elif key == 'q':
                self.drone.rotate(-5)
            elif key == 'e':
                self.drone.rotate(5)
            elif key == ' ':
                self.drone.emergency()
                self.control_active = False
            elif key == 'x':
                self.control_active = False

    def monitor_q_key(self):
        while self.running:
            key = self.get_key()
            if key == 'q' and not self.control_active:
                self.keyboard_control()
            time.sleep(0.1)

    def start_monitoring(self):
        monitor_thread = threading.Thread(target=self.monitor_q_key, daemon=True)
        monitor_thread.start()
        return monitor_thread

    def stop(self):
        self.running = False
        self.control_active = False
