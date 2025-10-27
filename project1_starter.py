"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Your Name Here]
Date: [Date]

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""

def create_character(name, character_class):
        level = 1
    strength, stamina, speed = calculate_stats(character_stand, level)
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
    pass

def calculate_stats(character_class, level):
    name = input("Enter your name:")
    character_stand = input("Select a stand from list:\nStar Platinum, The World, Stone Free, Killer Queen ")
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
    pass

def load_character(filename):
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
    pass

def level_up(character):
character['level'] += 1
    print(f"\n{character['name']} has leveled up to Level {character['level']}!")

    strength, stamina, speed = calculate_stats(character['stand'], character['level'])

    character['strength'] = strength
    character['stamina'] = stamina
    character['speed'] = speed 
    
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    pass

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
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
