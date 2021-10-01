import random
from items_class import *

class Character:
    """Initializes a template for character creation."""
    def __init__(self, name, item : list):
        self._name = name
        self._armor = 0
        self._level = 1
        self._hp = 100
        self._str = 2
        self._dex = 2
        self._isAlive = True
        self._damageModifier = 0
        self._xp = 0
        self._inventory = item
        self._wielded = False
        self._illuminated = False
        self._head = False
        self._chest = False
        self._coin = 100
        self._totalWeight = 0

    def getTotalWeight(self):
        return self._totalWeight

    def setTotalWeight(self, arg):
        self._totalWeight += arg
 
    def getIlluminated(self):
        """returns illuminated status"""
        return self._illuminated

    def getCoin(self):
        return self._coin

    #method for getting character name
    def getName(self):
        return self._name

    #method for getting character health
    def getHP(self):
        return self._hp
    
    #method for getting character experience
    def getXP(self):
        return self._xp
    
    #method for getting character strenght
    def getStr(self):
        return self._str

    #method for getting character dexterity
    def getDex(self):
        return self._dex
    
    #method for getting characters inventory
    def getInventory(self):
        return self._inventory

    #method for getting character dead/alive status
    def getIsAlive(self):
        return self._isAlive
    
    #method for getting character damage modifiers
    def getDamageModifier(self):
        return self._damageModifier 
    
    #method for getting character wielded status
    def getWielded(self):
        return self._wielded

    def getLevel(self):
        return self._level

    def getArmor(self):
        return self._armor
    
    def isEquipped(self, arg):
        if arg == "helmet":
            return self._head
        elif arg == "chestplate":   
            return self._chest
    
    def setEquipArmor(self, arg):
        if arg == "helmet":
            self._head = True
        elif arg == "chestplate":
            self._chest = True

    def setUneqiupArmor(self, arg):
        if arg == "helmet":
            self._head = None
        elif arg == "chestplate":
            self._chest = None
    

    def setIlluminated(self, arg):
        self._illuminated = arg

    #method for changing character experience 
    def setXP(self, XP):
        self._xp += XP

    #method for changing character health 
    def setHP(self, newHP):
        self._hp = newHP
    
    #method for changing character strenght
    def setStr(self, newStr):
        self._str = newStr
    
    #method for changing character wielded status to true
    def setWielded(self, weapon):
        if self._wielded:
            return False
        else:
            self._wielded = weapon
            self._damageModifier += weapon.getDamage()
    
    #method for changing character wielded status to false
    def setUnwield(self, weapon):
        self._wielded = False
        self._damageModifier -= weapon.getDamage()

    def setArmor(self, arg):
        self._armor += arg

    #method for character to take damage
    def takeDamage(self, dmg):
        taken_dmg = dmg - self._armor
        if taken_dmg > 1: 
            self._hp = self._hp - taken_dmg
            return taken_dmg
        else:
            self._hp = self._hp - 1
            return 1

    #method for character to do damage
    def doDamage(self):
        return (random.randint(1, (self._str + self._damageModifier )))
    
    #method for character to level up       
    def levelUp(self):
        if self._xp >= self._level * 200:
            self._hp += 10
            self._str += 1
            self._dex += 1
            self._level += 1
            return True
        else:
            return False
        
    def buy(self, item):
        self._inventory.append(item)


    def sell(self, item):
        self._inventory.remove(item)

    #def pickUp(self, item):
        #self._inventory.append(item)


    