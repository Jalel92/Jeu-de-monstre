import random
from utils import afficher_header_100
from db_init import personnages,monstres
from main import *

def en_vie(pv) :
    if pv > 0 :
        return True
    return False
 
def combattre(equipe) :
    #choisir un monstre
    monstre = random.choice(monstres)
    afficher_header_100(f"Vague 1 : L'équipe affrontera le monstre {monstre['name']} (⚔️  ATK : {monstre['ATK']} | 🛡️  DEF : {monstre['DEF']} | ❤️  PV : {monstre['PV']})")
    #equipe attaque monstre
    for i in range(len(equipe)) :
        attaquant = equipe[i]
        print(f"{attaquant['name']} attaque {monstre['name']} !")
        monstre['PV'] = monstre['PV'] - attaquant['ATK']




    #monstre attaque 1 joueur au hasard
    #si monstre mort -> vague suivant avec nouveau monstre



    # # Début du combat
    # vague = 0
    # while monstre['PV'] > 0 :
    #     team_actual = team

    #     attaquant = random.choice(team_actual)
    #     print(f"{attaquant['name']} attaque {monstre['name']} !")
    #     monstre['PV'] = monstre['PV'] - attaquant['ATK']

    #     team_actual.remove(attaquant)
    #     print(team_actual)

    #     attaquant2 = random.choice(team_actual)
    #     print(f"{attaquant2['name']} attaque {monstre['name']} !")
    #     monstre['PV'] = monstre['PV'] - attaquant['ATK']

    #     team_actual.remove(attaquant2)

    #     attaquant3 = random.choice(team_actual)
    #     print(f"{attaquant3['name']} attaque {monstre['name']} !")
    #     monstre['PV'] = monstre['PV'] - attaquant['ATK']

    #     if not  en_vie(monstre['PV']) :
    #         monstre['PV'] = 0

    #     print(f"{monstre['name']} n'a plus que {monstre['PV']} PV !")

    #     if en_vie(monstre['PV']) :
    #         cible_monstre = random.choice(team)
    #         cible_monstre['PV'] = cible_monstre['PV'] - monstre['ATK']
    #         print(f"{monstre['name']} attaque {cible_monstre['name']}")
    #         print(f"{cible_monstre['name']} n'a plus que {cible_monstre['PV']} PV !")


