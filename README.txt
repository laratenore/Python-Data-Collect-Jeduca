READ ME



Pré-requisitos para uso dos programas:
	
- Python 3
	
- instalar modulo requests
	
- instalar modulo beautifulsoup (bs4)

- instalar modulo csv


Passo a passo para a utilização do programa "busca.py":

1) Definir os parâmetros:
	Linha 25 - ano de publicação do trabalho: inserir anos entre aspas duplas e separados por vírgula. Ex: anos = ["2013", "2016"].
	Linha 27 - termos de busca: inserir os termos entre aspas simples, separados por vírgulae sem acentos. Termos com mais de uma palavra dever ser inserios entre aspas simples e aspas duplas. Ex: termos = list(['escolas', '"politicas educacionais"']).
	Linha 37 - caso queira coletar de um número específico de páginas, alterar a linha substindo '500' pelo número de páginas somado em um. Ex: Até página 10: "while flagProcessar and page<11:".

2) Enconding:
	Caso esteja usando um sistema operacional que não use como codificação padrão utf-8 (e.g. iOS), retirar as aspas ' """ ' no inicio da linha 68 e no fim da linha 70;

3) Local para salvar arquivos:
	Linha 107 - para salvar o html das fichas de cada trabalho da Plataforma Sucupira, é recomendado salvar em uma pasta separada dos demais arquivos. Após criar esta pasta, mude a linha alterando o nome do usuário e o caminho que o programa deve fazer até ela. OBS: 
Ex: caminho: documentos->Jornalismo->EAD->fichas = 
html_path = "/home/Joao/documentos/Jornalismo/EAD/fichas" 
	Linha 134 - idem ao item anterior mas com o caminho onde quer salvar os csv atualizados com resumos. Ex: html_path = "/home/Joao/documentos/Jornalismo/EAD/resutados-resumos"

Passo a passo para a utilização do programa "intersec-ord.py":

IMPORTANTE: o arquivo do programa deve estar na mesma pasta que os csv atualizados salvos pelo programa "busca.py"

1) Termos para intersecção:
	Linha 17 - termos que deseja encontrar intersecções entre trabalhos. Seguir mesmas regras de aspas duplas para termos com mais de uma palavra e de não inserir acentos. Ex: termos = list(['jornalismo', '"politicas educacionais"']).
	Linha 51 - caso queira especificar o nome do arquivo de intersecção de trabalhos, mudar o termo entre aspas. Ex: arquivoSaida = "inter-ord.ods" -> arquivoSaida = "inter-ord-termosJornalismo.ods".

Obs: arquivos com o mesmo nome são sobrescritos no anterior. Se for fazer vários arquivos diferentes, trocar sempre nome na linha 51.

Passo a passo para a utilização do programa "flag.py":

1) Definir os termos de cada grupo. Na linha 17, inserir os termos do primeiro grupo e na linha 18, do segundo grupo. Manter o modelo de termos entre aspas simples e se o termo tiver mais de uma palavra, usar aspas duplas e aspas simples.

2)Linha 21: entre aspas duplas, inserir o nome de planilha com termos interseccionados obtida pelo programa “intersec-ord.py”.

	
