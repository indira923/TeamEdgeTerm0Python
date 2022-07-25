from contextlib import AsyncExitStack
from typing import ItemsView
from unicodedata import name


class Characters :
    def __init__(self, name, attack, defense, health_points, temperture_points, relationship_points, inventory) :
        self.name = name
        self.attack = attack 
        self.defense =  defense
        self.health_points = health_points
        self.temperture.points = temperture_points
        self.relationship_points = relationship_points
        self.inventory = inventory 

main_character = Characters ("Mina",15, 30, 45, 30, 0, ["apple_juice"])
friend_1  = Characters("Jonah", 15, 30, 30, 45, 30, 0, ["apple_juice,"])
ghost_butler = Characters("Lucas",15, 30, 30, 45, 30, 0, ["coco, apple_juice "])
lost_maid = Characters("Katherine", 20, 40, 40, 50, 0,["broom"] )
heartbroken_ghost= Characters("Ingrid", 30, 50, 60, 0 ["flowers"])
maid = ("Casey", 50, 70, 70, 0)


class Locations :
    def __init__ (self, items, actions, characters):
        self. items = items 
        self.actions = actions
        self.characters = characters

class Actions :
    def __init__ (self, pick_up, go_to, look, touch):
        self.pick_up = pick_up
        self.go_to = go_to
        self.look = look
        self.touch = touch

entrance = Locations (["key"],"[pick up key"],["jonah, mina"])
hallway = Locations (["vase, dolls, paintings, key"],["look inside vase, look under doll, pick up key, look at paintings,"], ["Jonah,Lucas, Mina"] )
living_room = Locations(["tissue", "key",],["pick up tissue, pick up key,look around "], ["Jonah, Lucas, Mina"] )
kitchen = Locations(["knife","key", "apple_juice"], ["pick up knife, take apple_juice, talk to ghost, look around"], ["Jonah, Lucas, Mina, Katherine"])
stairs = Locations (["tissue, doll, key"], ["open doll", "pick up key, talk to ghost,look around, "],["jonah, lucas, mina, katherine, ingrid "])
bedroom = Locations(["broom, key"], ["talk to ghost, touch broom"], ["jonah, lucas, mina, casey, ingrid "])
basement = Locations(["mirror"],["touch mirror"],["jonah, lucas, mina, casey,ingrid"])

player_inventory = []
entrance = print("There are 3 rooms on this floor. You can go through the hallway, the stairs, and the basement. You need keys to go to these. the butler is here to assist you.")
hallway = print("The hallway has 4 paintings. The paintings are of a maid, a butler, a lost maid, and someone experiencing heartbreak. There is a vase on the table, and next to it is a doll.")
living_room = print("There is a ghost butler in here, he is friendly :)")
kitchen = print("it is cold in here. ")
bedroom = print("the maid is cleaning in here")
stairs = print("someone is laying dramatically on the stairs, blocking the exit")
basement = print("there is a mirror in here.")

go_to_kitchen = Actions (["knife","key", "apple_juice"], ["hallway, living_room"],["there is a knife on the counter and the room is very cold. a ghost is holding flowers."],["ghost, flowers"])
go_to_living_room = Actions (["you are in the living room"],["kitchen, entrance"],[])
go_to_hallway = Actions( )



def prompt_user ():
    reply = input("where do you want to go?")
    return reply 

