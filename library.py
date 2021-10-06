import time, sys
from character_class import Character
from monster_class import Monster
import commands as cmd
from world_creator import *
from account_handler import *
import shutil

ACTION = 0
TARGET = 1
NUMBER = 2

"""function for printing information about the room the player is in"""
def printInterface(currentRoom):
    if not canPlayerSee(currentRoom):
        print("Its too dark to see.")
    else:
        print(currentRoom.getRoomDesc())
        for item in currentRoom.getObjects():
            print(f"A "+item.getType() +".")
        printVisibleExits(currentRoom)    

def canPlayerSee(currentRoom):
    """Checks if room is lit, returns desc if true. If room is not lit, checks if
       player has a lit torch in inventory. If so, displays the room's description.
       If all fails, room is too dark to see."""
    if currentRoom.getDark() and not player.getIlluminated():
        return False
    else:
        return True

def checkWeight(item):
    if (player.getTotalWeight() + item.getWeight()) <= (player.getStr() * 10):
        return True
    else:
        print("It's too heavy!")
        return False
        
def playerDeath(playername):
    print("\nAn all encompassing voice bellows:\n")
    print("VICTORY NEEDS NO EXPLANATION, DEFEAT ALLOWS NONE.\n")
    print("The end.")
    shutil.rmtree(f'{playername.lower()}')
    sys.exit()




#function for taking and handling user input
def parsePlayerCommand(playerCommand, currentRoom):
    try: 
        command = playerCommand.strip().split()
        if command == []:
            return currentRoom

        elif command[ACTION] not in cmd._PLAYER_COMMANDS:
            print("Command doesn't exist.")

        elif command[ACTION] == cmd._HELP:
            cmd.displayHelpMenu()

        elif command[ACTION] == cmd._ATTACK:
            if not cmd.attack(command[TARGET], currentRoom):
                print("Invalid target.")

        elif command[ACTION] == cmd._GO:                                    
            newCurrentRoom = cmd.movePlayer(command[TARGET], currentRoom)
            if newCurrentRoom != None:
                printInterface(newCurrentRoom)
                return newCurrentRoom
            else:
                return currentRoom

        elif command[ACTION] == cmd._EXAMINE:
            if canPlayerSee(currentRoom):
                if command[TARGET] == "room":
                    printInterface(currentRoom)
                else:
                    cmd.examine(command[TARGET], currentRoom)
            else:
                print("It´s too dark to see.")

        elif command[ACTION] == cmd._STATUS:
            cmd.playerStatus() 

        elif command[ACTION] == cmd._TAKE_ITEM:
            if cmd.takeItem(command[TARGET], currentRoom):
                print(f"You take {command[TARGET]}.")
            else:
                print("You can't take that.")  

        elif command[ACTION] == cmd._DROP_ITEM:
            if cmd.dropItem(command[TARGET], currentRoom):
                print(f"You dropped {command[TARGET]}.")       
            else:
                print("You don't have that item.")

        elif command[ACTION] == cmd._INVENTORY:
            if player.getInventory():
                print("You're carrying:")
                cmd.printInventory(player)

        elif command[ACTION] == cmd._LOOT:
            if cmd.lootCheck(currentRoom, command[TARGET]):
                print(f"You loot it.")
            else:
                print("You can't loot that.")

        elif command[ACTION] == cmd._LIGHT:
            if cmd.lightExtinguish(command[ACTION], command[TARGET]):
                print("You light the torch.")
            elif not cmd.lightExtinguish(command[ACTION], command[TARGET]):
                print("That can't be lit.")

        elif command[ACTION] == cmd._EXTINGUISH:
            if cmd.lightExtinguish(command[ACTION], command[TARGET]):
                print("You put out the torch.")
            else:
                print("There is nothing to extinguish.")    

        elif command[ACTION] == cmd._EQUIP_ITEM:
            if cmd.manageGear(command[ACTION], command[TARGET]):
                print(f"You equipped {command[TARGET]}.")

        elif command[ACTION] == cmd._UNEQUIP_ITEM:
            if cmd.manageGear(command[ACTION], command[TARGET]):
                print(f"You unequipped {command[TARGET]}.")

        elif command[ACTION] == cmd._CONSUME_ITEM:
            if len(command) < 3:
                if cmd.consume(command[TARGET]):
                    print("You feel refreshed.")
                else:
                    print("You can't consume that!")
            elif len(command) == 3:
                if cmd.consume(command[TARGET], command[NUMBER]):
                    print("You feel refreshed.")
                else:
                    print("You can't consume that!")
        
        elif command[ACTION] == cmd._BUY:
            if currentRoom == cave_5:
                cmd.trade(command[ACTION], command[TARGET])
            else:
                print("You are nowhere near the shop!")
            
        elif command[ACTION] == cmd._SELL:
            if currentRoom == cave_5:
                cmd.trade(command[ACTION], command[TARGET])
            else:
                print("You are nowhere near the shop!")

        elif command[ACTION] == cmd._SAVE:
            saveGame(player, caves)
            print("Saved game.")

        elif command[ACTION] == cmd._QUIT:
            saveGame(player, caves)
            print("An all encompassing voice bellows: \n")
            print(f"SEIZE, {player.getName().upper()}.\nYOU SHALL SOON BE AGAIN.")
            sys.exit()
        elif command[ACTION] == cmd._OPEN:
            cmd.openContainer(currentRoom, command[TARGET])
        
        elif command[ACTION] == cmd._UNLOCK:
            cmd.unlock(currentRoom, command[TARGET])                
        return currentRoom
                
    except IndexError:
        print(f"{command[0].title()} what?")
        return currentRoom
        

#function for printing all visible exits in a room
def printVisibleExits(currentRoom):
    roomExits = []
    print("Visible exits: ", end='')
    if currentRoom.getExitWest():
        roomExits.append("West")   
    if currentRoom.getExitEast():
        roomExits.append("East")     
    if currentRoom.getExitNorth():
        roomExits.append("North")
    if currentRoom.getExitSouth():
        roomExits.append("South")
    print(str(roomExits).replace('[', '').replace(']', ''))