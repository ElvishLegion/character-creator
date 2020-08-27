import random

def drop_lowest (): #definition of drop lowest function
    a = (random.randint(1,6)) #Random number 1
    b = (random.randint(1,6)) #Random number 2
    c = (random.randint(1,6)) #Random number 3
    d = (random.randint(1,6)) #Random number 4

    array = [a, b, c, d] #Put random numbers in an array

    list.sort(array) #Sort the array

    sorted = (array[1:]) #This drops the lowest

    return (sum(sorted)) #This returns the final number after adding the remaining 3d6

def race (): # Definition of race function
    races = ["Dwarf", "Elf", "Halfling", "Human", "Dragonborn", "Gnome", "Half-Elf", "Half-Orc", "Tiefling"]
    return (random.choice(races)) #picks race
def alignment (): #Definition of alignment function
    alignments = ["Lawful Good" , "Neutral Good" , "Chaotic Good" , "Lawful Neutral" , "Neutral" , "Chaotic Neutral" , "Lawful Evil" , "Neutral Evil" , "Chaotic Evil"]
    return (random.choice(alignments)) #picks alingment
def Class (): #Definition of class function
    classes = ["Barb", "Bard", "Cleric", "Druid","Fighter","Monk", "Sorc", "Wizard", "Paladin", "Ranger", "Rogue", "Warlock"]
    return (random.choice(classes)) #picks class
print ('STR: ', (drop_lowest())) #Add label to numbers generated and print the returned number
print ('DEX: ', (drop_lowest()))
print ('CON: ', (drop_lowest()))
print ('INT: ', (drop_lowest()))
print ('WIS: ', (drop_lowest()))
print ('CHA: ', (drop_lowest()))

print (race())
print (alignment())
print (Class())