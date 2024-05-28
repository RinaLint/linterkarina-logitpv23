import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Установка размеров окна
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра Виселица")

# Загрузка и изменение размеров изображений для виселицы
images = [pygame.transform.scale(pygame.image.load(str(i) + ".png"), (300, 300)) for i in range(1, 7)]

# Список слов
words = ["автомобиль", "компьютер", "программирование", "python", "виселица", "игра", "разработка"]
word = random.choice(words)
guessed = []

# Шрифт для отображения слова
LETTER_FONT = pygame.font.SysFont('comicsans', 40)

# Функция для отображения текста на экране
def draw(word, guessed):
    win.fill((255, 255, 255))
    # Отображение слова
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = LETTER_FONT.render(display_word, 1, (0, 0, 0))
    win.blit(text, (400, 200))
    # Отображение виселицы
    if len(guessed) < len(images):
        win.blit(images[len(guessed)], (50, 100))
    # Отображение кнопок (букв)
    for i in range(26):
        x = 400 + i % 13 * 50
        y = 350 + i // 13 * 50
        ltr = chr(65 + i)
        text = LETTER_FONT.render(ltr, 1, (0, 0, 0))
        pygame.draw.circle(win, (0, 0, 0), (x, y), 20, 3)
        win.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))
    pygame.display.update()

# Основной игровой цикл
run = True
while run:
    draw(word, guessed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if 350 <= y <= 450:
                letter = chr(65 + (x - 400) // 50)
                guessed.append(letter)
                if letter not in word:
                    if len(guessed) == len(images) - 1:
                        pygame.time.delay(1000)
                        run = False

pygame.quit()
sys.exit()
