def archivo():
	f = open ('AFN.txt','r')
	contador = 0
	auxiliar = ""
	taux = ""
	estados = []
	alfabeto = []
	iniciales = []
	transiciones = []
	finales = []
	for linea in f:
		#estados
		if (contador == 0):
			auxiliar = linea.rstrip('\n')
			for i in auxiliar:
				if (i != ","):
					estados.append(i)
		#alfabeto
		elif (contador == 1):
			auxiliar = linea.rstrip('\n')
			for i in auxiliar:
				if (i != ","):
					alfabeto.append(i)
		#iniciales
		elif (contador == 2):
			auxiliar = linea.rstrip('\n')
			for i in auxiliar:
				if (i != ","):
					iniciales.append(i)
		#finales
		elif (contador == 3):
			auxiliar = linea.rstrip('\n')
			for i in auxiliar:
				if (i != ","):
					finales.append(i)
		#transiciones
		elif (contador > 3):
			auxiliar = (linea.rstrip('\n'))
			for i in auxiliar:
				if (i != ","):
					taux = taux + str(i)
			transiciones.append(taux)
			taux = ""
		contador = contador + 1
	f.close()
	#imprime automata del archivo
	print("Automata original leido del archivo.")
	print("Estados:\t" + str(estados))
	print("Alfabeto:\t" + str(alfabeto))
	print("Iniciales:\t" + str(iniciales))
	print("Finales:\t" + str(finales))
	print("Transiciones:\t" + str(transiciones))
	return (estados,alfabeto,iniciales,finales,transiciones)

def completar_automata(estados,alfabeto,transiciones):
	#introduce un estado mas
	existe = False
	transiciones_aux = []
	num_estados = len(estados)
	estados.append(str(num_estados))
	for i in estados:
		for j in alfabeto:
			for k in transiciones:
				if((k[0] == i) and (k[1] == j)):
					existe = True
				pass
			if(existe == True):
				existe = False
			else:
				nueva_tran = i + j + str(num_estados)
				transiciones_aux.append(nueva_tran)
				nueva_tran = ""
	transiciones = transiciones + transiciones_aux
	#imprime automata del archivo
	print("\nAutomata completado.")
	print("Estados:\t" + str(estados))
	print("Alfabeto:\t" + str(alfabeto))
	print("Iniciales:\t" + str(iniciales))
	print("Finales:\t" + str(finales))
	print("Transiciones:\t" + str(transiciones))
	return (estados,alfabeto,transiciones)

def buscaCaminos(estado, caracter_indice, transiciones, cadena, aux, caminos_rec,finales):
	if (cadena[caracter_indice] != "."):
		for trs in transiciones:
			if (trs[0] == estado) and (cadena[caracter_indice] == trs[1]):
				aux = aux + trs[2]
				buscaCaminos(trs[2],caracter_indice+1, transiciones,cadena, aux, caminos_rec,finales)
	elif (cadena[caracter_indice] == "."):
		for f in finales:
			print(aux)
			if(f == aux[-1]):
				for x in aux:
					print ("q"+x+"("+")"+" ",)
				print("")
		

def validacion(cadena, iniciales, finales, transiciones):
	cont = 0
	caminos = []
	ramas = []
	camino_principal = ""
	rama_aux = ""
	aux = []
	aux_ramas = []
	resultado = []
	iniciales_lista = iniciales
	resultado.append(iniciales)
#extrae los bloques de estados siguientes
	for caracter in cadena:
		for inic in iniciales_lista:
			for trs in transiciones:
				if((trs[0] == inic) and (caracter == trs[1])):
					aux.append(trs[2])
		resultado.append(aux)
		iniciales_lista = aux
		aux = []


#extrae las ramas y la rama principal
	tamano_caminos =  len(resultado)
	num_caminos = len(resultado[-1])
	for i in resultado:
		camino_principal = camino_principal + i[0]
	#print(camino_principal)
	lista_guion = ["-"]
	for x in resultado:
		if (len(x) < num_caminos):
			for i in range(num_caminos - len(x)):
				x = lista_guion + x
			aux.append(x)
		elif(len(x)==num_caminos):
			aux.append(x)
	for i in range(num_caminos):
		for j in aux:
			rama_aux = rama_aux + j[i]
		aux_ramas.append(rama_aux)
		rama_aux = ""
	for x in aux_ramas:
		for i in x:
			if(i!="-"):
				rama_aux = rama_aux + i
		ramas.append(rama_aux)
		rama_aux = ""
	for r in ramas:
		for x in range(tamano_caminos-len(r)):
			rama_aux = rama_aux + camino_principal[x]
		rama_aux = rama_aux + r
		caminos.append(rama_aux)
		rama_aux = ""
#checa si es valido
	aceptada = False
	for camin in caminos:
		for est_final in finales:
			if( camin[-1] == est_final):
				aceptada = True
				print ("Cadena aceptada.\nCamino:",)
				#cont = 0
				#for c in camin:
				#	if cont == len(cadena):
				#		print "q"+c+"("+")",
				#	else:
				#		print "q"+c+"("+cadena[cont]+")",
				#		cont = cont + 1
				#print("")
	if aceptada==False:
		print("Cadena no aceptada.")

if __name__ == "__main__":
	(estados, alfabeto, iniciales, finales, transiciones) = archivo()
	(estados,alfabeto,transiciones) = completar_automata(estados,alfabeto,transiciones)
	cadena = raw_input("Cadena: ")
	cad = ""
	error = False
	aceptada=False
	for c in cadena:
		for alf in alfabeto:
			if(c==alf):
				aceptada = True
				cad = cad + c
		if aceptada==False:
			print("Error en el caracter: "+c)
			error = True
		aceptada = False
	if(error==True):
		print("Cadena trabajada con errores usando modo panico, la nueva cadena es: "+cad)
	print(cad)
	cadena = cad
	validacion(cadena ,iniciales ,finales ,transiciones)

	cadena = cadena + "."
	caminos_rec = []
	buscaCaminos(iniciales[0],0,transiciones,cadena,iniciales[0],caminos_rec,finales)
	
