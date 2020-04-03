#!/usr/bin/env python

"""flag.py: O presente programa tem como principal funcao indicar os trabalhos que se relacionem com determinado
 grupo de termos. O indicador, chamado de flag, varia de -1 a 1 e representa o grau de proximidade com um dos]
grupos de termos. No final, reescreve o arquivo previamente recebido com uma nova coluna inicial para flag."""

__author__      = "Lara Tenore Ferreira"
__credits__     = ["Lara Tenore Ferreira", "Jesús P. Mena-Chalco"]
__year__        = "2018"
__email__       = "lara.tenore@aluno.ufabc.edu.br"

import csv
import sys

csv.field_size_limit(sys.maxsize)

termosJ = list(['jornalismo', 'imprensa', 'midia', '"cobertura jornalistica"', 'jornal','revista','televisao','TV','internet','jornalista'])
termosE = list(['fundeb','"politicas educacionais"', '"financiamento"', 'alfabetizacao', 'curriculo', '"trabalho docente"','"avaliacao educacional"','"legislacao educacional"','creche','"qualidade da educacao"'])


arquivoEntrada = "inter-ord.csv"
y = list([])
with open(arquivoEntrada, newline='') as odsfile:
        reader = csv.reader(odsfile, delimiter='\t', quotechar='"')
        for row in reader:
                if(row[1] == "Termos"):
                        row.insert(0, "Flag")
                        y.extend([row])
                elif(row[1] != "Termos"):
                        contJ = 0
                        contE = 0
                        row[1] = row[1].replace('{', '')
                        row[1] = row[1].replace('}', '')
                        row[1] = row[1].replace("'", "")
                        row[1] = row[1].split(", ")
                        for p in row[1]:
                                if p in termosE:
                                        contE = contE - 1
                                if p in termosJ:
                                        contJ = contJ + 1
                                        #print("CONT E = " + str(contE))
                        total = contJ+contE
                        #print("CONT J + CONT E = " + str(total))
                        total = total/len(row[1])
                        row.insert(0, total)
                        y.extend([row])
#print(y)

arquivoSaida = "inter-ord-Flag.csv"

with open(arquivoSaida, 'w') as myfile:
    wr = csv.writer(myfile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    wr.writerows(y)

