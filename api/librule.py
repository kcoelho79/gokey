from apps.app.models import Resident

def isresident(serial):
	print("SERIAL ",serial)
	if (Resident.objects.get(serial=serial)):
		print("### esta no banco ###")
		return True
	else:
		return False