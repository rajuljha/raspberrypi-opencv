import numpy as np
import cv2

# Initialize the video capture
cap = cv2.VideoCapture(0)

# Set the display width and height
dispW = 1280
dispH = 720
cap.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)

# Create a window
cv2.namedWindow('Catch the Ball')

# Initialize the paddle position and size
paddleWidth = 100
paddleHeight = 20
paddleX = dispW // 2 - paddleWidth // 2
paddleY = dispH - paddleHeight - 10
paddleSpeed = 10

# Initialize the ball position, size, and velocity
ballRadius = 20
ballX = np.random.randint(ballRadius, dispW - ballRadius)
ballY = 0
ballVX = np.random.randint(-5, 5)
ballVY = 5

# Define the colors
whiteColor = (255, 255, 255)
blueColor = (255, 0, 0)
pinkColor = (180, 105, 255)
font = cv2.FONT_HERSHEY_SIMPLEX
height = 1
weight = 2

# Create a loop that reads frames from the video stream
while True:
    # Read a frame from the video stream
    ret, frame = cap.read()
    if not ret:
        break
    
    # Flip the frame vertically
    frame = cv2.flip(frame, 1)
    
    # Draw the paddle on the frame
    cv2.rectangle(frame, (paddleX, paddleY), (paddleX + paddleWidth, paddleY + paddleHeight), whiteColor, -1)
    
    # Draw the ball on the frame
    cv2.circle(frame, (ballX, ballY), ballRadius, blueColor, -1)
    
    # Update the ball position based on its velocity
    ballX += ballVX
    ballY += ballVY
    
    # Check if the ball hits the paddle or the ground
    if ballY + ballRadius >= paddleY and ballX >= paddleX and ballX <= paddleX + paddleWidth:
        ballVY = -ballVY
        ballVX = np.random.randint(-5, 5)
    elif ballY + ballRadius >= dispH:
        break
    
    # Check if the ball hits the left or right wall
    if ballX - ballRadius <= 0 or ballX + ballRadius >= dispW:
        ballVX = -ballVX
    
    # Check if the ball hits the top wall
    if ballY - ballRadius <= 0:
        ballY = ballRadius
        ballVY = -ballVY
    
    # Check for key presses
    key = cv2.waitKey(1)
    if key == ord('q') or key == 27:
        break
    elif key == ord('a'):
        paddleX -= paddleSpeed
    elif key == ord('d'):
        paddleX += paddleSpeed
    
    # Display the frame
    cv2.imshow('Catch the Ball', frame)

# Release the video capture and destroy the window
cap.release()
cv2.destroyAllWindows()


'''
HOW CAN WE INCREASE THE DIFFICULTY OF THE GAME?
- Make the ball faster
- Make the paddle smaller
- Make both of them happen at the same time.


############## FUTURE TASKS AND ASSiGNMENTS ################
- Add functionality so that whenever the ball hits the paddle, the speed increases
- Also, whenever the ball hits the top of the frame, the paddle becomes smaller by some amount.
- Also, add the tracker for the current coordinates of the position of the ball. Show it in the top left of the screen.
- How to add sound effects to the game?

**Possibilities are endless and this is just the beginning. Start now and collaborate!!**
'''