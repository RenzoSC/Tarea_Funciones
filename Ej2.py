"""Realiza una función que dependiendo de los parámetros que reciba: convierte a segundos o a horas:
Si recibe un argumento, supone que son segundos y convierte a horas, minutos y segundos. 
Si recibe 3 argumentos, supone que son hora, minutos y segundos y los convierte a segundos."""

def tiempo(segundos, minutos=0, horas=0):
    if horas !=0:
        segundos += minutos*60 + horas*3600
        print("El tiempo en segundos es: " + str(segundos))
    else:
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


