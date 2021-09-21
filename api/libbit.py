
def serial_to_hex(serial):
    s1, s2 = serial.split('-')  # separa o prefixo 2 algarismo e o  sufixo 4 algarismo do serial
    s1 = int(s1).to_bytes(1, 'big')  # converte inteiro para byte
    s2 = int(s2).to_bytes(2, 'big')
    serial = b'\x00\x00' + s1 + s2
    return serial

def serial_to_strhex(serial):
    s1, s2 = serial.split('-')  # separa o prefixo 2 algarismo e o  sufixo 4 algarismo do serial
    s1 = int(s1).to_bytes(1, 'big')  # converte inteiro para byte
    s2 = int(s2).to_bytes(2, 'big')
    serial = b'\x00\x00' + s1 + s2
    return fmtByte_to_Str(serial)

def get_address(payload):
    address = message[-6:]
    #host = BitHandler.fmtByte_to_Str(address[0:4],'.')
    host = str(address[0]) +'.'+ str(address[1]) +'.'+ str(address[2]) +'.'+ str(address[3])
    port = int.from_bytes(address[4:], 'big')
    return ((host,port))

def calcula_checksum(frame):
    # calcula checksum
    cs = 0
    for i in range(len(frame)):
        cs = cs + frame[i]
    cs = cs & 0xff0 >> 4
    return cs

def bit_from_string(string, index, msb= False ):
       i, j = divmod(index, 8)
      # print(i,j)

       # msb (most significant bit) if true set the high-order bit first
       if msb:
           j = 8 - j

       if ord(string[i]) & (1 << j):
              return 1
       else:
              return 0

def Byte_to_Hex(frame):
    tamanho = len(frame)
    frameHex= []
    for i in range(tamanho):
        frameHex.append(hex(frame[i]))
    return frameHex

def fmtByte_to_Str(byte,separador=''):
    # formata Byte para  Str
    tamanho = len(byte)
    fstr= ''
    for i in range(tamanho):
        fstr += hex(byte[i])[2:].zfill(2) + separador
    return fstr


def Hex_to_Bin(hexnumber, num_of_bits=8):
    base=16
    return bin(int(hexnumber,base))[2:].zfill(num_of_bits)

def bcd2int(bcd):
    digit=0
    ret=0

    digit = (bcd >> 4) & 0x0F
    ret = ret * 10 + digit;

    digit = bcd & 0x0F
    ret = ret * 10 + digit
    return ret

def tobit(numero,msb,lsb):
    #recebe int e tranforma em bits

    bits = bin(numero)[2:].zfill(8)
    print(bits)
    #converte o index 0 para msb (inverte)
    istart = 7 - msb
    iend = (7 - lsb) + 1
    print(bits[istart:iend])
    return bits[istart:iend]

def onebit(b,i,ordem='crescente'):
    bits = bin(b)[2:].zfill(8)
    if ordem =='crescente':
        return int(bits[i],2)
    elif ordem == 'decrescente':
        invertida = 7 - i
        return int(bits[invertida],2)

def bits2int(b, msb, lsb):
    #Extrai o range de bits (entre 7 e 0) de um determinado byte, retorna valor decimal
    #msb = Bit +significativo Bit inicio range, 
    #lsb = Bit -significativo Bit fim range

    bits = bin(b)[2:].zfill(8)  # transforma 1 byte em 8 bits

    if (msb < 8) and (lsb <8):
        if (msb <= lsb): # tipo little 
            return int(bits[msb:lsb+1],2)

        elif (msb >= lsb): # tipo Big
            #inverte o index para o tipo big MSB esquerda para direita
            msb = 7 - msb
            lsb = 7 - lsb
            return int(bits[msb:lsb+1],2)
    else:
        return 'erro'