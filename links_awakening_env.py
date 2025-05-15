"""Link's Awakening gymnasium environment."""

from typing import Any, Literal, Optional

import gymnasium as gym
from gymnasium.spaces import Discrete
from pyboy import PyBoy
from pyboy.utils import WindowEvent


class LinksAwakeningEnv(gym.Env):
    """Link's Awakening DX environment for reinforcement learning."""

    def __init__(self, rom_path: str = "LinksAwakeningDX.gbc") -> None:
        super().__init__()

        self.pyboy = PyBoy(
            rom_path, window="SDL2"
        )  # loads the game rom, runs it in a visible window (SDL2)
        self.pyboy.set_emulation_speed(2)  # speeds up emulation (2x)

        # We have 8 actions, corresponding to "down", "left",
        # "right", "up", "a", "b", "select", "start"
        self.action_space = Discrete(8)

        self.ACTIONS: dict[int, int] = {
            0: WindowEvent.PRESS_ARROW_DOWN,
            1: WindowEvent.PRESS_ARROW_LEFT,
            2: WindowEvent.PRESS_ARROW_RIGHT,
            3: WindowEvent.PRESS_ARROW_UP,
            4: WindowEvent.PRESS_BUTTON_A,
            5: WindowEvent.PRESS_BUTTON_B,
            6: WindowEvent.PRESS_BUTTON_SELECT,
            7: WindowEvent.PRESS_BUTTON_START,
        }

    def reset(
        self, seed: Optional[int] = None, options: Optional[dict] = None
    ) -> tuple[Any, Any]:
        # TODO
        pass

    def step(self, action_idx: Any) -> tuple[Any, Any, Any, Literal[False], dict]:
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

        observation = self._get_obs()
        reward = self._get_reward()
        terminated = self._check_done()

        return observation, reward, terminated, False, {}

    def _get_obs(self):
        return

    def _get_reward(self) -> int:
        # placeholder reward logic: always return 0
        return 0

    def _check_done(self):
        return
