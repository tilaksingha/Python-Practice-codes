import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions and settings
WIDTH, HEIGHT = 608, 672
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman")

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PINK = (255, 105, 180)

# Font settings
font = pygame.font.Font(None, 36)

# Maze design
maze = [
    "############################",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#*####.#####.##.#####.####*#",
    "#.####.#####.##.#####.####.#",
    "#..........................#",
    "#.####.##.########.##.####.#",
    "#.####.##.########.##.####.#",
    "#......##....##....##......#",
    "######.##### ## #####.######",
    "######.##### ## #####.######",
    "######.##          ##.######",
    "######.## ###--### ##.######",
    "######.## #      # ##.######",
    "          #      #          ",
    "######.## #      # ##.######",
    "######.## ######## ##.######",
    "######.##          ##.######",
    "######.## ######## ##.######",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#.####.#####.##.#####.####.#",
    "#*..##................##..*#",
    "###.##.##.########.##.##.###",
    "###.##.##.########.##.##.###",
    "#......##....##....##......#",
    "#.##########.##.##########.#",
    "#.##########.##.##########.#",
    "#..........................#",
    "############################"
]

# Pacman settings
pacman_x, pacman_y = 14, 23
pacman_dir = "STOP"
score = 0
lives = 3

# Ghost settings
ghosts = [
    {"x": 13, "y": 11, "dir": random.choice(["UP", "DOWN", "LEFT", "RIGHT"]), "color": RED, "speed": 2},
    {"x": 14, "y": 11, "dir": random.choice(["UP", "DOWN", "LEFT", "RIGHT"]), "color": BLUE, "speed": 2},
    {"x": 13, "y": 13, "dir": random.choice(["UP", "DOWN", "LEFT", "RIGHT"]), "color": PINK, "speed": 2},
    {"x": 14, "y": 13, "dir": random.choice(["UP", "DOWN", "LEFT", "RIGHT"]), "color": WHITE, "speed": 2},
]

def move_pacman(x, y, direction):
    if direction == "UP":
        y -= 1
    elif direction == "DOWN":
        y += 1
    elif direction == "LEFT":
        x -= 1
    elif direction == "RIGHT":
        x += 1
    return x, y

def move_ghost(x, y, direction):
    if direction == "UP":
        y -= 1
    elif direction == "DOWN":
        y += 1
    elif direction == "LEFT":
        x -= 1
    elif direction == "RIGHT":
        x += 1

    if maze[y][x] == "#":
        direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])

    return x, y, direction

def draw_maze():
    for y, row in enumerate(maze):
        for x, tile in enumerate(row):
            if tile == "#":
                pygame.draw.rect(screen, BLUE, (x * 24, y * 24, 24, 24))
            elif tile == ".":
                pygame.draw.circle(screen, WHITE, (x * 24 + 12, y * 24 + 12), 4)
            elif tile == "*":
                pygame.draw.circle(screen, WHITE, (x * 24 + 12, y * 24 + 12), 8)

def game_loop():
    global pacman_x, pacman_y, pacman_dir, score, lives

    running = True
    game_over = False

    while running:
        screen.fill(BLACK)
        draw_maze()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and game_over:
                    pacman_x, pacman_y = 14, 23
                    pacman_dir = "STOP"
                    score = 0
                    lives = 3
                    game_over = False
                elif not game_over:
                    if event.key == pygame.K_LEFT:
                        pacman_dir = "LEFT"
                    if event.key == pygame.K_RIGHT:
                        pacman_dir = "RIGHT"
                    if event.key == pygame.K_UP:
                        pacman_dir = "UP"
                    if event.key == pygame.K_DOWN:
                        pacman_dir = "DOWN"

        if not game_over:
            next_x, next_y = move_pacman(pacman_x, pacman_y, pacman_dir)
            if maze[next_y][next_x] != "#":
                pacman_x, pacman_y = next_x, next_y

            if maze[pacman_y][pacman_x] == ".":
                maze[pacman_y] = maze[pacman_y][:pacman_x] + " " + maze[pacman_y][pacman_x + 1:]
                score += 10
            elif maze[pacman_y][pacman_x] == "*":
                maze[pacman_y] = maze[pacman_y][:pacman_x] + " " + maze[pacman_y][pacman_x + 1:]
                score += 50

            pygame.draw.circle(screen, YELLOW, (pacman_x * 24 + 12, pacman_y * 24 + 12), 12)

            for ghost in ghosts:
                ghost['x'], ghost['y'], ghost['dir'] = move_ghost(ghost['x'], ghost['y'], ghost['dir'])
                pygame.draw.circle(screen, ghost['color'], (ghost['x'] * 24 + 12, ghost['y'] * 24 + 12), 12)

                if ghost['x'] == pacman_x and ghost['y'] == pacman_y:
                    lives -= 1
                    if lives == 0:
                        game_over = True
                    else:
                        pacman_x, pacman_y = 14, 23

            score_text = font.render(f"Score: {score}", True, WHITE)
            screen.blit(score_text, (10, 10))

            for i in range(lives):
                pygame.draw.circle(screen, YELLOW, (WIDTH - (i + 1) * 32, 20), 10)
        else:
            game_over_text = font.render("Game Ended! Press Enter to Replay", True, WHITE)
            screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))

        pygame.display.flip()

        pygame.time.delay(100)

game_loop()

pygame.quit()
