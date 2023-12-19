# from enum import Enum
# from random import randrange
# import time

# class FeuTricolore:
#   def __init__(self, location, reference):
#     self.location = location
#     self.reference = reference
#     self.etatPanneau = "ETEINT"
#     self.color = "AUCUNE"

#   def etatDuPanneau(self):
#     print("le panneau numero {0} de {1} est actuellemet {2}".format(self.reference, self.location, self.etatPanneau))

#   def laCouleurDuFeu(self):
#     print("Le panneau numero {0} de {1} est actuellement au {2}".format(self.reference, self.location, self.color))

#   def passerAuRouge(self):
#     self.color = "ROUGE"  

#   def passerAuJaune(self):
#     self.color = "JAUNE"

#   def passerAuVert(self):
#     self.color = "VERT"

#   def allumerLePanneau(self):
#     self.etatPanneau = "ALLUME"  

#   def eteindreLePanneau(self):
#     self.etatPanneau = "ETEINT"  

# # Event = Enum('Event', ['LAISSER_CIRCULER', 'BLOQUER'])
# # aleatoire = randrange(2)


# # print(aleatoire)


# def simulateTrafic():
#   panneauA = FeuTricolore("Ndokoti", 3)
#   panneauA.etatDuPanneau()
#   panneauA.allumerLePanneau()
#   panneauA.etatDuPanneau()

#   panneauA.passerAuJaune()
#   panneauA.laCouleurDuFeu()
#   time.sleep(1)
#   panneauA.passerAuRouge()
#   panneauA.laCouleurDuFeu()
#   time.sleep(5)
#   panneauA.passerAuVert()
#   panneauA.laCouleurDuFeu()
#   time.sleep(2)

#   panneauA.eteindreLePanneau()
#   panneauA.etatDuPanneau()


# counter = 5

# while(counter > 0) :
#   simulateTrafic()
#   print("\n.................................Nouveau scenario...............")
#   counter-=1


import time
import random

# Initialisation des couleurs de chaque panneau
feux = {
    "panneau1": "vert",
    "panneau2": "rouge",
    "panneau3": "orange",
    "panneau4": "vert"
}

def changer_couleur(panneau):
    couleurs_possibles = ["vert", "orange", "rouge"]
    nouvelle_couleur = random.choice(couleurs_possibles)
    feux[panneau] = nouvelle_couleur
    print(f"{panneau}: {nouvelle_couleur}")

def gestion_feux():
    while True:
        for panneau in feux.keys():
            changer_couleur(panneau)
       
        # Temps que les couleurs restent inchangées
        time.sleep(5)

if __name__ == "main":
    gestion_feux()