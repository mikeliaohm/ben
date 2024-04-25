from .generic_agent import GenericAgent
from .human_agent import HumanAgent
from .naive_agent import NaiveAgent

# Player seats that uses agents, [North, East, South, West]
# True in a seat means the card will be dealt by an agent
AGENT_PLAYER = [False, False, True, False]
AGENT_TYPE = NaiveAgent