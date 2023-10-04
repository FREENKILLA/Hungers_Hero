import pygame
import cv2
from pygame.locals import QUIT

# Función que redimensiona una imagen manteniendo la relación de aspecto original.
def redimensionar_mantener_aspecto(src, ancho_objetivo, alto_objetivo):
    relacion_aspecto = src.shape[1] / src.shape[0]
    if ancho_objetivo / alto_objetivo < relacion_aspecto:
        w = ancho_objetivo
        h = int(w / relacion_aspecto)
    else:
        h = alto_objetivo
        w = int(h * relacion_aspecto)
    return cv2.resize(src, (w, h))

# Inicializa la biblioteca pygame.
pygame.init()

# Establece las dimensiones de la ventana.
ANCHO, ALTO = 1280, 720
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Hungers Hero')

# Carga un video usando OpenCV.
cap = cv2.VideoCapture('img/VideosFondo/portada3.mp4')

# Define colores para su uso posterior.
MORADO = (120, 67, 230)
VERDE = (0, 255, 0)

# Configura una fuente para su uso en la interfaz.
ruta_fuente = "fuentes/Anton-Regular.ttf"
fuente = pygame.font.Font(ruta_fuente, 50)

# Función para dibujar botones con interactividad.
def dibujar_boton(texto, x, y, pos_mouse):
    color = MORADO
    superficie_texto = fuente.render(texto, True, color)
    rectangulo_texto = superficie_texto.get_rect(center=(x, y))
    
    # Cambia el color del botón si el mouse pasa sobre él.
    if rectangulo_texto.collidepoint(pos_mouse):
        superficie_texto = fuente.render(texto, True, VERDE)

    pantalla.blit(superficie_texto, rectangulo_texto)
    return rectangulo_texto

# Inicia el bucle principal del juego.
ejecutando = True
reloj = pygame.time.Clock()

while ejecutando:
    ret, fotograma = cap.read()
    if not ret:
        # Reinicia el video cuando se termina.
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret, fotograma = cap.read()

    # Convierte el fotograma a formato RGB y redimensiona.
    fotograma = cv2.cvtColor(fotograma, cv2.COLOR_BGR2RGB)
    fotograma = redimensionar_mantener_aspecto(fotograma, ANCHO, ALTO)
    imagen_video_string = fotograma.tostring()
    superficie_video = pygame.image.fromstring(imagen_video_string, fotograma.shape[1::-1], 'RGB')
    
    # Dibuja el fotograma en la pantalla.
    pantalla.fill((0, 0, 0))
    desplazamiento_x = (ANCHO - fotograma.shape[1]) // 2
    desplazamiento_y = (ALTO - fotograma.shape[0]) // 2
    pantalla.blit(superficie_video, (desplazamiento_x, desplazamiento_y))

    # Manejo de eventos.
    pos_mouse = pygame.mouse.get_pos()
    for evento in pygame.event.get():
        if evento.type == QUIT:
            ejecutando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # Detecta clics en los botones.
            if boton_reproducir.collidepoint(pos_mouse):
                print("¡Español clickeado!")
            elif boton_informacion.collidepoint(pos_mouse):
                print("¡Ingles clickeada!")

    # Dibuja los botones.
    boton_reproducir = dibujar_boton('Español', ANCHO/2, ALTO/2 - 30, pos_mouse)
    boton_informacion = dibujar_boton('Ingles', ANCHO/2, ALTO/2 + 30, pos_mouse)

    pygame.display.flip()
    reloj.tick(30)

# Libera los recursos y cierra pygame al salir.
pygame.mixer.music.stop()
cap.release()
pygame.quit()
