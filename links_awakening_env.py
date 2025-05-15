"""Link's Awakening gymnasium environment."""

from typing import Dict

import gymnasium as gym
from gymnasium.spaces import Discrete
from pyboy import PyBoy
from pyboy.utils import WindowEvent


class LinksAwakeningEnv(gym.Env):
    """Link's Awakening DX environment for reinforcement learning."""

    def __init__(self, rom_path="LinksAwakeningDX.gbc"):
        super().__init__()

        self.pyboy = PyBoy(rom_path, window="SDL2")
        self.pyboy.set_emulation_speed(2)

        # We have 8 actions, corresponding to "down", "left",
        # "right", "up", "a", "b", "select", "start"
        self.action_space = Discrete(8)

        self.ACTIONS: Dict[int, int] = {
            0: WindowEvent.PRESS_ARROW_DOWN,
            1: WindowEvent.PRESS_ARROW_LEFT,
            2: WindowEvent.PRESS_ARROW_RIGHT,
            3: WindowEvent.PRESS_ARROW_UP,
            4: WindowEvent.PRESS_BUTTON_A,
            5: WindowEvent.PRESS_BUTTON_B,
            6: WindowEvent.PRESS_BUTTON_SELECT,
            7: WindowEvent.PRESS_BUTTON_START,
        }

    def step(self, action_idx):
        """
        Take a step in the environment.

        Args:
            action: The action to take

        Returns:
            Tuple of (observation, reward, done, truncated, info)
        """
        action = self.ACTIONS[action_idx]
        self.pyboy.send_input(action)
        for _ in range(2):
            self.pyboy.tick()
        release_event = WindowEvent[action.name.replace("PRESS", "RELEASE")]
        self.pyboy.send_input(release_event)
        for _ in range(2):
            self.pyboy.tick()
