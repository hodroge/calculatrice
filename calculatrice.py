import os

operande1 = float (input ( "Entrer l'operande 1:"))
operation = input( """Entrer l'operation "+", "-", "*", ou "/" :""" )
#il ne faut pas oublier comme on a plusieurs condition il faut mettre plusieurs "
operande2 = float (input ("Entrer l'opération 2:"))

if operation == "+":
	resultat = operande1 + operande2
	print ( "%. 3f + %. 3f = % . 3f ", operande1, operande2, resultat)
elif operation == "-":
	resultat = operande1 - operande2
	print ( "%. 3f + %. 3f = % . 3f ", operande1, operande2, resultat)
# , 3f est 3 chiffre après la virgule
elif operation == "*":
	resultat = operande1 * operande2
	print ( "%. 3f + %. 3f = % . 3f ", operande1, operande2, resultat)
# pas mettre des parenthese avant les opperation
elif operation == "/":
	if (operande2):
		resultat = operande1 / operande2
		print ( "%. 3f + %. 3f = % . 3f ", operande1, operande2, resultat)
	else:
		print ("erreur : Division par zéro")
else: 
	print("erreur opération invalide")
# après else il faut revenir a la ligne après ajout de :
os.system ("pause")
#pour arrêter le programme à ce point et comme ça de vérifier en exécutant si le programme est correcvt jusqu’au se point
