from pyboy import PyBoy
from pyboy.utils import WindowEvent
import time

rom_path = "LinkAwakeningDX.gbc"
pyboy = PyBoy(rom_path, window="SDL2")
pyboy.set_emulation_speed(4)

# let the game boot
print("waiting for title screen...")
for _ in range(4000):
    pyboy.tick()

# press start to begin new game
print("pressing START to get past title screen...")
pyboy.send_input(WindowEvent.PRESS_BUTTON_START)
for _ in range(10):
    pyboy.tick()
pyboy.send_input(WindowEvent.RELEASE_BUTTON_START)

for _ in range(1000):
    pyboy.tick()
