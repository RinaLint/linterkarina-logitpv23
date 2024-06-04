import pygame
import random
import sys

#инициализация Pygame и его музыкального модуля
pygame.init()
#pygame.mixer.init()

#размеры окна игры и его заголовка
WIDTH, HEIGHT = 800, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра Виселица")

#изображения виселицы
hangman_images = [pygame.transform.scale(pygame.image.load(f"{i}.png"), (300, 300)) for i in range(1, 7)]
defeat_image = pygame.transform.scale(pygame.image.load("youlose.jpg"), (300, 300))
win_image = pygame.transform.scale(pygame.image.load("youwin.jpg"), (300, 300))

#звук
#win_sound = pygame.mixer.Sound("win_sound.wav")
#lose_sound = pygame.mixer.Sound("lose_sound.wav")

#слова и выбор
words = ["elif", "if", "print", "for", "whiletrue", "init", "int", "import", "else", "delete", "pop", "remove"]
word = random.choice(words).upper()
guessed = []

#шрифты
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
DIALOG_FONT = pygame.font.SysFont('comicsans', 30)

#функция для отрисовки игрового экрана
def draw(word, guessed):
    #заполнение экрана белым цветом
    win.fill((255, 255, 255))

    #отрисовка букв алфавита и кружков вокруг них
    for i in range(26):
        x = 50 + (i % 13) * 50
        y = 300 + (i // 13) * 50
        ltr = chr(65 + i)
        if ltr in guessed:
            color = (0, 255, 0) if ltr in word else (255, 0, 0)
        else:
            color = (0, 0, 0)
        text=LETTER_FONT.render(ltr, 1, color)
        pygame.draw.circle(win, color, (x, y), 20, 3)
        win.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))

    #подсчет количества неправильных попыток
    wrong_guesses = len([g for g in guessed if g not in word])
    
    #отображение изображения виселицы в зависимости от количества ошибок
    if wrong_guesses < len(hangman_images):
        win.blit(hangman_images[wrong_guesses], (250, HEIGHT - 400))
    else:
        #если ошибок больше допустимого количества, отображение изображения поражения и проигрыша
        win.blit(hangman_images[-1], (250, HEIGHT - 400))
        pygame.display.update()
        pygame.time.delay(1000)
        win.blit(defeat_image, (250, HEIGHT - 400))
        #pygame.mixer.Sound.play(lose_sound)
        pygame.display.update()
        pygame.time.delay(2000)
        show_dialog("You lose! Do you want to continue?", ["Continue", "Close"])
        return

    #проверка, угаданы ли все буквы в слове
    if all(letter in guessed for letter in word):
        win.blit(win_image, (250, HEIGHT - 400))
        #pygame.mixer.Sound.play(win_sound)
        pygame.display.update()
        pygame.time.delay(2000)
        show_dialog("Congratulations! You win!", ["Continue", "Close"])
        return

    #отображение загаданного слова с угаданными буквами и пропусками
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, (0, 0, 0))
    win.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT - 100))

    pygame.display.update()

#функция для отображения диалогового окна после завершения игры
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
                    button_rect = pygame.Rect(WIDTH // 2 - text_width // 2, 450 + i * 50, text_width, text_height)
                    if button_rect.collidepoint(x, y):
                        if option == "Continue":
                            run_dialog = False
                            reset_game()
                        elif option == "Close":
                            pygame.quit()
                            sys.exit()

        #диалоговое окно
        win.fill((255, 255, 255))
        pygame.draw.rect(win, (0, 0, 0), (150, 250, 500, 300), 3)
        text = dialog_font.render(message, 1, (0, 0, 0))
        win.blit(text, (WIDTH // 2 - text.get_width() // 2, 300))

        for i, option in enumerate(options):
            option_text = dialog_font.render(option, 1, (0, 0, 0))
            win.blit(option_text, (WIDTH // 2 - option_text.get_width() // 2, 450 + i * 50))

        pygame.display.update()

#следующий уровень
def reset_game():
    global word, guessed
    word = random.choice(words).upper()
    guessed = []

#главный цикл игры
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

#завершение
pygame.quit()
sys.exit()
