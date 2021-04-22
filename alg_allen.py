#!/usr/bin/env python3
# -*-coding: utf-8 -*-

#Fonction de test pour la class Intervalle
def test():
	x = Intervalle(1,10)
	mylist = [1, 10, 11, 12, 10, 11, 8, 12, 1, 11, 0, 10, 0, 11, -1, 0]
	a = 1
	for i in range (0, 16, 2):
		y = Intervalle(mylist[i], mylist[i+1])
		print("\n\n----- Test numéro {} -----".format(a))
		x.display(y)
		if x.e(y):
			print("Les deux éléments sont égaux.")
		elif x.b(y):
			print("x est avant y")
		elif x.m(y):
			print("x précède y")
		elif x.o(y):
			print("x chevauche y")
		elif x.s(y):
			print("x commence y")
		elif x.ff(y):
			print("x termine y")
		elif x.dd(y):
			print("x est pendant y")
		elif x.bi(y):
			print("x est après y")
		else:
			print("Erreur: les éléments n'ont aucun liens entre eux.")
		a += 1
		print("")
		userless = input("Appuyez sur entrée pour lancer le prochain test")

class Intervalle:

	def __init__(self, d, f): 
		assert isinstance (f, int)
		assert isinstance (d, int) and d <= f 
		self.d = d 
		self.f = f

	"""Fonction de test d'égalité entre x et y. Input : x et y ; Output : affichage du résultat (égal ou non égal)"""
	def e(self, other):
		assert isinstance(other, Intervalle)
		if (self.f == other.f and self.d == other.d):
			return True
		else:
			return False

	"""Tester si x se situe avant y ou non. Input : x et y; Output : affichage du résultat (x avant y ou non)"""
	def b(self, other):
		assert isinstance(other, Intervalle)
		if(self.f < other.d):
			return True
		else:
			return False

	"""Tester si x précède y ou non. Input : x et y ; output : x précède y ou non"""
	def m(self, other):
		assert isinstance(other, Intervalle)
		if (self.f == other.d):
			return True
		else:
			return False

	"""Tester si x chevauche y. Input : x et y ; output : x chevauche y ou non"""
	def o(self, other):
		assert isinstance(other, Intervalle)
		if(self.d < other.d and other.d < self.f and self.f < other.f):
			return True
		else:
			return False

	"""Tester si x commence y. Input : x et y ; output : x commence y ou non"""
	def s(self, other):
		assert isinstance(other, Intervalle)
		if(self.d == other.d):
			return True
		else:
			return False

	"""Tester si x termine y. Input : x et y; output : x termine y ou non. Attention, si on utilise f,il y a une 
	confusion entre la fonction et l'attribut. Ce n'est pas logique car il y a une confusion entre une fonction 
	et un point mais soit. Ce problème est sûrement lié à la version de python utilisé"""
	def ff(self, other):
		assert isinstance(other, Intervalle)
		if (self.f == other.f):
			return True
		else:
			return False

	"""Tester si x est pendant y. Input : x et y ; output : x est pendant y ou non. Attention au nom de fonction 'd()'
	qui est confondus avec l'attribut 'd'"""
	def dd(self, other):
		assert isinstance(other, Intervalle)
		if(self.d > other.d and self.f < other.f):
			return True
		else:
			return False

	"""Tester si x est après ou avant y. On utilise la négation de la fonction b() pour avoir l'inverse.
	input : x et y ; output : x après y ou x pas après y
	On utilise la réciproque de la fonction b() pour avoir le résultat de bi()"""
	def bi(self, other):
		if(self.b(other) == False):
			return True
		else:
			return False

	#Fonction d'affichage des coordonnées des deux objets
	def display(self, other):
		print("L'objet x vaut : ({}, {})".format(self.d, self.f))
		print("L'objet y vaut : ({}, {})\n".format(other.d, other.f))


test()