import random
import uuid
from typing import Dict, Optional


class Agent:

    def __init__(self, money: float, agent_id: Optional[str] = None):
        if not agent_id:
            agent_id = str(uuid.uuid4())
        self.agent_id = agent_id
        self.money = money

    def win(self, amount: int = 1):
        pass

    def lose(self, amount: int = 1):
        pass

    def trade(self, other: 'Agent', amount: int = 1):
        pass

    def to_dict(self) -> Dict:
        return {
            "agent_id": self.agent_id,
            "money": self.money
        }
