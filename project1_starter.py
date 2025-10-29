"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Tashe Graham]
Date: [10/20/2025]

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""


     #Creates a new character dictionary with calculated stats
    #Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    #Example:
    #char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    
    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
import os   

def calculate_stats(character_stand, level):
    base_stamina = 200
    stm_growth = 30
    range = "close"
    base_speed = 100
    spd_growth = 50
    base_strength = 150
    str_growth = 20

    if character_stand == "Star Platinum":
        base_stamina = 200
        stm_growth = 50
        range = "close"
        base_speed = 300
        spd_growth = 50
        base_strength = 350
        str_growth = 50
    elif character_stand == "The World":
        base_stamina = 175
        stm_growth = 35
        range = "long"
        base_speed = 275
        spd_growth = 35
        base_strength = 325
        str_growth = 35
    elif character_stand == "Stone Free":
        base_stamina = 150 
        stm_growth = 20
        range = "close"
        base_speed = 200
        spd_growth = 40
        base_strength = 275
        str_growth = 30
    elif character_stand == "Killer Queen":
        base_stamina = 125
        stm_growth = 50
        range = "long"
        base_speed = 150
        spd_growth = 75
        base_strength = 235
        str_growth = 50
    else:
        return "Invalid stand selection"
    
    strength = base_strength + ((level - 1) * str_growth)
    speed = base_speed + ((level - 1) * spd_growth)
    stamina = base_stamina + ((level - 1) * stm_growth)

    return (strength, stamina, speed)

def create_character(name, character_stand):
    level = 1
    strength = calculate_stats(character_stand, level)
    stamina = calculate_stats(character_stand, level)
    speed = calculate_stats(character_stand, level)
    character = {
            "name": name,
            "stand": character_stand,
            "level": level,
            "strength": strength,
            "stamina": stamina,
            "range": range,
            "speed": speed
        }
    
    return character

    
    
    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)
    pass

def save_character(character, filename):
    with open(filename, "w") as f:
        f.write(f"Character Name: {character['name']}\n")
        f.write(f"Stand: {character['stand']}\n")
        f.write(f"Level: {character['level']}\n")
        f.write(f"Strength: {character['strength']}\n")
        f.write(f"Stamina: {character['stamina']}\n")
        f.write(f"Range: {character['range']}\n")
        f.write(f"Speed: {character['speed']}\n")
    return True
   # Saves character to text file in specific format
   # Returns: True if successful, False if error occurred
    
  #  Required file format:
   # Character Name: [name]
    #Class: [class]
   # Level: [level]
    #Strength: [strength]
   # Magic: [magic]
   # Health: [health]
   # Gold: [gold]
    
    # TODO: Implement this function
    # Remember to handle file errors gracefully
    pass

def load_character(filename):
    if not os.path.exists(filename):
        print(f"Error: Character file not found at {filename}")

    with open(filename, "r") as f:
        character = {}
        lines = f.readlines()

        character['name'] = lines[0].split(': ')[1].strip()
        character['stand'] = lines[1].split(': ')[1].strip()
        character['level'] = int(lines[2].split(': ')[1].strip())
        character['strength'] = int(lines[3].split(': ')[1].strip())
        character['stamina'] = int(lines[4].split(': ')[1].strip())
        character['range'] = lines[5].split(': ')[1].strip()
        character['speed'] = int(lines[6].split(': ')[1].strip())
    return character


    
    #Loads character from text file
    #Returns: character dictionary if successful, None if file not found
    
    # TODO: Implement this function
    # Remember to handle file not found errors
    pass

def display_character(character):
    print(f"\n=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Stand: {character['stand']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Stamina: {character['stamina']}")
    print(f"Range: {character['range']}")
    print(f"Speed {character['speed']}")
    return None
    

    
   # Prints formatted character sheet
    #Returns: None (prints to console)
    
   # Example output:
   # === CHARACTER SHEET ===
   # Name: Aria
   # Class: Mage
   # Level: 1
   # Strength: 5
   # Magic: 15
    #Health: 80
    #Gold: 100
    
    # TODO: Implement this function
    pass

def level_up(character):
    character['level'] += 1
    print(f"\n{character['name']} has leveled up to Level {character['level']}!")

    strength, stamina, speed = calculate_stats(character['stand'], character['level'])

    character['strength'] = strength
    character['stamina'] = stamina
    character['speed'] = speed
    """
    #Increases character level and recalculates stats
   # Modifies the character dictionary directly
   # Returns: None
    """
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    pass

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    

    char = create_character("Tashe", "Killer Queen")
    display_character(char)

    save_file = "my_character.txt"
    if save_character(char, save_file):
        print(f"\nSuccessfully saved {char['name']} to {save_file}")
    
    print(f"Loading character from {save_file}...")
    loaded_char = load_character(save_file)

    if loaded_char:
        print(f"Load successfull!")
        display_character(loaded_char)
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")




