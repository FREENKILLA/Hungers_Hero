import pygame
import sys
from pyvidplayer import Video

# Inicialización
pygame.init()
size = (1000, 575)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Hungers Hero")
pygame.display.set_icon(pygame.image.load("img/botones/logo.png"))
white = (255, 255, 255)
intro = Video("videos/Intro HH.mp4")
# Carga de imagen y sonido
sprite_sheet = pygame.image.load("img/fondos_pantalla/BGHH.png")
controls_image_english = pygame.image.load("img/fondos_pantalla/CONTROLS.png")
controls_image_spanish = pygame.image.load("img/fondos_pantalla/CONTROLES.png")
bg_music = pygame.mixer.Sound("sounds/main.wav")
seleccionar = pygame.mixer.Sound('sounds/Selec.wav')

frame_rects = []
for y in range(0, sprite_sheet.get_height(), 575):
    for x in range(0, sprite_sheet.get_width(), 1000):
        frame_rects.append(pygame.Rect(x, y, 1000, 575))

frame_index = 0
frame_speed = 3  # Ajusta la velocidad de la animación según tus necesidades
frame_countdown = frame_speed

# Estado de idioma actual y última vez que se hizo clic
current_language = "spanish"
last_click_time = 0

# Cadena de texto de idiomas
languages = {
    "inglish": {
        "play": "Play",
        "options": "Options",
        "controls": "Controls",
        "exit": "Exit",
        "spanish": "Spanish",
        "inglish": "Inglish",
        "sound": "Sound",
        "back": "Back",
        "lvl1": "Level 1",
        "lvl2": "Level 2",
        "lvl3": "Level 3"
    },
    "spanish": {
        "play": "Jugar",
        "options": "Opciones",
        "controls": "Controles",
        "exit": "Salir",
        "spanish": "Español",
        "inglish": "Ingles",
        "sound": "Sonido",
        "back": "Volver",
        "lvl1": "Nivel 1",
        "lvl2": "Nivel 2",
        "lvl3": "Nivel 3"
    }
}

# Estado de menú actual
menu_state = "main"

def start_game():
    print("Juego Iniciado")
    seleccionar.play()

def show_options():
    global menu_state
    print("Mostrando Opciones")
    menu_state = "options"
    seleccionar.play()

def show_controls():
    global menu_state
    print("Mostrando Controles")
    menu_state = "controls"
    seleccionar.play()

def go_back():
    global menu_state
    menu_state = "main"
    seleccionar.play()

def quit_game():
    pygame.quit()
    sys.exit()

def set_language(language):
    global current_language
    current_language = language
    seleccionar.play()

# Clase para los botones
class Button:
    def __init__(self, text, x, y, width, height, color, active_color, action=None):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.active_color = active_color
        self.action = action

    def draw(self, screen):
        global last_click_time
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if (self.x + self.width > mouse[0] > self.x and
            self.y + self.height > mouse[1] > self.y):
            pygame.draw.rect(screen, self.active_color, (self.x, self.y, self.width, self.height))

            current_time = pygame.time.get_ticks()
            if click[0] == 1 and current_time - last_click_time > 500 and self.action is not None:
                self.action()
                last_click_time = current_time
        else:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

        font = pygame.font.Font("fuentes/SFProDisplay-Black.ttf", 30)
        text = font.render(self.text, True, white)
        screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))


# Crear botones
main_buttons = [
    Button("Play", 700, 240, 275, 45, (0, 128, 0), (0, 255, 0), start_game),
    Button("Options", 700, 303, 275, 45, (0, 128, 128), (0, 255, 255), show_options),
    Button("Controls", 700, 366, 275, 45, (128, 0, 128), (255, 0, 255), show_controls),
    Button("Exit", 700, 429, 130, 45, (128, 0, 0), (255, 0, 0), quit_game)
]

option_buttons = [
    Button("Español", 700, 240, 275, 45, (0, 128, 0), (0, 255, 0), lambda: set_language("spanish")),
    Button("Inglish", 700, 303, 275, 45, (0, 128, 128), (0, 255, 255), lambda: set_language("inglish")),
    Button("Sound", 700, 366, 275, 45, (128, 0, 128), (255, 0, 255)),
    Button("Back", 700, 429, 130, 45, (128, 0, 0), (255, 0, 0), go_back)
]

controls_buttons = [
    Button("Back", 103, 23, 120, 45, (128, 0, 0), (255, 0, 0), go_back)  # Botón para regresar al menú principal
]
def play_intro():
    while True:
        intro.draw(screen, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                intro.close()
                pygame.mixer.stop()
                draw_menu()
                return  


music = [bg_music, seleccionar]
# Función para dibujar el menú
def draw_menu():
    pygame.mixer.Sound.play(bg_music, loops=-1)
    frame_index = 0
    frame_speed = 3  # Ajusta la velocidad de la animación según tus necesidades
    frame_countdown = frame_speed
    # Este es el bucle del menú
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Actualiza la animación
        frame_countdown -= 1
        if frame_countdown <= 0:
            frame_countdown = frame_speed
            frame_index = (frame_index + 1) % len(frame_rects)

        # Borra la pantalla
        screen.fill((0, 0, 0))

        # Dibuja el frame actual en la ventana
        current_frame = frame_rects[frame_index]
        screen.blit(sprite_sheet, (0, 0), current_frame)
        


        # Actualiza el texto de los botones de acuerdo al idioma actual
        for i, text_key in enumerate(["play", "options", "controls", "exit"]):
            main_buttons[i].text = languages[current_language][text_key]
        for i, text_key in enumerate(["spanish", "inglish", "sound", "back"]):
            option_buttons[i].text = languages[current_language][text_key]

        controls_buttons[0].text = languages[current_language]["back"]

        if menu_state == "main":
            for button in main_buttons:
                button.draw(screen)
        elif menu_state == "options":
            for button in option_buttons:
                button.draw(screen)
        elif menu_state == "controls":
            if current_language == "inglish":
                screen.blit(controls_image_english, (0, 0))
            else:
                screen.blit(controls_image_spanish, (0, 0))
            
            # Dibujar el botón para regresar
            for button in controls_buttons:
                button.draw(screen)

        pygame.display.flip()
        pygame.time.Clock().tick(60)

    pygame.quit()
    sys.exit()

# Llama a la función para mostrar el menú
play_intro()
pygame.mixer.Sound.play(bg_music, loops=-1)