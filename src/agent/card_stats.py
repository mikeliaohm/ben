import enum
from typing import Dict, List, Tuple
from collections import deque

from .card_utils import index_to_card

class PlayerPosition(enum.Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

# Store a card trick
CardTrick = List[Tuple[PlayerPosition, int]]
CardPlayed = deque[CardTrick]

# Store the probability distribution of each card
CardDist = Dict[int, Tuple[PlayerPosition, float]]

def append_trick(tricks: CardPlayed, position: PlayerPosition, card: int) -> None:
    """
    Append a card to the current trick.
    """
    # new trick
    if len(tricks) == 0 or len(tricks[-1]) == 4:
        tricks.append([(position, card)])
    # existing trick
    else:
        tricks[-1].append((position, card))

def print_deque(deque: CardPlayed) -> None:
    """
    Print the contents of a deque.
    """
    for idx, tricks in enumerate(deque):
        print(f"Trick {idx + 1}:")
        for trick in tricks:
            print(f"Player {trick[0]} / Card {index_to_card(trick[1])}")