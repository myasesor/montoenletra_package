import math

def numeroaletra(valor):
    '''
    * Funcion que retorna en letras cualquier valor enviado en un rango de 1 a 9 billones
    * Autor - Roger Jose Retamoza Campo
    * Fecha - Noviembre 10 de 2022
    * Lugar - Barranquilla Colombia Sur America
    * Uso numeroaletra(92514072)
    # >>> type(numeroaletra()) == type(list())
    '''
    if valor==0:
        retun = ""
    elif valor==1:
        retun = "UN"
    elif valor==2:
        retun = "DOS"
    elif valor==3:
        retun = "TRES"
    elif valor==4:
        retun = "CUATRO"
    elif valor==5:
        retun = "CINCO"
    elif valor==6:
        retun = "SEIS"
    elif valor==7:
        retun = "SIETE"
    elif valor==8:
        retun = "OCHO"
    elif valor==9:
        retun = "NUEVE"
    elif valor==10:
        retun = "DIEZ"
    elif valor==11:
        retun = "ONCE"
    elif valor==12:
        retun = "DOCE"
    elif valor==13:
        retun = "TRECE"
    elif valor==14:
        retun = "CATORCE"
    elif valor==15:
        retun = "QUINCE"
    elif valor in [16,17,18,19]:
        retun = "DIECI" + numeroaletra(valor - 10)
    elif valor==20:
        retun = "VEINTE"
    elif valor in [21,22,23,24,25,26,27,28,29]:
        retun = "VEINTI" + numeroaletra(valor - 20)
    elif valor==30:
        retun = "TREINTA"
    elif valor==40:
        retun = "CUARENTA"
    elif valor==50:
        retun = "CINCUENTA"
    elif valor==60:
        retun = "SESENTA"
    elif valor==70:
        retun = "SETENTA"
    elif valor==80:
        retun = "OCHENTA"
    elif valor==90:
        retun = "NOVENTA"
    elif valor==100:
        retun = "CIEN"
    elif valor in [200,300,400,600,800]:
        retun = numeroaletra((math.trunc(valor/100))) + "CIENTOS"
    elif valor==500:
        retun = "QUINIENTOS"
    elif valor==700:
        retun = "SETECIENTOS"
    elif valor==900:
        retun = "NOVECIENTOS"
    elif valor==1000:
        retun = "MIL"
    elif valor==1000000:
        retun = 'UN MILLON DE'
    elif valor < 100:
        retun = numeroaletra( (math.trunc(valor / 10) * 10) ) + " Y " + numeroaletra(valor % 10)
    elif valor < 200:
        retun = "CIENTO " + numeroaletra(valor - 100)
    elif valor < 1000:
        retun = numeroaletra((math.trunc(valor / 100) * 100)) + " " + numeroaletra(valor % 100)
    elif valor < 2000:
        retun = "MIL " + numeroaletra(valor % 1000)
    elif (valor < 1000000):
        retun=numeroaletra((math.trunc(valor / 1000)))+" MIL"
        if (valor % 1000 < 1000):
            retun = retun + " " + numeroaletra(valor % 1000)
    elif valor < 2000000:
        retun = "UN MILLON " + numeroaletra(valor % 1000000)
    elif (valor < 1000000000000.0):
        retun = numeroaletra((math.trunc(valor / 1000000))) + " MILLONES "
        if ((valor-(math.trunc(valor / 1000000) * 1000000))<1000000 and (valor-(math.trunc(valor / 1000000) * 1000000)) != 0):
            retun = retun + numeroaletra(valor - (math.trunc(valor / 1000000) * 1000000))
        else:
            retun = retun + "DE"
    elif (valor==1000000000000.0):
        retun = "UN BILLON DE"
    elif (valor<2000000000000.0):
        retun = "UN BILLON " + numeroaletra(valor-(math.trunc(valor/1000000000000.0)*1000000000000.0))
    else:
        retun=numeroaletra((math.trunc(valor/1000000000000.0)))+" BILLONES "
        if (valor - (math.trunc(valor/1000000000000.0)*1000000000000.0) < 1000000000000.0 and valor-(math.trunc(valor/1000000000000.0)*1000000000000.0) != 0):
            retun = retun + numeroaletra(valor-(math.trunc(valor/1000000000000.0)*1000000000000.0))
        else:
            retun = retun + "DE"
    return retun
