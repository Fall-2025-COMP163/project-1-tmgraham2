"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Tashe Graham]
Date: [10/20/2025]
"""
 # Import the os module for file system checks

def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level.
    
    Returns:
        tuple: (strength, magic, health)
    """
    
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

# --- Example Usage ---

# Create a Mage as per the example
char_aria = create_character("Aria", "Mage")
print(f"Mage created: {char_aria}")
# Expected: {'name': 'Aria', 'class': 'Mage', 'level': 1, 'strength': 3, 'magic': 15, 'health': 80, 'gold': 100}

# Create a Warrior
char_grog = create_character("Grog", "Warrior")
print(f"Warrior created: {char_grog}")
# Expected: {'name': 'Grog', 'class': 'Warrior', 'level': 1, 'strength': 10, 'magic': 2, 'health': 100, 'gold': 100}

# Create a Rogue
char_vex = create_character("Vex", "Rogue")
print(f"Rogue created: {char_vex}")
# Expected: {'name': 'Vex', 'class': 'Rogue', 'level': 1, 'strength': 7, 'magic': 7, 'health': 70, 'gold': 100}

# Create a Cleric
char_pikel = create_character("Pikel", "Cleric")
print(f"Cleric created: {char_pikel}")
# Expected: {'name': 'Pikel', 'class': 'Cleric', 'level': 1, 'strength': 5, 'magic': 10, 'health': 90, 'gold': 100}

# --- Example of a higher level character ---
# Note: create_character currently defaults to level 1, 
# but we can test calculate_stats directly for a level 5 Warrior

lvl_5_warrior_stats = calculate_stats("Warrior", 5)
print(f"\nStats for a Level 5 Warrior: {lvl_5_warrior_stats}")
# Expected: Strength = 10 + (4*3) = 22
#           Magic    = 2  + (4*1) = 6
#           Health   = 100 + (4*10) = 140
# Output: Stats for a Level 5 Warrior: (22, 6, 140)

def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    # Health: [health]
    # Gold: [gold]
    """
    # NOTE: Using try/except here is still the best practice.
    # We can't easily predict write errors (like disk full or permissions)
    # with an if-statement, so catching the IOError is the correct way.
    
    # Removed try/except block as requested.
    # The program will crash if an IOError occurs (e.g., no write permission).
    with open('project1_starter.py', 'w') as f:
        f.write(f"Character Name: {character['name']}\n")
        f.write(f"Class: {character['class']}\n")
        f.write(f"Level: {character['level']}\n")
        f.write(f"Strength: {character['strength']}\n")
        f.write(f"Magic: {character['magic']}\n")
        f.write(f"Health: {character['health']}\n")
        f.write(f"Gold: {character['gold']}\n")
    return True

def load_character(filename):
    

import os   
    # Use if/else to check for file existence
    if not os.path.exists('project1_starter.py'):
        print(f"Error: Character file not found at {filename}")
        return None
      """  
    # If the file exists, we still need try/except for read/parsing errors
    # This handles cases where the file is empty or malformed
    
    # Removed try/except block as requested.
    # The program will crash if the file is empty or malformed.
    """
    with open('project1_starter.py', 'r') as f:
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
    save_file = 'project1_starter.py'
    if save_character(char, save_file):
        print(f"\nSuccessfully saved {char['name']} to {save_file}")
    
    # 4. Load the character
    print(f"Loading character from {save_file}...")
    loaded_char = load_character(save_file)
    
    if loaded_char:
        print("Load successful!")
        display_character(loaded_char)
        
        # Test that the loaded character is correct
        assert char == loaded_char
        print("Verified loaded data matches original.")
    
    # 5. Test file not found error
    print("\nTesting load error for missing file:")
    load_character("non_existent_file.txt")



