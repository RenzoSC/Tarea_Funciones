"""Escribir dos funciones que permitan calcular: La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
La cantidad de horas, minutos y segundos de un tiempo dado en segundos."""

def cuantos_seg (horas, minutos=0, segundos=0):
    """Calcula el tiempo en segundos, recibe 3 argumentos: horas, minutos y segundos.
    Las horas son un argumento obligatorio"""
    tiempo = horas * 3600 + minutos*60 + segundos
    return tiempo

def tiempo_total (segundos = 0):
    """Calcula el tiempo en horas, minutos y segundos en base al argumento 'segundos'"""
    horas= segundos / 3600
    decimales_horas= segundos%3600
    if decimales_horas < 3600:
        horas = segundos//3600
        minutos = decimales_horas/60
        if decimales_horas % 60 < 60:
            minutos = decimales_horas//60
            segundos = decimales_horas % 60
        else:
            pass
    else:
        pass
    print ("El tiempo total es " + str(horas) + " : " + str(minutos) + " : " + str(segundos))

tiempo_total(3665)
print("La cantidad de segundos es: " + str(cuantos_seg(1,1,5)))