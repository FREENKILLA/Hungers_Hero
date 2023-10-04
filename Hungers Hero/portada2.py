import pygame
import cv2
from pygame.locals import QUIT

# Función para redimensionar la imagen manteniendo la relación de aspecto
def redimensionar_mantener_aspecto(src, ancho_objetivo, alto_objetivo):
    relacion_aspecto = src.shape[1] / src.shape[0]
    if ancho_objetivo / alto_objetivo < relacion_aspecto:
        w = ancho_objetivo
        h = int(w / relacion_aspecto)
    else:
        h = alto_objetivo
        w = int(h * relacion_aspecto)
    return cv2.resize(src, (w, h))

# Inicialización de pygame
pygame.init()

# Configuración de la ventana
ANCHO, ALTO = 1280, 720
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Hungers Hero')

# Configuración de OpenCV para cargar un video
cap = cv2.VideoCapture('img/VideosFondo/portada2.mp4')

# Definición de colores
MORADO = (120, 67, 230)
VERDE = (0, 255, 0)

# Configuración de la fuente
ruta_fuente = "fuentes/Anton-Regular.ttf"
fuente = pygame.font.Font(ruta_fuente, 50)

# Función para dibujar botones en la pantalla
def dibujar_boton(texto, x, y, pos_mouse):
    color = MORADO
    superficie_texto = fuente.render(texto, True, color)
    rectangulo_texto = superficie_texto.get_rect(center=(x, y))
    
    if rectangulo_texto.collidepoint(pos_mouse):
        superficie_texto = fuente.render(texto, True, VERDE)

    pantalla.blit(superficie_texto, rectangulo_texto)
    return rectangulo_texto

# Bucle principal del juego
ejecutando = True
reloj = pygame.time.Clock()

while ejecutando:
    ret, fotograma = cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret, fotograma = cap.read()

    # Convertir colores y redimensionar el fotograma
    fotograma = cv2.cvtColor(fotograma, cv2.COLOR_BGR2RGB)
    fotograma = redimensionar_mantener_aspecto(fotograma, ANCHO, ALTO)

    imagen_video_string = fotograma.tostring()
    superficie_video = pygame.image.fromstring(imagen_video_string, fotograma.shape[1::-1], 'RGB')
    
    # Dibujar fotograma en la pantalla
    pantalla.fill((0, 0, 0))
    desplazamiento_x = (ANCHO - fotograma.shape[1]) // 2
    desplazamiento_y = (ALTO - fotograma.shape[0]) // 2
    pantalla.blit(superficie_video, (desplazamiento_x, desplazamiento_y))

    # Manejo de eventos
    pos_mouse = pygame.mouse.get_pos()
    for evento in pygame.event.get():
        if evento.type == QUIT:
            ejecutando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_dificil.collidepoint(pos_mouse):
                print("¡DIFICIL clickeado!")
            elif boton_facil.collidepoint(pos_mouse):
                print("¡FACIL clickeada!")

    # Dibujar botones
    boton_dificil = dibujar_boton('DIFICIL', ANCHO/2, ALTO/2 - 30, pos_mouse)
    boton_facil = dibujar_boton('FACIL', ANCHO/2, ALTO/2 + 30, pos_mouse)

    pygame.display.flip()
    reloj.tick(30)

# Limpiar recursos cuando se cierra el juego
pygame.mixer.music.stop()
cap.release()
pygame.quit()
