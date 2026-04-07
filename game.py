import random
from utils import afficher_header_100
from db_init import personnages,monstres

def en_vie(perso) :
    if perso['PV'] > 0 :
        return True
    return False

def choix_monstre() : #ne pas oublier de changer la fonction pour ne pas tomber sur des monstres morts
    monstre = random.choice(monstres)
    return monstre

def equipe_en_vie(equipe) :
    c = 0
    for character in equipe :
        if en_vie(character) :
             c += 1
    return c == len(equipe)


def monstre_attack(monstre,equipe) :
    cible = random.choice(equipe)
    print(f"{monstre['name']} attaque {cible['name']} !")
    cible['PV'] = cible['PV'] - monstre['ATK']
    if cible['PV'] <= 0 :
        print(f"{cible['name']} est MORT !") 
        equipe.remove(cible)


def team_attack(equipe,monstre) :
    for i in range(len(equipe)) :
        attaquant = equipe[i]
        if en_vie(attaquant) :
            print(f"{attaquant['name']} attaque {monstre['name']} !")
            monstre['PV'] = monstre['PV'] - attaquant['ATK']
            print(f"{monstre['name']} n'a plus que {monstre['PV']} !")
         

def combattre(equipe) :
    #choisir un monstre
    monstre = choix_monstre()
    vague = 1
    while equipe_en_vie(equipe) : #tant que equipe n'est pas mort
        if en_vie(monstre) :#si monstre vivant :
                team_attack(equipe,monstre) #l'équipe attack le monstre
                if en_vie(monstre) : #si le monstre est encore vivant
                        monstre_attack(monstre,equipe) #le monstre attaque l'équipe
                elif not en_vie(monstre) : #si monstre mort :
                    monstre = choix_monstre()
                    vague += 1
                    afficher_header_100(f"Vague {vague} : L'équipe affrontera le monstre {monstre['name']} (⚔️  ATK : {monstre['ATK']} | 🛡️  DEF : {monstre['DEF']} | ❤️  PV : {monstre['PV']})")

    return vague




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


