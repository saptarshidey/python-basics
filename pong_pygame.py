import pygame
import random
import os

WIDTH, HEIGHT = 900, 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

PADDLE_VELOCITY = 8
BALL_VELOCITY_X = random.randint(3, 6)
BALL_VELOCITY_Y = random.randint(3, 6)

PADDLE_WIDTH, PADDLE_HEIGHT = 16, 70
BALL_WIDTH = 16

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def move(paddle, ball, keys_pressed):
    # move the ball
    ball.x += BALL_VELOCITY_X
    ball.y += BALL_VELOCITY_Y

    '''if BALL_VELOCITY_X < 0: # moving left
        if ball.left + BALL_VELOCITY_X >= 0: ball.x += BALL_VELOCITY_X

    if BALL_VELOCITY_X > 0: # moving right
        if ball.right + BALL_VELOCITY_X <= WIDTH: ball.x += BALL_VELOCITY_X

    if BALL_VELOCITY_Y < 0: # moving up
        if ball.top + BALL_VELOCITY_Y >= 0: ball.y += BALL_VELOCITY_Y

    if BALL_VELOCITY_Y > 0: # moving down
        if ball.bottom + BALL_VELOCITY_Y <= HEIGHT: ball.y += BALL_VELOCITY_Y'''

    # move the paddle
    if keys_pressed[pygame.K_UP] and paddle.top - PADDLE_VELOCITY >= 0: paddle.y -= PADDLE_VELOCITY
    if keys_pressed[pygame.K_DOWN] and paddle.bottom + PADDLE_VELOCITY <= HEIGHT: paddle.y += PADDLE_VELOCITY

def handle_collision(paddle, ball):
    global BALL_VELOCITY_X
    global BALL_VELOCITY_Y

    if ball.left <= 0 or ball.right >= WIDTH:   # ball touches left or right wall
        BALL_VELOCITY_X *= -1

    if ball.top <= 0 or ball.bottom >= HEIGHT:  # ball touches top or bottom wall
        BALL_VELOCITY_Y*= -1

    if ball.colliderect(paddle):   # ball touches paddle
        BALL_VELOCITY_X *= -1

    if paddle.top <= 0: paddle.top = 0
    if paddle.bottom >= HEIGHT: paddle.bottom = HEIGHT

def draw(paddle, ball):
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.circle(screen, WHITE, (ball.centerx, ball.centery), BALL_WIDTH//2)

def main():
    pygame.display.set_caption("First Game!")
    clock = pygame.time.Clock()

    paddle = pygame.Rect(20, 40, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = pygame.Rect(100, 200, BALL_WIDTH, BALL_WIDTH)

    while True:
        # Process player inputs.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        keys_pressed = pygame.key.get_pressed()
        move(paddle, ball, keys_pressed)
        draw(paddle, ball)
        handle_collision(paddle, ball)

        # Refresh on-screen display
        pygame.display.update()
        clock.tick(FPS)  # wait until next frame (at 60 FPS)


if __name__ == "__main__":
    main()
