class Soldier:
    def __init__(self,name):
        self.name = name

class Gun:
    def __init__(self):
        self.bullets = 2

    def AK47(self):
        print(f"AK47 did: ")
        if self.bullets:
            piy = 0
            for x in range(self.bullets):
                piy += 1
                self.bullets -= 1
                print("\tti-gi-ti-gi-tish",piy)
        else:
            print(f"No bullets!")
            self.patrons()

    def patrons(self):
        print(f"\tBullets left {self.bullets} pieces")

    def reload(self):
        self.bullets += 4
        print(f"Soldier {self.name.title()} scream 'REALOAD!'")

class Act_of_Shooting(Soldier,Gun):
    def __init__(self,name):
        Soldier.__init__(self,name)
        Gun.__init__(self)
        print(f"Bullets: {self.bullets} pieces")

Soldier = Act_of_Shooting('Peter')
Soldier.AK47()
Soldier.patrons()
Soldier.reload()