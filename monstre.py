from random import *
import itertools as it

#https://fr.wikipedia.org/wiki/Liste_des_divinit%C3%A9s_slaves

class Monstre():
    def __init__(self,maxVie=100,MaxAttaque=5,maxVitesse=3,nom="",description=""):
        self.vie = maxVie
        self.max_vie = maxVie
        self.attaque = MaxAttaque
        self.vitesse = maxVitesse
        self.nom = nom
        self.description = description

    def monstreAlea():
        k=randint(1,10)
        if k==1:
            return Monstre.babayaga()
        elif k==2:
            Monstre.rod()
        elif k==3: return Monstre.likho()
        elif k==4: return Monstre.zaria()
        else:return Monstre(maxVie=randint(30,50),
                            MaxAttaque=randint(1,3)+randint(1,2),
                            maxVitesse=randint(2,3),
                            nom="MonstreAlea")
    def monstrePerso(vie=100):
        lnom = ["vodianoï", "léchi", "domovoï", "Almasty", "Dzedka", "Indrik", "Lazavik", "Polkan", "Zlydzens"] #https://fr.wikipedia.org/wiki/Liste_de_cr%C3%A9atures_l%C3%A9gendaires
        l = [i for i in range(len(lnom))]
        nom = choice(l)
        return Monstre(maxVie=randint(vie-10,vie+10),
                            MaxAttaque=randint(1,3)+randint(1,2),
                            maxVitesse=randint(2,3),
                            nom=nom)

    def babayaga():
        "Renvoie un Babayaga"
        return Monstre(maxVie=2000,  MaxAttaque=50, maxVitesse=1,  nom = "Baba Yaga", description= "Sorcière qui mange les petits enfants.")

    def likho():
        return Monstre(maxVie=1000,  MaxAttaque=25, maxVitesse=8,  nom = "Likho",description= "Personnification du mauvais sort et de la malchance.")

    def rod():
        return Monstre(maxVie=1000000,  MaxAttaque=500, maxVitesse=3,  nom = "Rod",description="Père des dieux, créateur de tout ce qui existe.")

    def zaria():
        return Monstre(maxVie=5000,  MaxAttaque=500, maxVitesse=100,  nom = "Zaria",description="Déesse de la beauté.")

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
        return f'Monstre({self.nom}, {self.vie}/{self.max_vie}, {self.description}, {self.attaque}, {self.vitesse})'


class GroupeDeMonstre():

    #nbpoints=10000 je ne sais pas comment faire
    def __init__(self,nom,lmonstres):
        self.lmonstres=lmonstres #Liste des monstres composant le groupe
        self.nom=nom  #le nom du groupe

    def groupeAlea(nom="Groupe à Léa",n=10):
        lm = [Monstre.monstreAlea() for k in range(n)]
        #TB mais on peut faire plus simple
##		l = [i for i in range(len(GroupeDeMonstre.lfm))]
##		for k in range(n):
##			lmAlea.append(GroupeDeMonstre.lm[random.choice(l)])
        g= GroupeDeMonstre(nom=nom,lmonstres=lm)
        return g

    def groupeAleaVal(nom="Groupe à Léa",TotalPV=1000000,j=100):
        "Renvoie un groupe de monstre avec à peu près TotalPV de points de vie"
        i=0 
        lm = []
        while(i < j):
            lm.append(Monstre.monstrePerso(vie=TotalPV/j))
            i+=1
        g= GroupeDeMonstre(nom=nom,lmonstres=lm)
        return g

        

    def combattre(self,other):
        while(self.lmonstres or other.lmonstres):
            if not(self.lmonstres):
                return False
            elif not(other.lmonstres):
                return True
            else:
                if Monstre.combat(self.lmonstres[-1], other.lmonstres[-1]) == True:
                    del other.lmonstres[-1]
                else:
                    del self.lmonstres[-1]
        #Exécute le combat de deux groupes de monstres
		#Tant que les listes de monstres self et other ne sont pas vides
        # On fait se combattre deux monstres
        #self.lmonstres est la liste des montres du groupe self
        #other.lmonstres est la liste des monstres gu roupe other
        #self.lmonstres[0] est le premier monstre du groupe self
        
    def meilleurGroupe(nbPoints=10000,nbCombats=1000):
        "Renvoie le meilleur groupe de monstres de nbpoints après avoir fait fait nbCombats entre groupes"
        lsmonstres = [Monstre.babayaga(), Monstre.rod(), Monstre.likho(), Monstre.zaria()]
        lcombo = []
        for i in range(1, len(lsmonstres)+1):
            lcombo.append(list(it.combinations(lsmonstres, i)))
        for k in range(0, nbCombats):
            if GroupeDeMonstre.combattre(lcombo[k], lcombo[k+1]):
                del lcombo[k+1]
        return lcombo
"""
Traceback (most recent call last):
  File "monstre080221.py", line 156, in <module>
    GroupeDeMonstre.meilleurGroupe()
  File "monstre080221.py", line 122, in meilleurGroupe
    if GroupeDeMonstre.combattre(lcombo[k], lcombo[k+1]):
  File "monstre080221.py", line 98, in combattre
    while(self.lmonstres or other.lmonstres):
AttributeError: 'list' object has no attribute 'lmonstres'

je ne comprend pas pourquoi


"""
        
    def __str__(self):
        s=f" {self.nom} comporte {self.n} monstres : "
        for m in self.lmonstres:
            s+="\n      "+str(m)
        return s

def main():
    m1=Monstre(nom="Albert")
    print(m1)
    babayaga1=Monstre.babayaga()
    print(babayaga1)
    print(repr(babayaga1))
    likho1=Monstre.likho()
    rod1=Monstre.rod()
    zaria1=Monstre.zaria()
    g2=GroupeDeMonstre.groupeAlea(nom="Groupe 2",n=5)
    g1=GroupeDeMonstre(nom="Groupe 1",lmonstres=[babayaga1,likho1,rod1,zaria1])
    if (GroupeDeMonstre.combattre(
        GroupeDeMonstre.groupeAleaVal(nom="Groupe 1",TotalPV=100000,j=100),
        GroupeDeMonstre.groupeAleaVal(nom="Groupe 2",TotalPV=5000,j=100)
        )):
        print("Gagné !")
    else: 
        print("Perdu !")
    
    if len(g1.lmonstres)>0:
        print("Gagné ! ")
    else:
        print("Perdu !")
GroupeDeMonstre.meilleurGroupe()
#https://docs.python.org/fr/3/library/__main__.html
if __name__ == "__main__":
    main()
                
