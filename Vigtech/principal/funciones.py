import scholar
import os
import json
def buscadorSimple(frase):
	
	querier=scholar.ScholarQuerier()
	
	settings=scholar.ScholarSettings()
	
	query=scholar.SearchScholarQuery()

	query.set_phrase(frase)
	query.set_num_page_results(40)

	querier.send_query(query)
	scholar.downloadArticles(querier)

	articles=querier.articles
	articulos=getArticlesDict(articles)
	#MOVER ARTICULOS A CARPETA TMP
	#if articulos is not None:
	#	moveFiles()
	#	indexarArchivos()
	return articulos
	
def buscadorAvanzado(frase,words, autor, after, before):
	querier=scholar.ScholarQuerier()
	settings=scholar.ScholarSettings()
	query=scholar.SearchScholarQuery()
	if frase != "":
		query.set_phrase(frase)
	if words != "":
		query.set_words(words)
	if autor != "":
		query.set_author(autor)
	if after !="" or before != "":
		query.set_timeframe(after, before)

	query.set_num_page_results(40)
	querier.send_query(query)
	
	articles=querier.articles
	scholar.downloadArticles(querier)

	articulos=getArticlesDict(articles)

	#if articulos is not None:
	#	moveFiles()
	#	indexarArchivos()
	return articulos

def getArticlesDict(articles):
	articulos=[]
	for art in articles:

		titulo=art.attrs["title"][0]
		#print(titulo)
		url=art.attrs["url"][0]
		url_pdf=art.attrs["url_pdf"][0]
		#state =art.attrs['state'][0]
		if url_pdf is not None:
			newArt={'titulo': titulo, 'url':url, 'url_pdf':url_pdf}
			print (newArt['titulo']+ '\n')
			articulos.append(newArt)
	return articulos

def moveFiles(nombreProyecto, user):
	rutaProyecto=str(user)+ "."+str(nombreProyecto) 
	items = os.listdir(os.getcwd())
	#os.listdir(os.getcwd())
	for files in items:
		if files.endswith(".pdf"):
			preName=str(files).replace(" ","\\ ")
			os.system("mv -f " + preName + " " + rutaProyecto+"/" )
	os.system("mv " + rutaProyecto+ "/" + " static/"+rutaProyecto+"/")
	
def indexarArchivos():
	ejecutar= "java -jar /home/administrador/OlayaVigtech/Indexador/Indexador.jar /home/administrador/OlayaVigtech/indices/ /home/administrador/archivos"
	print "Indexando..."
	os.system(ejecutar)
	print "Indexacion terminada..."

def CrearDirectorioProyecto(nombreProyecto, user):


	nombreDirectorio= str(user)+ "."+str(nombreProyecto) 
	os.system("mkdir " + nombreDirectorio)

def cambiarNombreDirectorio(nombreAnterior,nuevoNombre, user):
	nombreDirectorioAnterior= str(user)+ "."+str(nombreAnterior.replace(" ",""))
	nombreDirectorioNuevo= str(user)+ "."+str(nuevoNombre.replace(" ",""))

	os.system("mv" + nombreDirectorioAnterior+"/ " + nombreDirectorioNuevo+"/")

def busqueda (consulta):
	ruta_indeces= "Busquedas/asdIndices"
	ruta_json="Busquedas/"
	ruta_jar="Busquedas/dist/JSONConverter.jar"
	try:
		os.system("java -jar " +ruta_jar +" "+ consulta + " " + ruta_indeces+ " "+ruta_json)
		json_data=open(ruta_json+ "prueba.txt")
		data=json.load(json_data)

		return data
	except Exception, e:
		raise e
def crearListaDocumentos(id_proyecto, user):
	archivo= open("static/"+str(user)+"."+str(id_proyecto)+"/"+"docs.txt", "r")
	lista = []
	for linea in archivo:
		lista.append(linea.rstrip())
	return lista
	
def escribir_archivo_documentos(id_proyecto, user, articulosScholar, articulosScopus):
	lista=[]
	for art in articulosScholar:
		lista.append(art['titulo'] + ".pdf")
		
	lista = lista + articulosScopus
	pdfs = open("static/"+str(user)+"."+str(id_proyecto)+"/"+"docs.txt", "w")
	for pdf in lista:
		pdfs.write(pdf+'\n')
        
	
#buscadorSimple("Hello World")
#("","Named Entity Reo","", "","")

#import os
#for file in os.listdir("/mydir"):
#    if file.endswith(".txt"):
#        print(file)
