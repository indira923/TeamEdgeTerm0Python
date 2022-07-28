from cmath import nanj
from contextlib import AsyncExitStack
from ntpath import join
from typing import ItemsView
from typing_extensions import Self
from unicodedata import name


class Characters :
    def __init__(self, name, attack, defense, health_points, temperture_points, relationship_points, inventory) :
        self.name = name
        self.attack = attack 
        self.defense =  defense
        self.health_points = health_points
        self.temperture_points = temperture_points
        self.relationship_points = relationship_points
        self.inventory = inventory 

main_character = Characters ("Mina",15, 30, 45, 30, 0, ["apple_juice"])
friend_1  = Characters("Jonah", 15, 30, 45, 30, 0, ["apple_juice,"])
ghost_butler = Characters("Lucas",15, 30, 45, 30, 0, ["coco, apple_juice "])
lost_maid = Characters("Katherine", 20, 40, 40, 50, 0, ["broom"] )
heartbroken_ghost= Characters("Ingrid", 30, 50,  40, 60, 0 ,["flowers"])
maid = Characters("Casey", 50, 70, 70, 0, ["apple_juice"])


class Locations :
    def __init__ (self, items, actions, characters, description):
        self. items = items 
        self.actions = actions
        self.characters = characters
        self.description = description 

class Actions :
    def __init__ (self, pick_up, go_to, look, touch):
        self.pick_up = pick_up
        self.go_to = go_to
        self.look = look
        self.touch = touch

entranced = "There are 3 rooms on this floor. You can go through the hallway, the stairs, and the basement. You need keys to go to these. the butler is here to assist you."
hallwayd = "The hallway has 4 paintings. The paintings are of a maid, a butler, a lost maid, and a heartbroken women. There is a vase on the table, and next to it is a doll."
living_roomd = "There is a ghost butler in here, he is friendly :)"
kitchend = "it is cold in here. "
bedroomd = "the maid is cleaning in here"
stairsd = "someone is laying dramatically on the stairs, blocking the exit"
basementd = "there is a mirror in here."

entrance = Locations(["key"],["pick up key"],[friend_1], entranced)
hallway = Locations(["vase", "dolls", "paintings", "key"],["look inside vase", "look under doll, pick up key, look at paintings,"], [friend_1, ghost_butler], hallwayd)
living_room = Locations(["tissue", "key",],["pick up tissue, pick up key,look around "], [friend_1, ghost_butler], living_roomd)
kitchen = Locations(["knife","key", "apple_juice"], ["pick up knife, take apple_juice, talk to ghost, look around"], [friend_1, ghost_butler, lost_maid], kitchend)
stairs = Locations(["tissue, doll, key"], ["open doll", "pick up key, talk to ghost,look around, "],[friend_1, ghost_butler, lost_maid, heartbroken_ghost], stairsd)
bedroom = Locations(["broom, key"], ["talk to ghost, touch broom"], [friend_1, ghost_butler, lost_maid, heartbroken_ghost, maid], bedroomd)
basement = Locations(["mirror"],["touch mirror"],[friend_1, ghost_butler, lost_maid, heartbroken_ghost, maid], basementd)




go_to_kitchen = Actions(["knife","key", "apple_juice"], [hallway, living_room],["there is a knife on the counter and the room is very cold. a ghost is holding flowers."],["ghost, flowers"])
go_to_living_room = Actions(["key,tissue"],[kitchen, entrance],["you are in the living room."],["key, tissue"])
go_to_hallway = Actions(["key, dolls, paintings,key"], [stairs, kitchen], ["there are 4 paintings in the hallway, along with a vase and a mirror."], ["paintings, doll"])



def prompt_user ():
    reply = input("where do you want to go?")
    return reply 

print("welcome to Eidolon")
welcome_message = "Hi, I'm Lucas, the butler of this house. I will be guiding you throughout the game."
print (welcome_message)
active = True 
current_location = entrance
while active:
    print(current_location.description)
    prompt_user()
    #active = False
#pick up here later    

def switch_locations(main_character): 
    switch_locations = Locations 
    switch_locations(main_character)

#def health_points ():


def relationship_points ():
    #if main_character 
    for x in range (50):
        print ("you can date now!")

class Talk :
    def __init__ (self, en_t, hw_t, kt_t, st_t, bd_t, bs_t):
        self.en_t = en_t
        self.hw_t = hw_t
        self.kt.t = kt_t
        self.st_t = st_t
        self.bd_t = bd_t 
        self.bs_t = bs_t 

def health_points ():
    for x in :



main_charactert = Talk()
friend_1t = Talk (["what is going on?"], ["these dolls are scary"], ["we should restock"], ["what is she doing"], ["this room is so clean, can she clean my room too?"], ["what do you think we should do Mina?"] )
ghost_butler = Talk (["you should pick up keys to go to other rooms"], ["try looking under the paintings and dolls"], ["you should restock"], [""])
lost_maid = Talk (["..."], [""])
heartbroken_ghost = Talk(["..."], ["what are they doing down there", ])
maid = Talk(["..."], [""])

join_party = 