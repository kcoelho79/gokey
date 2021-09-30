from apps.app.models import Resident


def isresident(serial):
	try:
		if (Resident.objects.get(serial=serial)):
			print("### esta no banco ###")
			return True
		else:
			return False
			print("### nao esta no bando tandera ###")
	except Resident.DoesNotExist:
		serial = None