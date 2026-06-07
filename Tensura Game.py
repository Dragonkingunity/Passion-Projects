# Story New Otherworlders appper with copys of the 14 ultimate skills causeing the world to colapse in 3 years time
# Creidts to ElTabaLuca for the EP Values of the Demon Lords
import random
'''player_races = ["Human", "Elf", "Dwarf", "Orc", "Goblin", "Beastmen", "Undead", "Walking Dead", "Oni", "Lesser angel", "Lesser Demon", "Harpy", "Giant", "Lizardman", "Slime", "Insectoid"]


base_races = ["Human", "Elf", "Dwarf", "Orc", "Goblin", "Lesser Spirit", "Beastmen", "Undead", "Walking Dead", "Oni", "Lesser angel", "Lesser Demon", "Harpy", "Giant", "Lizardman", "Slime", "Insectoid"]



human_Evolution = {
    "Human": {"next": "Enlightened Human", "needed EP": "100,000", "next": "Vampire", "need Zane Blood": "True"},
    "Enlightened Human": {"next": "Human Saint", "needed EP": "400,000"},
    "Human Saint": {"next": "Divine Human", "needed EP": "2,000,000"},
    "Divine Human": {"next": None}
}
vampire_Evolution = {
    "Vampire": {"next": "Vampire Overcomer", "needed EP": "150,000" or "Haverst Festival"},
    "Vampire Overcomer": {"next": "Vampire Lord", "needed EP": "400,000" },
    "Vampire Lord": {"next": "Divine Vampire", "needed EP": "2,000,000" },
    "Divine Vampire": {"next": None}
}'''






ultimate_Skills = [
    "Uriel, Lord of Vows",
    "Lucifer, Lord of Pride",
    "Michael, Lord of Justice",
    "Satanael, Lord of Wrath",
    "Raphael, Lord of Knowledge",
    "Beelzebuth, Lord of Gluttony",
    "Sariel, Lord of Hope",
    "Belphegor, Lord of Sloth",
    "Metatron, Lord of Purity",
    "Asmodeus, Lord of Lust" ,
    "Raguel, Lord of Charity",
    "Mammon, Lord of Greed",
    "Gabriel, Lord of Patience",
    "Leviathan, Lord of Envy" 

]

random.shuffle(ultimate_Skills)


#Players

p_1 = "Player 1"
print(f"{p_1} has the ultimate skill: {list(ultimate_Skills)[0]}")

p_2 = "Player 2"
print(f"{p_2} has the ultimate skill: {list(ultimate_Skills)[1]}")

p_3 = "Player 3"
print(f"{p_3} has the ultimate skill: {list(ultimate_Skills)[2]}")

p_4 = "Player 4"
print(f"{p_4} has the ultimate skill: {list(ultimate_Skills)[3]}")

p_5 = "Player 5"
print(f"{p_5} has the ultimate skill: {list(ultimate_Skills)[4]}")

p_6 = "Player 6"
print(f"{p_6} has the ultimate skill: {list(ultimate_Skills)[5]}")

p_7 = "Player 7"
print(f"{p_7} has the ultimate skill: {list(ultimate_Skills)[6]}")

p_8 = "Player 8"
print(f"{p_8} has the ultimate skill: {list(ultimate_Skills)[7]}")

p_9 = "Player 9"
print(f"{p_9} has the ultimate skill: {list(ultimate_Skills)[8]}")

p_10 = "Player 10"
print(f"{p_10} has the ultimate skill: {list(ultimate_Skills)[9]}")

p_11 = "Player 11"
print(f"{p_11} has the ultimate skill: {list(ultimate_Skills)[10]}")

p_12 = "Player 12"
print(f"{p_12} has the ultimate skill: {list(ultimate_Skills)[11]}")

p_13 = "Player 13"
print(f"{p_13} has the ultimate skill: {list(ultimate_Skills)[12]}")

p_14 = "Player 14"
print(f"{p_14} has the ultimate skill: {list(ultimate_Skills)[13]}")

demon_Lords = {"Guy Crimson": {"Race": "Primordial Daemon","ep": "40,000,000", "ultimate_Skill": "Lucifer, Lord of Pride"},
                "Rimuru Tempest":{"Race": "Demon Slime", "ep": "251,000,000", "ultimate_Skill": "Raphael, Lord of Knowledge" and "Beelzebuth, Lord of Gluttony" and "Uriel, Lord of Vows"},
                "Millim Nava": {"Race": "Dragoniod", "ep": "60,000,000", "ultimate_Skill": "Satanel, Lord of Wrath"},
                "Ramiris": {"Race": "Pixie", "ep": "6,000"},
                "Dagruel": {"Race": "Giant", "ep": "5,000,000"},
                "Luminous Valentine": {"Race": "High Blood", "ep": "6,000,000", "ultimate_Skill": "Asmodeus, Lord of Lust"},
                "Dino": {"Race": "Fallen Angel", "ep": "3,000,000", "ultimate_Skill": "Belphegor, Lord of Sloth"},
                "Leon Cromwell": {"Race": "Demonoid", "ep": "5,000,000", "ultimate_Skill": "Metatron, Lord of Purity"},
                }

'''twelve_Patrons = {"Benimaru": {"ep": "4,397,780"},
                   "Diablo": {"ep": "6,666,666"},
                   "Ranga": {"ep": "4,340,084"},
                    "Shion": {"ep": "4,229,140"},
                    "Carrera": {"ep": "7,013,351"},
                    "Testarossa": {"ep": "3,33,124"},
                    "Ultima": {"ep": "2,668,811"},
                    "Kumara": {"ep": "1,899,944"},
                    "Gabiru": {"ep": "1,263,824"},  
                    "Geld": {"ep": "2,378,749"},
                    "Zegion": {"ep": "4,988,856"},
                    "Adalman": {"ep": "877,333"}
                   }'''

true_Dragons = {"Veldora Tempest": {"Race": "True Dragon", "ep": "88,126,579"},
                "Velzard": {"Race": "True Dragon", "ep": "80,000,000", "ultimate_Skill": "Leviathan, Lord of Envy"},
                "Velgrynd": {"Race": "True Dragon", "ep": "74,350,087", "ultimate_Skill": "Raguel, Lord of Charity"},
                None: None,
                }

'''#"Beretta": {"ep": "1,970,873"}
#"Souei": {"ep": "1,281,162"}
# '''


def main():
    print("Welcome to the Tensura Game!")
    print("You are a new Otherworlder who has just arrived in this world.")
    print("Your goal is to level up, defeat monsters, and eventually challenge the Demon Lords and True Dragons to save the world from collapse.")
    print("Good luck on your journey!")

def level_up():
    global p_Level, p_Hp, p_Mp, p_min_Atk, p_Atk
    p_Level += 1
    p_Hp += 20
    p_Mp += 10
    p_min_Atk += 5
    p_Atk += 5
    print(f"\nCongratulations! You've reached Level {p_Level}!")
    print(f"Your stats have increased: HP: {p_Hp}, MP: {p_Mp}, ATK: {p_min_Atk}-{p_Atk}")








def woldboss(demon_lord, true_dragon):
    print("\n--- A World Boss appears! ---")
    print("The World Boss is a powerful monster that requires multiple players to defeat.")
    print("Defeating the World Boss will grant you a large amount of EP and rare items!")
    # Implement World Boss mechanics here (e.g., health, damage, rewards)

    if demon_lord == "Guy Crimson":
        print("The World Boss is Guy Crimson, the Primordial Daemon!")
        if true_dragon == "Vlzard":
            print("The true dragon Vlzard of Envy! Has come to protect Guy Crimson!")
        else:
            print("No true dragon has come to protect Guy Crimson!")

    elif demon_lord == "Rimuru Tempest":
        print("The World Boss is Rimuru Tempest, the Demon Slime!")
        if true_dragon == "Veldora Tempest":
            print("The true dragon Veldora Tempest! Has come to protect Rimuru Tempest!")
        else:
            print("No true dragon has come to protect Rimuru Tempest!")

    elif demon_lord == "Millim Nava":
        print("The World Boss is Millim Nava, the Dragoniod!")

    elif demon_lord == "Ramiris":
        print("The World Boss is Ramiris, the Pixie!")
        if true_dragon == "Veldora Tempest":
            print("The true dragon Veldora Tempest! Has come to protect Ramiris!")
        else:
            print("No true dragon has come to protect Ramiris!")

    elif demon_lord == "Dagruel":
        print("The World Boss is Dagruel, the Giant!")

    elif demon_lord == "Luminous Valentine":
        print("The World Boss is Luminous Valentine, the High Blood!")

    elif demon_lord == "Dino":
        print("The World Boss is Dino, the Fallen Angel!")

    elif demon_lord == "Leon Cromwell":
        print("The World Boss is Leon Cromwell, the Demonoid!")

    else:
        print("The World Boss is unknown!")

    if true_dragon is not None:
        print(f"There's a true dragon nearby: {true_dragon}")

woldboss(random.choice(list(demon_Lords.keys())), random.choice(list(true_Dragons.keys())))



