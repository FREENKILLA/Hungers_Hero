import pygame
import sys

def set_all_volume(sounds, mult):
    for sound in sounds:
        vol = sound.get_volume()
        sound.set_volume(min(vol * mult, 0.01))

# Inicialización
pygame.init()
size = (1000, 600) 
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Hungers Hero")
logo = pygame.image.load("img/principal/logo.png")
pygame.display.set_icon(logo)
white = (255, 255, 255)

# Carga de imagen y sonido
bg_image = pygame.image.load("img/principal/Background3.png")
bg_music = pygame.mixer.Sound("sounds/intro.mp3")

seleccionar = pygame.mixer.Sound('sounds/Selec.wav')

pygame.mixer.Sound.play(bg_music, loops=-1)
bg_image = pygame.image.load("img/principal/background3.png"). convert() #Convertir el formato de la imagen
bg_image = pygame.transform.scale(bg_image,(1000, 600))

music = [bg_music, seleccionar]
set_all_volume(music, 0.1)

# Estado de idioma actual y última vez que se hizo clic
current_language = "english"
last_click_time = 0

# Cadena de texto de idiomas
languages = {
    "english": {
        "play": "Play",
        "options": "Options",
        "controls": "Controls",
        "exit": "Exit",
        "spanish": "Spanish",
        "english": "English",
        "back": "Back"
    },
    "spanish": {
        "play": "Jugar",
        "options": "Opciones",
        "controls": "Controles",
        "exit": "Salir",
        "spanish": "Español",
        "english": "Inglés",
        "back": "Regresar"
    }
}

# Estado de menú actual
menu_state = "main"

# Acciones para los botones
def start_game():
    print("Juego Iniciado")
    seleccionar.play()

def show_options():
    global menu_state
    print("Mostrando Opciones")
    menu_state = "options"
    seleccionar.play()

def show_controls():
    print("Mostrando Controles")
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

        if (self.x+self.width > mouse[0] > self.x and
            self.y+self.height > mouse[1] > self.y):
            pygame.draw.rect(screen, self.active_color, (self.x, self.y, self.width, self.height))

            current_time = pygame.time.get_ticks()
            if click[0] == 1 and current_time - last_click_time > 500 and self.action is not None:
                self.action()
                last_click_time = current_time
        else:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

        font = pygame.font.SysFont("fuentes/minecraft.ttf", 30)
        text = font.render(self.text, True, white)
        screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

# Crear botones
main_buttons = [
    Button("Play", 400, 260, 200, 50, (0, 128, 0), (0, 255, 0), start_game),
    Button("Options", 400, 320, 200, 50, (0, 128, 128), (0, 255, 255), show_options),
    Button("Controls", 400, 380, 200, 50, (128, 0, 128), (255, 0, 255), show_controls),
    Button("Exit", 400, 440, 200, 50, (128, 0, 0), (255, 0, 0), quit_game)
]

option_buttons = [
    Button("Español", 400, 200, 200, 50, (0, 128, 0), (0, 255, 0), lambda: set_language("spanish")),
    Button("English", 400, 260, 200, 50, (0, 128, 128), (0, 255, 255), lambda: set_language("english")),
    Button("Back", 400, 320, 200, 50, (128, 0, 0), (255, 0, 0), go_back)  # Modificación aquí
]

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg_image, (0, 0))

    # Actualiza el texto de los botones de acuerdo al idioma actual
    for i, text_key in enumerate(["play", "options", "controls", "exit"]):
        main_buttons[i].text = languages[current_language][text_key]
    for i, text_key in enumerate(["spanish", "english", "back"]):
        option_buttons[i].text = languages[current_language][text_key]

    if menu_state == "main":
        for button in main_buttons:
            button.draw(screen)
    elif menu_state == "options":
        for button in option_buttons:
            button.draw(screen)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
