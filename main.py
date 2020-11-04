### Making changes for AP CS ###

import time
import numpy as np
import sys

from Pokemon import Pokemon

if __name__ == '__main__':
    #Create Pokemon
    Charizard = Pokemon('Charizard', 'Fire', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'], {'ATTACK':12, 'DEFENSE': 8})
    Blastoise = Pokemon('Blastoise', 'Water', ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'],{'ATTACK': 10, 'DEFENSE':10})
    Venusaur = Pokemon('Venusaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'],{'ATTACK':8, 'DEFENSE':12})

    Charmander = Pokemon('Charmander', 'Fire', ['Ember', 'Scratch', 'Tackle', 'Fire Punch'],{'ATTACK':4, 'DEFENSE':2})
    Squirtle = Pokemon('Squirtle', 'Water', ['Bubblebeam', 'Tackle', 'Headbutt', 'Surf'],{'ATTACK': 3, 'DEFENSE':3})
    Bulbasaur = Pokemon('Bulbasaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Tackle', 'Leech Seed'],{'ATTACK':2, 'DEFENSE':4})

    Charmeleon = Pokemon('Charmeleon', 'Fire', ['Ember', 'Scratch', 'Flamethrower', 'Fire Punch'],{'ATTACK':6, 'DEFENSE':5})
    Wartortle = Pokemon('Wartortle', 'Water', ['Bubblebeam', 'Water Gun', 'Headbutt', 'Surf'],{'ATTACK': 5, 'DEFENSE':5})
    Ivysaur = Pokemon('Ivysaur\t', 'Grass', ['Vine Wip', 'Razor Leaf', 'Bullet Seed', 'Leech Seed'],{'ATTACK':4, 'DEFENSE':6})

    Growlithe = Pokemon('Growlithe', 'Fire', ['Ember', 'Scratch', 'Flamethrower', 'Fire Punch'],{'ATTACK':8, 'DEFENSE':4})
    Staryu = Pokemon('Staryu', 'Water', ['Bubblebeam', 'Water Gun', 'Headbutt', 'Surf'],{'ATTACK': 7, 'DEFENSE':5})
    Exeggcute = Pokemon('Exeggcute\t', 'Grass', ['Vine Wip', 'Razor Leaf', 'Bullet Seed', 'Leech Seed'],{'ATTACK':6, 'DEFENSE':6})

    Arcanine = Pokemon('Arcanine', 'Fire', ['Ember', 'Scratch', 'Flamethrower', 'Fire Punch'],{'ATTACK':6, 'DEFENSE':5})
    Starmie = Pokemon('Starmie', 'Water', ['Bubblebeam', 'Water Gun', 'Headbutt', 'Surf'],{'ATTACK': 5, 'DEFENSE':5})
    Exeggutor = Pokemon('Exeggutor\t', 'Grass', ['Vine Wip', 'Razor Leaf', 'Bullet Seed', 'Leech Seed'],{'ATTACK':4, 'DEFENSE':6})

     Kangaskhan = Pokemon('Kangaskhan', 'Normal', ['Pound', 'Bite', 'Stomp', 'Headbutt'],{'ATTACK':4, 'DEFENSE':9})
    Snorlax = Pokemon('Snorlax', 'Normal', ['Covet', 'Last Resort', 'Lick', 'Tackle'],{'ATTACK': 8, 'DEFENSE':5})
    Porygon = Pokemon('Porygon\t', 'Normal', ['Zap Cannon', 'Thunder Shock', 'Psybeam', 'Discharge'],{'ATTACK':6, 'DEFENSE':7})

     Vulpix = Pokemon('Vulpix', 'Fire', ['Ember', 'Incinerate', 'Extrasensory', 'Flamethrower'],{'ATTACK':4, 'DEFENSE':3})
    Magikarp = Pokemon('Magikarp', 'Water', ['Tackle', 'Splash', 'Bounce', 'Hydro Pump'],{'ATTACK': 5, 'DEFENSE':2})
    Rattata = Pokemon('Rattata\t', 'Normal', ['Tackle', 'Bite', 'Crunch', 'Sucker Punch'],{'ATTACK':1, 'DEFENSE':6})

    Ninetales = Pokemon('Ninetales', 'Fire', ['Ember', 'Extrasensory', 'Fire Blast', 'Headbutt'],{'ATTACK':4, 'DEFENSE':10})
    Gyarados = Pokemon('Gyarados', 'Water', ['Bite', 'Tackle', 'Whirlpool', 'Ice Fang'],{'ATTACK': 5, 'DEFENSE':9})
    Tropius = Pokemon('Tropius\t', 'Grass', ['Gust', 'Leaf Storm', 'Razor Leaf', 'Magical Leaf'],{'ATTACK':3, 'DEFENSE':11})


    Charizard.fight(Blastoise) # Get them to fight