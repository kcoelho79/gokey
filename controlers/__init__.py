import controlers.mg3000

def get_controler(frame):
    if frame[6] <= 79:
        controler = mg3000.MG3000(frame)
        print("MG3000 encontrado")
    else:
        controler = "controladoraII"
        print("controladora II  encontrado")
    return controler
