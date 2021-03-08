"""
    instance:
        two characters fight
            1. Create Character Class
                class Character:

            2. instance attributes
                name, hp in the __init__() method
                def __init__(self,name,hp)
            3.
"""
import time


class Character:
    # attributes
    def __init__(self, name, hp):
        """
        __init__(), the method initialization
        :param name: duelist's names
        :param hp: duelist's health points
        """
        self.name = name
        self.hp = hp
        pass

    # def __new__(cls, *args, **kwargs):
    #     pass

    def __str__(self):
        return "%s remains %d hp" % (self.name, self.hp)

    def attack(self, rival):
        """
        attack enemy one time
        :param rival: enemy
        :return:
        """
        rival.hp -= 10  # enemy got hurt, -10 hp
        info = "%s hit %s, %s -10 hp " % (self.name, rival.name, rival.name)
        print(info)
        pass

    def kick(self, rival):
        """
        kick enemy one time
        :param rival: enemy
        :return:
        """
        rival.hp -= 15  # enemy is hurt, -15 hp
        info = "%s kicked %s, %s -15 hp" % (self.name, rival.name, rival.name)
        print(info)
        pass

    def med_treat(self):
        """
        med treat, add 10 hp
        :return:
        """
        med_info = "%s took a med, increased 10 hp" % self.name
        print(med_info)
        pass


# create two object to fight
cap_america = Character("Cap.America", 100)
super_man = Character("Superman", 100)

while True:
    if cap_america.hp <= 0 or super_man.hp <= 0:
        break
        pass
    cap_america.attack(super_man)  # cap_america attacked super man
    print(super_man)
    print(cap_america)
    print("+++++  ++++++  ++++++")
    cap_america.kick(super_man)
    print(super_man)
    print(cap_america)
    super_man.attack(cap_america)
    print(cap_america)
    print(super_man)
    print("+++++  ++++++  ++++++")
    cap_america.med_treat()
    print(cap_america)
    print(super_man)
    time.sleep(1)
    pass

print("game over!")
