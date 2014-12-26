from django.db import models
from django.contrib.auth.models import User
import sys    # sys.setdefaultencoding is cancelled by site.py
reload(sys)    # to re-enable sys.setdefaultencoding()
sys.setdefaultencoding('utf-8')
#rom django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class proyecto(models.Model):
	#proyectoKey= models.AutoField(primary_key=True)

	id_proyecto=models.AutoField(primary_key=True)
	titulo=models.CharField(max_length=200, db_column="nombre_proyecto")
	idUsuario=models.ForeignKey(User, db_column="fk_usuario")
	calificacion=models.IntegerField()
	fraseBusqueda= models.CharField(max_length=200, db_column="busqueda")

	def __unicode__(self):
		return self.titulo
