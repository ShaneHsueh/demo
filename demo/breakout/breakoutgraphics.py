"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle_width = paddle_width
        self.paddle_offset = paddle_offset
        self.paddle = GRect(paddle_width, paddle_height, x=(self.window_width-paddle_width)/2,
                            y=self.window_height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius, ball_radius, x=(self.window_width-ball_radius)/2,
                          y=(self.window_height-ball_radius)/2)
        self.ball_radius = ball_radius
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.dx = 0
        self.dy = 0

        # Initialize our mouse listeners
        onmousemoved(self.move_paddle)
        onmouseclicked(self.ball_speed)

        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols//5):
                self.brick = GRect(brick_width, brick_height, x=i*(brick_width+brick_spacing),
                                   y=brick_offset + j*(brick_height+brick_spacing))
                self.brick.filled = True
                self.brick.fill_color = 'red'
                self.window.add(self.brick)

        for i in range(brick_rows):
            for j in range(brick_cols//5):
                self.brick = GRect(brick_width, brick_height, x=i*(brick_width+brick_spacing),
                                   y=brick_offset + brick_cols//5*(brick_height+brick_spacing)
                                   + j*(brick_height+brick_spacing))
                self.brick.filled = True
                self.brick.fill_color = 'orange'
                self.window.add(self.brick)

        for i in range(brick_rows):
            for j in range(brick_cols//5):
                self.brick = GRect(brick_width, brick_height, x=i*(brick_width+brick_spacing),
                                   y=brick_offset + brick_cols//5*(brick_height+brick_spacing)*2
                                   + j*(brick_height+brick_spacing))
                self.brick.filled = True
                self.brick.fill_color = 'yellow'
                self.window.add(self.brick)

        for i in range(brick_rows):
            for j in range(brick_cols//5):
                self.brick = GRect(brick_width, brick_height, x=i*(brick_width+brick_spacing),
                                   y=brick_offset + brick_cols//5*(brick_height+brick_spacing)*3
                                   + j*(brick_height+brick_spacing))
                self.brick.filled = True
                self.brick.fill_color = 'green'
                self.window.add(self.brick)

        for i in range(brick_rows):
            for j in range(brick_cols//5):
                self.brick = GRect(brick_width, brick_height, x=i*(brick_width+brick_spacing),
                                   y=brick_offset + brick_cols//5*(brick_height+brick_spacing)*4
                                   + j*(brick_height+brick_spacing))
                self.brick.filled = True
                self.brick.fill_color = 'blue'
                self.window.add(self.brick)

    def move_paddle(self, mouse):
        if mouse.x < self.paddle_width/2:
            self.window.add(self.paddle, x=0, y=self.window_height - self.paddle_offset)
        elif mouse.x > self.window.width-self.paddle_width/2:
            self.window.add(self.paddle, x=self.window.width-self.paddle_width,
                            y=self.window_height - self.paddle_offset)
        else:
            self.window.add(self.paddle, x=mouse.x-self.paddle_width/2, y=self.window_height-self.paddle_offset)

    def ball_speed(self, mouse):
        if self.dx == 0 and self.dy == 0:
            self.dx = random.randint(1, MAX_X_SPEED)
            self.dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.dx *= -1

    def reset_ball(self):
        self.ball.x = (self.window_width - self.ball_radius)/2
        self.ball.y = (self.window_height - self.ball_radius)/2
        self.dx = 0
        self.dy = 0
