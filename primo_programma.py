import libreria
import time

def main():
    robot = libreria.AlphaBot()

    robot.forward()
    time.sleep(2)
    robot.stop()

    robot.backward()
    time.sleep(2)
    robot.stop()

    robot.left()
    time.sleep(2)
    robot.stop()

    robot.right()
    time.sleep(2)
    robot.stop()

if __name__ == "__main__":
    main()
