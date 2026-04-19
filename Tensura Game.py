# Story New Otherworlders appper with copys of the 14 ultimate skills causeing the world to colapse in 3 years time
# Creidts to ElTabaLuca for the EP Values of the Demon Lords
import random


# Player Stats
p_EP = 0
p_Hp =
p_SHP =
p_Magicules =
p_Aura =


player_races = ["Human", "Elf", "Dwarf", "Orc", "Goblin", "Beastmen", "Undead", "Walking Dead", "Oni", "Lesser angel", "Lesser Demon", "Harpy", "Giant", "Lizardman", "Slime", "Insectoid"]


base_races = ["Human", "Elf", "Dwarf", "Orc", "Goblin", "Lesser Spirit", "Beastmen", "Undead", "Walking Dead", "Oni", "Lesser angel", "Lesser Demon", "Harpy", "Giant", "Lizardman", "Slime", "Insectoid"]



human_Evolution = {
    "Human": {"next": "Enlightened Human", "needed EP": "100,000", "next": "Vampire", "need Zane Blood"},
    "Enlightened Human": {"next": "Human Saint", "needed EP": "400,000"}
    "Human Saint": {"next": "Divine Human", "needed EP": "2,000,000"}
    "Divine Human": {"next": None}
}
vampire_Evolution = {
    "Vampire": {"next": "Vampire Overcomer", "needed EP": "150,000" or "Haverst Festival"},
    "Vampire Overcomer": {"next": "Vampire Lord", "needed EP": "400,000" }
    "Vampire Lord": {"next": "Divine Vampire", "needed EP": "2,000,000" }
    "Divine Vampire": {"next": None}
}






ultimate_Skills = {
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

}




demon_Lords = {"Guy Crimson": {"Race": "Primordial Daemon","ep": "40,000,000", "ultimate_Skill": "Lucifer, Lord of Pride"},
                "Rimuru Tempest":{"Race": "Demon Slime", "ep": "251,000,000", "ultimate_Skill": "Raphael, Lord of Knowledge" and "Beelzebuth, Lord of Gluttony" and "Uriel, Lord of Vows"},
                "Millim Nava": {"Race": "Dragoniod", "ep": "60,000,000", "ultimate_Skill": "Satanel, Lord of Wrath"},
                "Ramiris": {"Race": "Pixie", "ep": "6,000"},
                "Dagruel": {"Race": "Giant", "ep": "5,000,000"},
                "Luminous Valentine": {"Race": "High Blood", "ep": "6,000,000", "ultimate_Skill": "Asmodeus, Lord of Lust"},
                "Dino": {"Race": "Fallen Angel", "ep": "3,000,000", "ultimate_Skill": "Belphegor, Lord of Sloth"},
                "Leon Cromwell": {"Race": "Demonoid", "ep": "5,000,000", "ultimate_Skill": "Metatron, Lord of Purity"},
                }

twelve_Patrons = {"Benimaru": {"ep": "4,397,780"},
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
                   }

ture_Dragons = {"Veldora Tempest": {"Race": "True Dragon", "ep": "88,126,579"},
                "Velzard": {"Race": "True Dragon", "ep": "80,000,000", "ultimate_Skill": "Leviathan, Lord of Envy"},
                "Velgrynd": {"Race": "True Dragon", "ep": "74,350,087", "ultimate_Skill": "Raguel, Lord of Charity"},
                }

#"Beretta": {"ep": "1,970,873"}
#"Souei": {"ep": "1,281,162"}