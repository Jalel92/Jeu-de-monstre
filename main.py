import os
from db_init import *
import random
from utils import *
from game import *


def afficher_menu():
    #Effacer le contenu du terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    #Afficher mon en-tête
    titre = "Jeu de combat"
    afficher_header_50(titre)
    #Afficher les choix possibles
    print("1. Démarrer une nouvelle partie")
    print("2. Afficher les 3 meilleurs scores")
    print("3. Quitter")

def creer_equipe():
    choix_team = []
    print("Voici la liste des personnages :")
    for i in range(len(personnages)) :
        print(f"{i}. {personnages[i]["name"]} | ❤️  ​PV : {personnages[i]["PV"]} | ⚔️  ​ATK : {personnages[i]["ATK"]} | 🛡️  ​DEF : {personnages[i]["DEF"]}") 
    for i in range(3) :
        num = int(input(" Entrez le numéro du personnage : "))
        if num in choix_team :
            raise ValueError("Ce personnage a déjà été séléctionné !")
        if num not in (0,1,2,3,4,5,6,7,8,9) :
            raise ValueError("Entrez un numéro correct !")
        choix_team.append(num)
    team = [personnages[choix_team[0]],personnages[choix_team[1]],personnages[choix_team[2]]]
    return team
        

def demander_pseudo():
    #Demander le pseudo
    pseudo = input("Entrez votre pseudo : ")  
    #Renvoyer le pseudo
    return pseudo

def enregistrer_score(pseudo,score) :
    dict0 = {'pseudo' : pseudo, 'score' : score}
    database["SCORES"].insert_one(dict0)

def nouvelle_partie():
    pseudo = demander_pseudo()
    equipe = creer_equipe()
    score = combattre(equipe)
    afficher_header_100(f"Tes combattans sont mort... Ils ont héroïquement vaincu {score} monstres !")
    enregistrer_score(pseudo,score)

def afficher_score() :
    resultats = database["SCORES"].find().limit(3) 
    c = 0
    for doc in resultats :
        print(f"Joueur : {doc['pseudo']}  | Score : {doc['score']} ")
    return resultats


def main() :
    afficher_menu()
    choix_joueur = int(input("Entrez un choix : "))
    if choix_joueur not in (1,2,3) :
        raise ValueError("Veuillez entrez un chiffre correct !")
    elif choix_joueur == 1 : #Option 1 : Démarrer une nouvelle partie
        nouvelle_partie()
    elif choix_joueur == 2 : #Option 2  : Affiche les 3 meilleurs scores
        print(afficher_score())
    else :#Option 3 : Quitter
        print("À bientot !")
        os.system('cls' if os.name == 'nt' else 'clear')

main()
    


    