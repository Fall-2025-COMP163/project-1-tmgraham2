"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Tashe Graham]
Date: [10/20/2025]
"""
import os # Import the os module for file system checks

def calculate_stats(character_class, level):
    
    
    
    # Set default stats
    base_strength = 5
    str_growth = 2
    base_magic = 5
    mag_growth = 2
    base_health = 80
    health_growth = 5

    # Adjust stats based on class
    if character_class == "Warrior":
        base_strength = 10
        str_growth = 3
        base_magic = 2
        mag_growth = 1
        base_health = 100
        health_growth = 10
    elif character_class == "Mage":
        base_strength = 3
        str_growth = 1
        base_magic = 15
        mag_growth = 3
        base_health = 80
        health_growth = 5
    elif character_class == "Rogue":
        base_strength = 7
        str_growth = 2
        base_magic = 7
        mag_growth = 2
        base_health = 70
        health_growth = 5
    elif character_class == "Cleric":
        base_strength = 5
        str_growth = 2
        base_magic = 10
        mag_growth = 3
        base_health = 90
        health_growth = 8
    
    # Calculate final stats based on level
    # Formula: base_stat + ((level - 1) * growth_rate)
    # We use (level - 1) so at level 1, stats are just the base stats.
    strength = base_strength + ((level - 1) * str_growth)
    magic = base_magic + ((level - 1) * mag_growth)
    health = base_health + ((level - 1) * health_growth)
    
    return (strength, magic, health)

def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats.
    
    Returns:
        dict: Keys: name, class, level, strength, magic, health, gold
    """
    
    level = 1
    gold = 100
    
    # Get stats from the calculation function
    strength, magic, health = calculate_stats(character_class, level)
    
    # Assemble the character dictionary
    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }
    
    return character


def save_character(character, filename):
    

    with open(filename, 'w') as f:
        f.write(f"Character Name: {character['name']}\n")
        f.write(f"Class: {character['class']}\n")
        f.write(f"Level: {character['level']}\n")
        f.write(f"Strength: {character['strength']}\n")
        f.write(f"Magic: {character['magic']}\n")
        f.write(f"Health: {character['health']}\n")
        f.write(f"Gold: {character['gold']}\n")
    return True

def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found or error
    """
    # Use if/else to check for file existence
    if not os.path.exists(filename):
        print(f"Error: Character file not found at {filename}")
        return None
        
    # If the file exists, we still need try/except for read/parsing errors
    # This handles cases where the file is empty or malformed
    
    # Removed try/except block as requested.
    # The program will crash if the file is empty or malformed.
    with open(filename, 'r') as f:
        character = {}
        lines = f.readlines()
        
        # Simple line-by-line parsing
        # Assumes file is always in the correct format
        character['name'] = lines[0].split(': ')[1].strip()
        character['class'] = lines[1].split(': ')[1].strip()
        character['level'] = int(lines[2].split(': ')[1].strip())
        character['strength'] = int(lines[3].split(': ')[1].strip())
        character['magic'] = int(lines[4].split(': ')[1].strip())
        character['health'] = int(lines[5].split(': ')[1].strip())
        character['gold'] = int(lines[6].split(': ')[1].strip())
        
        return character

def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    print("\n=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    print("=======================")

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # Increase level
    character['level'] += 1
    print(f"\n{character['name']} leveled up to Level {character['level']}!")
    
    # Recalculate stats for the new level
    strength, magic, health = calculate_stats(character['class'], character['level'])
    
    # Update the character dictionary
    character['strength'] = strength
    character['magic'] = magic
    character['health'] = health

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR v2.0 ===")
    
    # 1. Create a character
    char = create_character("TestHero", "Warrior")
    display_character(char)
    
    # 2. Level up the character
    level_up(char)
    display_character(char)

    # 3. Save the character
    save_file = "my_character.txt"
    if save_character(char, save_file):
        print(f"\nSuccessfully saved {char['name']} to {save_file}")
    
   







