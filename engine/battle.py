import random

class Battle:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        self.over = False
        self.winner = None

    def effective_damage(self, player):
        if player.primary_weapon:
            return player.strength + player.primary_weapon.power
        else:
            return player.strength

    def get_other(self, player):
        return self.player1 if self.player2 == player else self.player2

    def attack(self, player, location):
        location_mult = {
            'head': random.randint(4, 6)/10,
            'body': random.randint(2, 8)/10,
            'legs': random.randint(2, 6)/10
        }
        other = self.get_other(player)
        damage = self.effective_damage(other) * location_mult[location]
        player.health -= damage
        if player.dead:
            self.over = True
            self.winner = other