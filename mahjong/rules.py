""" For each type of rules, turn on or off certain rules """
from dataclasses import dataclass


@dataclass
class Rules:
    hand_count: int = 13
