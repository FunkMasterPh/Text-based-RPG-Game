from items_class import Item

class Torch(Item):
    def __init__(self):
        super().__init__()
        self._weight = 3
        self._value = 5
        self._type = "torch"
        self._desc ="A stick on fire. "
        self._isOn = False
    
    #returns on/off status of torch
    def getOn(self):
        return self._isOn
    
    #sets torch status to on
    def setOnOff(self, arg):
        self._isOn = arg
    
    def getDesc(self):
        return self._desc

class Key(Item):
    def __init__(self, id, desc):
        super().__init__()
        self._weight = 2
        self._value = 50
        self._type = "key"
        self._id = id
        self._desc = desc
    
    def getDesc(self):
       return self._desc


class Lock(Item):
    def __init__(self, id):
        super().__init__()
        self._isLocked = True
        self._id = id
        self._desc = ""

    def getDesc(self):
        return self._desc

class Door(Item):
    def __init__(self, lock: Lock, direction):
        super().__init__()
        self._type = "door"
        self._isOpen = False
        self._desc = "A robust wooden door."
        self._lock = lock
        self._direction = direction
        
    def getIsOpen(self):
        return self._isOpen
    
    def getIsOpenPrint(self):
        if self._isOpen:
            return "an open"
        elif not self._isOpen:
            return "a closed"

    def getDesc(self):
        return self._desc
    
    def getDirection(self):
        return self._direction
    
    def setIsOpen(self, arg):
        self._isOpen = arg

    
  
class Chest(Item):
    def __init__(self, inventory: list):
        super().__init__()
        self._desc = "Treasure chest!"
        self._inventory = inventory
        
    def getDesc(self):
        return self._desc