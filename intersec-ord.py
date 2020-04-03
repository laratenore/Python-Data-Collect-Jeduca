#!/usr/bin/env python

"""intersec-ord.py: O presente programa agrupa a intersecção entre os trabalhos coletados pelo
programa busca.py, excluindo assim, possíveis repetições e indicando quais termos se relacionam 
a cada trabalho. Por fim, ordena os trabalhos pela quantidade de termos."""

__author__      = "Lara Tenore Ferreira"
__credits__     = ["Lara Tenore Ferreira", "Jesús P. Mena-Chalco"]
__year__        = "2018"
__email__       = "lara.tenore@aluno.ufabc.edu.br"

import csv
import sys
 
csv.field_size_limit(sys.maxsize)
 
termos  = list(['jornalismo', 'imprensa', 'midia', '"cobertura jornalistica"', 'jornal','revista','televisao','TV','internet','jornalista', 'fundeb','"politicas educacionais"', '"financiamento"', 'alfabetizacao', 'curriculo', '"trabalho docente"','"avaliacao educacional"','"legislacao educacional"','creche','"qualidade da educacao"'])
dictTD  = dict([])
cont = 0
for t in termos:
     
    arquivoEntrada = "busca-resultados-"+t+".csv"
 
    with open(arquivoEntrada, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t', quotechar='"')
        for row in reader:
            idTD   = row[4]
            infoTD = row
            if not idTD in dictTD:
                dictTD[idTD] = ( set([t]), infoTD )
            else:
                dictTD[idTD][0].add(t)
 
listTD = list(dictTD.items())   
listTD = sorted(listTD, key=lambda x: len(x[1][0]))

	


tsv = "No de termos\tTermos\tAutor\tBiblioteca\tData da Defesa\tGrau Acadêmico\tID\tInstituição\tLink\tMunicipo do Programa\tNome do Programa\tPáginas\tTítulo\tVolumes\tResumo\n"
sep  = "\t"
 
while cont < len(listTD):
	tsv = tsv + str(len(listTD[cont][1][0])) +sep+ str(listTD[cont][1][0]) + sep
	for e in listTD[cont][1][1]:
		tsv += e + sep
	tsv = tsv + "\n"
	print(cont)
	cont += 1
 
arquivoSaida = "inter-ord.csv"
output = open(arquivoSaida, 'w')
output.write(tsv)
output.close

#print ("%%%%%%")
    #print (dictTD[TD][0])
    #print (dictTD[TD][1])
    #dictTD[TD][0] == termos // dictTD[TD][1] == complemento do csv anterior