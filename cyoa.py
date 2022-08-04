
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
ghost_butler = Characters("Lucas",15, 30, 45, 30, 0, ["coco, apple_juice"])
lost_maid = Characters("Katherine", 20, 40, 40, 50, 0, ["key"])
heartbroken_ghost= Characters("Ingrid", 30, 50,  40, 60, 0,["key"])
maid = Characters("Casey", 50, 70, 70, 60, 0, ["apple_juice"])


class Locations :
    def __init__ (self, name, items, actions, characters, description):
        self.name = name
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

entrance = Locations("entrance", ["key"],["pick up key"],[friend_1], entranced)
hallway = Locations("hallway", ["vase", "dolls", "paintings", "key"],["look inside vase", "look under doll", "pick up key", "look at paintings"], [friend_1, ghost_butler], hallwayd)
living_room = Locations("living_room", ["key",],["pick up tissue", "pick up key","look around "], [friend_1, ghost_butler], living_roomd)
kitchen = Locations("kitchen", ["knife","key", "apple_juice"], ["pick up knife", "take apple_juice", "talk to ghost", "look around"], [friend_1, ghost_butler, lost_maid], kitchend)
stairs = Locations("stairs", ["tissue, doll, key"], ["open doll", "pick up key", "talk to ghost" ,"look around"],[friend_1, ghost_butler, lost_maid, heartbroken_ghost], stairsd)
bedroom = Locations("bedroom", ["key"], ["pick up key"], [friend_1, ghost_butler, lost_maid, heartbroken_ghost, maid], bedroomd)
basement = Locations("basement", ["mirror"],["touch mirror"],[friend_1, ghost_butler, lost_maid, heartbroken_ghost, maid], basementd)

locations = [entrance, hallway, living_room, kitchen, stairs, bedroom, basement]


go_to_kitchen = Actions(["knife","key", "apple_juice"], [hallway, living_room],["there is a knife on the counter and the room is very cold. a ghost is holding flowers."],["ghost, flowers"])
go_to_living_room = Actions(["key"],[kitchen, entrance],["you are in the living room."],["key"])
go_to_hallway = Actions(["key", "dolls", "paintings"], [stairs, kitchen], ["there are 4 paintings in the hallway, along with a vase and a mirror."], ["paintings, doll"])


#current_items = key 
def prompt_user ():
    reply = input("where do you want to go? or do you want to pick up items or do an action?")
    if not switch_locations(reply):


        def Actions ():
            global actions
            for actions in current_location.actions:
                if reply == locations.action:
                 locations.action = actions 
                return True




def switch_locations(reply): 
    global current_location
    for location in locations:
        if reply == location.name:
            current_location = location
            return True
    


print("welcome to Eidolon")
welcome_message = "Hi, I'm Lucas, the butler of this house. I will be guiding you throughout the game."
print (welcome_message)
active = True 
current_location = entrance
while active:
    print(current_location.description)
    reply = prompt_user()
    switch_locations(reply)
    
#pick up here later    



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



friend_1t = Talk (["what is going on?"], ["these dolls are scary"], ["we should restock"], ["what is she doing"], ["this room is so clean, can she clean my room too?"], ["what do you think we should do Mina?"] )
ghost_butler = Talk (["you should pick up keys to go to other rooms"], ["try looking under the paintings and dolls"], ["you should restock"], ["..."], ["almost done!"], ["if you have all the keys you are free to leave."])
lost_maid = Talk (["..."], ["..."], ["there's some keys in here, you should look around"],["what"], ["we're almost at the exit"], ["i don't remember cleaning this part of the house."], [""])
heartbroken_ghost = Talk(["..."], ["what are they doing down there"],["..."], ["Oh no! I have lost my lovely maiden! "],["soon we can leave"], ["bye bye"] )
maid = Talk(["..."], ["..."], ["..."], ["maidenless"], ["everyone made it!"], ["bye!"] )




