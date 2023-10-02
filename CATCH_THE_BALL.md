# Catch the Ball

This is a simple game where the player tries to catch a ball with a paddle. The ball falls from the top of the screen, and the player moves the paddle left and right to catch the ball. If the player misses the ball, the game ends.

## Requirements

- Python 3.x
- OpenCV

## How to Play

1. Run the `catch_the_ball.py` script.
2. Move the paddle left and right using the 'a' and 'd' keys.
3. Try to catch the falling ball with the paddle.
4. If the ball hits the paddle, it bounces back up. If the ball misses the paddle and hits the ground, the game ends.

## How to Increase Difficulty

To increase the difficulty of the game, you can make the ball move faster, make the paddle smaller, or both. Here are some changes you can make to the code to increase the difficulty:

1. Increase the value of `ballVY` to make the ball fall faster.
2. Increase the value of `ballVX` to make the ball move faster horizontally.
3. Decrease the value of `paddleWidth` to make the paddle smaller.

## Future Tasks and Assignments

- Add functionality so that whenever the ball hits the paddle, the speed increases.
- Also, whenever the ball hits the top of the frame, the paddle becomes smaller by some amount.
- Add a tracker for the current coordinates of the position of the ball. Show it in the top left of the screen.
- How to add sound effects to the game?

**Possibilities are endless and this is just the beginning. Start now and collaborate!!**

## Credits

This code was created with the help of the [OpenCV documentation](https://docs.opencv.org/master/d9/df8/tutorial_root.html).