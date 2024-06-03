import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Установка размеров окна
WIDTH, HEIGHT = 800, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра Виселица")

# Загрузка изображений для виселицы, поражения и выигрыша
hangman_images = [pygame.transform.scale(pygame.image.load(f"{i}.png"), (300, 300)) for i in range(1, 7)]
defeat_image = pygame.transform.scale(pygame.image.load("youlose.jpg"), (300, 300))
win_image = pygame.transform.scale(pygame.image.load("youwin.jpg"), (300, 300))

# Список слов
words = ["elif", "if", "print", "for", "whiletrue", "init", "int"]
word = random.choice(words).upper()  # Преобразуем слово в верхний регистр
guessed = []

# Шрифты для отображения
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
DIALOG_FONT = pygame.font.SysFont('comicsans', 30)

# Функция для отображения текста на экране
def draw(word, guessed):
    win.fill((255, 255, 255))

    # Отображение кнопок (букв)
    for i in range(26):
        x = 50 + (i % 13) * 50  # Измененные координаты X для букв
        y = 300 + (i // 13) * 50  # Измененные координаты Y для букв
        ltr = chr(65 + i)
        text = LETTER_FONT.render(ltr, 1, (0, 0, 0))
        pygame.draw.circle(win, (0, 0, 0), (x, y), 20, 3)
        win.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))

    # Проверка, угадано ли слово
    if all(letter in guessed for letter in word):
        win.blit(win_image, (250, HEIGHT - 400))  # Отображение изображения с надписью о выигрыше
        pygame.display.update()
        pygame.time.delay(2000)  # Задержка перед отображением диалогового окна
        show_dialog("Поздравляем! Вы выиграли!", ["Продолжить", "Закрыть"])

    else:
        # Отображение виселицы или изображения поражения
        wrong_guesses = len([g for g in guessed if g not in word])
        if wrong_guesses < len(hangman_images):
            win.blit(hangman_images[wrong_guesses], (250, HEIGHT - 400))  # Новые координаты для виселицы
        else:
            win.blit(defeat_image, (250, HEIGHT - 400))  # Отображение изображения поражения
            pygame.display.update()
            pygame.time.delay(2000)  # Задержка перед отображением диалогового окна
            show_dialog("Вы проиграли! Хотите продолжить?", ["Продолжить", "Закрыть"])

    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, (0, 0, 0))
    win.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT - 100))  # Новое поле для угаданных букв внизу

    pygame.display.update()

# Функция для отображения диалогового окна
def show_dialog(message, options):
    run_dialog = True
    dialog_font = pygame.font.SysFont('comicsans', 30)
    while run_dialog:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for i, option in enumerate(options):
                    option_text = dialog_font.render(option, 1, (0, 0, 0))
                    text_width, text_height = dialog_font.size(option)
                    button_rect = pygame.Rect(250, 400 + i * 50, text_width, text_height)
                    if button_rect.collidepoint(x, y):
                        if option == "Продолжить":
                            run_dialog = False
                            reset_game()
                        elif option == "Закрыть":
                            pygame.quit()
                            sys.exit()

        win.fill((255, 255, 255))
        pygame.draw.rect(win, (0, 0, 0), (200, 350, 400, 200), 3)
        text = dialog_font.render(message, 1, (0, 0, 0))
        win.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

        for i, option in enumerate(options):
            option_text = dialog_font.render(option, 1, (0, 0, 0))
            win.blit(option_text, (WIDTH // 2 - option_text.get_width() // 2, 400 + i * 50))

        pygame.display.update()

# Функция для сброса игры при продолжении
def reset_game():
    global word, guessed
    word = random.choice(words).upper()
    guessed = []

run = True
while run:
    draw(word, guessed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for i in range(26):
                letter_x = 50 + (i % 13) * 50
                letter_y = 300 + (i // 13) * 50
                if (letter_x - 20 <= x <= letter_x + 20) and (letter_y - 20 <= y <= letter_y + 20):
                                        letter = chr(65 + i)
                                        if letter not in guessed:
                                            guessed.append(letter)
                                            break

pygame.quit()
sys.exit()

