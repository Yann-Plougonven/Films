class Realisateur:
    def __init__(self, identifiant, nom, prenom):
        self._identifiant = identifiant
        self._nom = nom
        self._prenom = prenom
        self._films = []
        
    def get_identifiant(self):
        return self._identifiant
    
    def get_nom(self):
        return self._nom
    
    def get_prenom(self):
        return self._prenom
    
    def presentation(self):
        return f"realisateur : {self._prenom} {self._nom}"
    
    def ajouter_film(self, film):
        self._films.append(film)
        film._realisateur = self
        
    def get_films(self):
        return self._films
    
    
class Film():
    def __init__(self, identifiant, titre, annee):
        self._identifiant = identifiant
        self._titre = titre
        self._annee = annee
        self._realisateur = None
        
    def get_identifiant(self):
        return self._identifiant
    
    def get_titre(self):
        return self._titre
    
    def get_annee(self):
        """
        >>> f1.get_annee()
        2005
        """
        return self._annee
    
    def get_realisateur(self):
        return self.realisateur
    
    def presentation(self):
        """
        >>> f1.presentation()
        'Le roi Yann'
        """
        return self.get_titre()
    
    def __repr__(self): # Pour avoir le nom et pas l'adresse RAM
        return self.presentation()
    

r1 = Realisateur(1, "Donald", "Trump")
#print(r1.presentation())
f1 = Film(1, "Le roi Yann", 2005)
f2 = Film(2, "apprends l'alphabet avec Dora", 2002)
#print("film :", f1.presentation())

r1.ajouter_film(f1)
r1.ajouter_film(f2)

#print(r1.get_films())
print(f1.presentation())

import doctest
doctest.testmod()