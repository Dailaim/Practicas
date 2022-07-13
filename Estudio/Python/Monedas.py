

# FUNCIONES

def costo_servicio_video_streaming(tiempo_inicio_reproduccion,tiempo_fin_reproduccion):
    """
    Calcula el costo de un servicio de video streaming por demanda

    >>> costo_servicio_video_streaming(1,2)
    >>> 2000

    >>> costo_servicio_video_streaming(1,1)
    >>> 1000

    >>> costo_servicio_video_streaming(1,0)
    >>> 0

    """
    
    # Variables
    costo_servicio_video_streaming = 0
    tiempo_transcurrido_reproduccion = 0

    # Proceso
    tiempo_transcurrido_reproduccion = tiempo_fin_reproduccion - tiempo_inicio_reproduccion

    costo_servicio_video_streaming = tiempo_transcurrido_reproduccion * 2

    if costo_servicio_video_streaming < 1000:
        costo_servicio_video_streaming = 1000

    # Retorno
    return costo_servicio_video_streaming

# PROGRAMA PRINCIPAL

tiempo_inicio_reproduccion = int(input("Ingrese el tiempo de inicio de la reproduccion (hhmmss): "))
tiempo_fin_reproduccion = int(input("Ingrese el tiempo de fin de la reproduccion (hhmmss): "))
costo_servicio_video_streaming = costo_servicio_video_streaming(tiempo_inicio_reproduccion,tiempo_fin_reproduccion)
print(f"El costo del servicio de video streaming es de: ${costo_servicio_video_streaming}")