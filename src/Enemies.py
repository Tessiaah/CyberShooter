class Enemy:
    def __init__(self, hp, maxhp, sprite, position=(0, 0)):
        self.hp = hp
        self.maxhp = maxhp
        self.sprite = sprite
        self.position = position

    def takedamage(self, playerdamage):
        self.hp -= playerdamage
        if self.hp < 0:
            self.hp = 0

    def fullheal(self):
        self.hp += self.maxhp

    def isdead(self):
        if self.hp == 0:
            return True
        return False
