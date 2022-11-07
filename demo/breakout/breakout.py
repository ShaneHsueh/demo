"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 50  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts

graphics = BreakoutGraphics()


def main():
    lives = NUM_LIVES
    # Add the animation loop here!
    while True:
        graphics.ball.move(graphics.dx, graphics.dy)
        pause(FRAME_RATE)
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            graphics.dx *= -1
        if graphics.ball.y <= 0:
            graphics.dy *= -1
        if graphics.ball.y >= graphics.window.height:
            lives -= 1
            if lives == 0:
                break
            graphics.reset_ball()
        check_for_collisions(graphics.ball)


def check_for_collisions(event):
    ball_upper_left = graphics.window.get_object_at(event.x, event.y)
    ball_upper_right = graphics.window.get_object_at(event.x+2*graphics.ball_radius, event.y)
    ball_lower_left = graphics.window.get_object_at(event.x, event.y+2*graphics.ball_radius)
    ball_lower_right = graphics.window.get_object_at(event.x+2*graphics.ball_radius, event.y+2*graphics.ball_radius)
    if ball_upper_left is not None and ball_upper_left is not graphics.paddle:
        graphics.dy *= -1
        graphics.window.remove(ball_upper_left)
    elif ball_upper_right is not None and ball_upper_right is not graphics.paddle:
        graphics.dy *= -1
        graphics.window.remove(ball_upper_right)
    elif ball_lower_right is not None and ball_lower_right is not graphics.paddle:
        graphics.dy *= -1
        graphics.window.remove(ball_lower_right)
    elif ball_lower_left is not None and ball_lower_left is not graphics.paddle:
        graphics.dy *= -1
        graphics.window.remove(ball_lower_left)
    elif ball_upper_left or ball_upper_right or ball_lower_left or ball_lower_right is graphics.paddle:
        if graphics.dy>0:
            graphics.dy *= -1


if __name__ == '__main__':
    main()
