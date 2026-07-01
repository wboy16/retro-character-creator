# 6. The Retro ASCII Profile Generator

print("Welcome to the Creation Screen for a Retro Text-Based Role-Playing Game (RPG)!!!")
print()
# --- DATA COLLECTION ---
character_name = input("Enter your Character name: \n")
character_class = input("Enter your Character Class (e.g., Warrior, Mage, Fighter, Rogue, Cleric, etc.): \n")
character_catchphrase = input("Enter your Character's Catchphrase: \n")
character_weapon = input("What is your Character's Weapon: \n")

# --- UI RENDERING ---

print("=" * 30)
print("|     CHARACTER SHEET     |")
print()
print("|Name:   " + character_name)
print("|Class:   " + character_class)
print("|Weapon:   " + character_weapon)
print("|Quote:   " + '"' + character_catchphrase + '!"')
print("=" * 30)
