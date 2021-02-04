import random

#https://fr.wikipedia.org/wiki/Liste_des_divinit%C3%A9s_slaves

class Monster():

    def __init__(self,maxVie=100,MaxAttaque=5,maxVitesse=3,nom="",description=""):
        self.vie = maxVie
        self.max_vie = maxVie
        self.attaque = MaxAttaque
        self.vitesse = maxVitesse
        self.nom = nom
        self.description = description


    def __add__(self, other):
        return Monster(maxVie=(self.vie+other.vie),  MaxAttaque=(self.attaque+other.attaque), maxVitesse=(self.vitesse+other.vitesse),  nom=f" {self.nom} et {other.nom}")

    def babayaga():
            return Monster(maxVie=2000,  MaxAttaque=50, maxVitesse=1,  nom = "Baba Yaga", description= "Sorcière qui mange les petits enfants.")

    def likho():
            return Monster(maxVie=1000,  MaxAttaque=25, maxVitesse=8,  nom = "Likho",description= "Personnification du mauvais sort et de la malchance.")

    def rod():
            return Monster(maxVie=1000000,  MaxAttaque=500, maxVitesse=3,  nom = "Rod",description="Père des dieux, créateur de tout ce qui existe.")

    def zaria():
            return Monster(maxVie=5000,  MaxAttaque=500, maxVitesse=100,  nom = "Zaria",description="Déesse de la beauté.")

        #todo (plus tard): faire des monstres  partir d'un dictionnaire

    def combat(self, other):
        while (self.vie > 0 or other.vie > 0):
            self.vie -= other.attaque
            other.vie -= self.attaque

            if self.vie <= 0:
                return False
            elif other.vie <= 0:
                return True

    def __str__(self):
        s=f" {self.nom} : Vie={self.vie:1.1f}/{self.max_vie:1.1f}"
        return s

    def __repr__(self):
        return f'Monster({self.nom}, {self.vie}/{self.max_vie}, {self.description}, {self.attaque}, {self.vitesse})'


class GroupeDeMonstre(): 
	lm = [Monster.rod(), Monster.babayaga(), Monster.likho(), Monster.zaria()]
	#nbpoints=10000 je ne sais pas comment faire
	def groupeAlea(n=10): 
		lmAlea = []
		l = [i for i in range(len(GroupeDeMonstre.lm))]
		for k in range(n):
			lmAlea.append(GroupeDeMonstre.lm[random.choice(l)])
		print(lmAlea) 

	def combattre(self,other): #Exécute le combat de deux groupes de monstres
		pass

	def meilleurGroupe(nbPoints=10000,nbCombats=1000):  #Renvoie le meilleur groupe de monstres de nbpoints après avoir fait fait nbCombats entre groupes
		pass


def main():
    babayaga1=Monster.babayaga()
    print(babayaga1)
    repr(babayaga1)
    likho=Monster.likho()
    rod=Monster.rod()
    zaria=Monster.zaria()
    if Monster.combat(babayaga1+babayaga1, likho+babayaga1) == True:
        print("Gagné ! ")
    else:
        print("Perdu !")
    GroupeDeMonstre.groupeAlea()

#https://docs.python.org/fr/3/library/__main__.html
if __name__ == "__main__":
    main()
