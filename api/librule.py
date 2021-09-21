#setup to use Django Models external python script 
# https://stackoverflow.com/questions/19475955/using-django-models-in-external-python-script
import os,sys
from django.conf import settings
import django
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()
##
from apps.app.models import Resident

def isresident(serial):
	print("SERIAL ",serial)
	if (Resident.objects.get(serial=serial)):
		print("### esta no banco ###")
		return True
	else:
		return False