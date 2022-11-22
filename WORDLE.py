#!/usr/bin/env python3

from termcolor import colored
from os import system as s
from random import choice
from sys import platform
from time import time


# Date : 22 november 2022
# Game : WORDLE
#
# Author : Brunk
# Language : Python3
# Developped on : Fedora 37
#
# Github : https://github.com/NullBrunk


def cls():
    if platform == "linux":
        s("clear")
    else:
        s("cls")


def yellowbg(text: str) -> str:
    return colored(str(text), 'yellow', attrs=['reverse'])

def greenbg(text: str) -> str:
    return colored(str(text), 'green', attrs=['reverse'])

def greybg(text: str) -> str:
    return colored(str(text), 'white', attrs=['reverse'])

def redbg(text: str) -> str:
    return colored(str(text), 'red', attrs=['reverse'])

def get_words() -> list:
        return [ "agent", "aider", "aimer", "aller", "alors", "amour", "annee", "appel", "arbre", "arabe", "armee", "autre", "avion", "avoir", "balle", "blanc", "boire", "boite", "bonne", "bruit", "carre", "carte", "cause", "chaud", "chien", "choix", "chose", "clair", "corps", "cours", "creer", "crier", "debut", "doigt", "doute", "droit", "droit", "drole", "ecole", "effet", "envie", "facon", "faire", "faute", "femme", "filer", "fille", "finir", "fleur", "force", "forme", "frere", "froid", "front", "garde", "genre", "geste", "gosse", "grand", "grand", "grave", "hello", "heure", "homme", "hotel", "image", "jambe", "jeter", "jeune", "jouer", "jurer", "juste", "leger", "lever", "levre", "libre", "ligne", "livre", "maman", "matin", "mener", "merci", "merde", "metre", "monde", "moyen", "odeur", "ombre", "oncle", "ordre", "passe", "payer", "peine", "petit", "petit", "photo", "piece", "place", "plein", "poche", "point", "porte", "poser", "prier", "reste", "rêver", "rouge", "route", "salam", "salle", "salut", "scene", "serre", "singe", "signe", "soeur", "sorte", "suite", "sujet", "super", "table", "taire", "temps", "tenir", "terre", "tirer", "toute", "train", 'tronc', "venir", "verre", "vieux", "vieux", "ville", "vivre", "voler", ]

def show(tab):
    cls()
    for line in tab:
        print(line, end='') 

def game(toguess: str, words: list) -> int:
    
    tab = ["┌───────────────────────────────┐\n", "└───────────────────────────────┘"]

    for i in range(0,6):
        show(tab)
           
        cond = False
        while cond is False:

            das = colored("\n? ", 'cyan')
            user_word = input(das).lower()
            if user_word in words:
                cond = True
            else:
                print(redbg("Veuillez choisir un mot valide"))
        
        final_word = "│ "

        for i in range(len(user_word)):
            if user_word[i] == toguess[i]:
                final_word += greenbg(f"  {user_word[i].upper()}  ") + " "
               
            elif user_word[i] in toguess:
                final_word += yellowbg(f"  {user_word[i].upper()}  ") + " "
               
            else:
                final_word += greybg(f"  {user_word[i].upper()}  ") + " "

        final_word += "│\n"

        tab[-1] = final_word
        tab.append("└───────────────────────────────┘\n")
        
        if toguess == user_word:
            show(tab)
            print(greenbg("You guessed, gg !"))
            return 1    

    show(tab)
    
    print(redbg(f"\nLe mot à trouver était {toguess}."))
    return 0



def main():
    words = get_words()
    toguess = choice(words)
    
    t1 = time()
    game(toguess, words)    
    t2 = time()

    print(greenbg("Done in " + str(t2 - t1).split(".")[0] + "s"))

if __name__ == "__main__":
    main()
