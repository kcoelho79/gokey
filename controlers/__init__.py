import controlers.mg3000
import controlers.control2

def discover(frame):
    if frame[6] <= 79:
        controler = mg3000.MG3000(frame)
        print("MG3000 encontrado")
    else:
        controler = control2.CONTROL2(frame)
        print("controladora II  encontrado")
    return controler
