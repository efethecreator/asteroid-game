# Asteroids Game

A classic Asteroids game clone developed in Python using [pygame](https://www.pygame.org/). The player controls a spaceship, shoots randomly appearing asteroids, and tries to avoid collisions.

## Features

- Asteroids spawn randomly and split when hit.
- The player can rotate and move the spaceship forward/backward.
- Shoot asteroids to destroy them.
- Collision detection and game over mechanics.

## Installation

1. Make sure Python 3.11 or higher is installed.
2. Install the required dependencies:
   ```sh
   pip install pygame==2.6.1
   ```
## Running the Game

Start the game by running the main file:
```sh
python main.py
```

## Controls

- **W**: Move forward
- **S**: Move backward
- **A**: Rotate left
- **D**: Rotate right
- **Space**: Shoot

## File Structure

- `main.py`: Game loop and startup
- `player.py`: Player spaceship
- `asteroid.py`: Asteroid object
- `asteroidfield.py`: Asteroid spawning and management
- `shot.py`: Bullet object
- `circleshape.py`: Base class for circular objects
- `constants.py`: Game constants

