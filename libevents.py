
def validade_header(frame):
    if ((frame[0] == 64 and frame[13] == 64) or (frame[0] == 83 and frame[1] == 84 and frame [2] == 88)):
        return True
