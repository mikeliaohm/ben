"""
generic_agent.py
----------------
by Mike Liao

Create a generic agent class that defines a common set of interfaces.
"""

from typing import List, Dict

from objects import CardResp

class GenericAgent:
    def __init__(self, hand_str: str) -> None:
        self.hand52: CardResp = None

    # Invoked when the agent is to deal a hand for the initial trick.
    async def opening_lead(auction: List[str]) -> any:
        raise NotImplementedError
    
    async def async_play_card(trick_i: int, leader_i: int, 
        current_trick52: List[int], players_states: List[any], 
        bidding_scores: List[any], quality: any, 
        probability_of_occurence: List[float], shown_out_suits: List[Dict], 
        play_status: str) -> CardResp:
        raise NotImplementedError
    
    def set_real_card_played(opening_lead52: CardResp, player_i: int) -> None:
        raise NotImplementedError
    
    def set_card_played(trick_i: int, leader_i: int, i: int, card: int) -> None:
        raise NotImplementedError
    
    def set_own_card_played52(card52: int) -> None:
        raise NotImplementedError
    
    def set_public_card_played52(card52: int) -> None:
        raise NotImplementedError