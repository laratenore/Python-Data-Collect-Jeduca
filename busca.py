#!/usr/bin/env python

"""busca.py: O presente programa faz uma busca online no site http://catalogodeteses.capes.gov.br 
de acordo com termos e anos definidos como parâmetros e gera um csv com todos os trabalhos
encontrados por termo, incluindo os resumos encontrados na Plataforma Sucupira."""

__author__      = "Lara Tenore Ferreira"
__credits__     = ["Lara Tenore Ferreira", "Jesús P. Mena-Chalco"]
__year__        = "2018"
__email__       = "lara.tenore@aluno.ufabc.edu.br"



import requests
import time
import csv
import os
from bs4 import BeautifulSoup

#=======================================================
# PRIMEIRO PROGRAMA - CATALOGO DE TESES E DISSERTAÇÕES
#=======================================================

prefixoDeSaida = "busca-resultados-"
anos = [ "2013", "2014", "2015", "2016", "2017"] 

termos = list(['fundeb','"politicas educacionais"', '"financiamento"', 'alfabetizacao', 'curriculo', '"trabalho docente"','"avaliacao educacional"','"legislacao educacional"','creche','"qualidade da educacao"'])

for t in termos:
    arquivoSaida = prefixoDeSaida+t+".csv"        
    print("\nArquivo: {}".format(arquivoSaida) )

    x = list([])
    for year in anos:
        page = 1             # <--- deve iniciar em 1
        flagProcessar = True
        while flagProcessar and page<500:
            jsonPost =  {
            "termo":t,
            "filtros":[{
                "campo":"Ano",
                "valor":year}],
            "pagina":page,
            "registrosPorPagina":20
            }

            # Usamos o try-except caso a consulta no servidor nao seja realizada de forma correta
            try:  
                r = requests.post('http://catalogodeteses.capes.gov.br/catalogo-teses/rest/busca', json=jsonPost)
                dJson = r.json()

                if (u'tesesDissertacoes' in dJson) and (len(dJson[u'tesesDissertacoes']))!=0:
                    print("Termo: {} \tAno: {} \tPagina: {} \tStatus: {}\t Elementos:{} ".format(t, year, page, r.status_code, len(dJson[u'tesesDissertacoes'])) )
                    x.extend(dJson[u'tesesDissertacoes'])
                
                    page += 1
                    time.sleep(2)
                else:
                    flagProcessar = False
            except:
                print("--Tentando baixar novamente o Json em 10 segundos")
                time.sleep(10)
                continue

    print("Lista de trabalhos identificados: {}\n".format(len(x)) )
    
   #Convertendo cada elemento para utf8 ---- usar em iOS
 """for item in x:
        for k in item.keys():
            item[k] = item[k].encode('utf8')"""

    # Usamos um dicionario para converter a lista 'x' de trabalhos em um CSV 
    with open(arquivoSaida,'w') as f:
        title = "autor, biblioteca, dataDefesa, grauAcademico, id, instituicao, link, municipioPrograma, nomePrograma, paginas, titulo, volumes".split(", ") # quick hack
        cw = csv.DictWriter(f, title, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        cw.writeheader()
        cw.writerows(x)
        # Os arquivos gerados serao CSV, em que o caractere \t (TAB) eh o elemento usado para separar celular


  #==================================================================
  # SEGUNDO PROGRAMA - RESUMOS
  #==================================================================

    print("Iniciando busca de resumos...")
    y = list([])
    arquivo_Entrada = arquivoSaida #entrada com o nome do csv
    print("\nArquivo: {}".format(arquivo_Entrada) )

    with open(arquivo_Entrada, newline='') as csvfile:
        cont = 0
        reader = csv.reader(csvfile, delimiter='\t', quotechar='"')

        for row in reader:
            if(row[6] == "link"):
                row.append("resumo")
                y.extend([row])

            elif(row[6] != "link"):
                try:
                    page = requests.get(row[6])
                    page
                    soup = BeautifulSoup(page.content, 'html.parser')
                    cont = cont + 1

                    #salvando o html 
                    html_path = "/home/usuario/folder1/folder2" #substituir pelo local correto onde quer salvar o html das páginas
                    output =open(os.path.join(html_path, row[4]+".html"),'w') #salva página sucupira pelo id do trabalho
                    output.write(soup.prettify())
                    output.close

                    if(len(soup.find_all(id="resumo")) != 0):
                        #encontrando o resumo
                        resumo = soup.find_all(id="resumo")[0].get_text()
                        resumo = resumo.replace("\r\n", " ") #quebra de linha
                        row.append(resumo)
                        y.extend([row])
                        print(cont)

                    else:
                        print("- link sem resumo (erro)")
                        row.append("sem resumo")
                        y.extend([row])

                    time.sleep(2)

                
                except:
                    print("--Tentando acessar novamente em 10 segundos")
                    time.sleep(10)
                    continue

        arquivo_Saida = arquivo_Entrada
        csv_path = "/home/usuario/folder1/folder2/" #substituir pelo local correto onde quer salvar os csv finais
        with open(os.path.join(csv_path, arquivo_Saida),'w') as f:
            cw = csv.writer(f, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)            
            cw.writerows(y)