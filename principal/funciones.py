import scholar
import os
import json
def buscadorSimple(frase):
	#frase=input("Ingrese la frase a buscar: ")
	#print("Estoy buscando")
	querier=scholar.ScholarQuerier()
	#print ("Querier: "+str(querier))
	settings=scholar.ScholarSettings()
	#print ("Settings: "+str(settings))
	query=scholar.SearchScholarQuery()
	#print ("Query: " + str(query))

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
	rutaProyecto=str(user)+ "."+str(nombreProyecto.replace(" ","")) 
	items = os.listdir(os.getcwd())
	#os.listdir(os.getcwd())
	for files in items:
		if files.endswith(".pdf"):
			preName=str(files).replace(" ","\\ ")
#			newName='/home/administrador/archvios/'+preName
#			name=preName.split(" ")
#			final=name[0]+".pdf"
		#preName=art['titulo'] +".pdf"
		#newName='tmp/'+preName
#			os.rename(preName,newName)
#			print("mv  /home/administrador/Scholar/tmp/"+ preName +" /home/administrador/archivos")
			os.system("mv -f " + preName + " " + rutaProyecto+"/" )
			#os.system("mv -f /home/administrador/buscadorscholar/"+ preName +" /home/administrador/archivos")
			#os.system("mv  /home/administrador/Scholar/tmp/"+"\""+preName"\""+" /home/administrador/archivos")
	
def indexarArchivos():
	ejecutar= "java -jar /home/administrador/OlayaVigtech/Indexador/Indexador.jar /home/administrador/OlayaVigtech/indices/ /home/administrador/archivos"
	print "Indexando..."
	os.system(ejecutar)
	print "Indexacion terminada..."

def CrearDirectorioProyecto(nombreProyecto, user):


	nombreDirectorio= str(user)+ "."+str(nombreProyecto.replace(" ","")) 
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

#buscadorSimple("Hello World")
#("","Named Entity Reo","", "","")

#import os
#for file in os.listdir("/mydir"):
#    if file.endswith(".txt"):
#        print(file)
