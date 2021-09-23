from .weapon import Weapon
import random

class Player:
    def __init__(self, name, id):
        self.name = name
        self.id = id

        # Stats
        self.health = 100
        self.hunger = 0
        self.thirst = 0
        self.strength = random.randint(50, 90)

        # Extra
        self.location = None 
        self.weapons: list[Weapon] = []
        self.killed = []
        self.reason_of_death = None

        # Runtime
        self.responses:int = 0
        self.response = None
        self.prompt = None
        self.finished_responding = False

    @classmethod
    def from_member(cls, member):
        return cls(member.name, member.id)

    @property
    def dead(self) -> bool:
        return any([
            self.health <= 0,
            self.hunger > 100, 
            self.thirst > 100, 
            self.reason_of_death is not None
        ])

    @property
    def responded(self) -> bool:
        return self.responses > 0
    
    def __repr__(self):
        return f'<Player: {self.name}>'

    def reset_responses(self):
        self.responses = 0
        self.response = None
        self.prompt = None        
        self.finished_responding = False
    
    def add_response(self, response):
        self.responses += 1
        self.response = self.prompt.responses[response]
        return self.response

    def get_prompt(self):
        prompt = self.location.get_prompt(self)
        return self.set_prompt(prompt)

    def set_prompt(self, prompt):
        self.prompt = prompt
        return self.prompt

    def kill(self, reason):
        self.health = 0
        self.reason_of_death = reason