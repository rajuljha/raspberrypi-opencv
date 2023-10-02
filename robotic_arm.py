import RPi.GPIO as GPIO
import time

# Define the GPIO pins for the servo motors
servo_pins = [11, 12, 13, 15, 16, 18]

# Initialize the GPIO pins
GPIO.setmode(GPIO.BOARD)
for pin in servo_pins:
    GPIO.setup(pin, GPIO.OUT)

# Define the servo motor objects
servos = [GPIO.PWM(pin, 50) for pin in servo_pins]

# Define the servo motor angles for each degree of freedom
servo_angles = [
    [90, 90, 90, 90, 90, 90],  # Initial position
    [90, 90, 90, 90, 90, 0],   # Rotate base
    [90, 90, 90, 0, 90, 0],    # Raise arm
    [90, 90, 0, 0, 90, 0],     # Lower forearm
    [90, 90, 0, 0, 0, 0],      # Open gripper
    [90, 90, 0, 0, 0, 90],     # Close gripper
    [90, 90, 0, 90, 0, 90],    # Move arm to the side
    [90, 90, 0, 90, 90, 90],   # Move arm to the front
]

# Define the servo motor angles for each degree of freedom for the pickup motion
pickup_angles = [
    servo_angles[0],  # Initial position
    servo_angles[1],  # Rotate base
    servo_angles[2],  # Raise arm
    servo_angles[3],  # Lower forearm
    servo_angles[5],  # Close gripper
    servo_angles[3],  # Raise forearm
    servo_angles[2],  # Lower arm
    servo_angles[0],  # Initial position
]

# Define the function to move the servo motors to the specified angles
def move_servos(angles):
    for i, angle in enumerate(angles):
        servos[i].ChangeDutyCycle(2 + angle / 18)
        time.sleep(0.5)

# Move the robotic arm to the initial position
move_servos(servo_angles[0])

# Wait for user input to start the pickup motion
input("Press Enter to start the pickup motion...")

# Move the robotic arm to the pink dot location and pick up the object
move_servos(pickup_angles)

# Clean up the GPIO pins
for servo in servos:
    servo.stop()
GPIO.cleanup()