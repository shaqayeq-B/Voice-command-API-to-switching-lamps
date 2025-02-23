import pygame
import time

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Voice Command Test")

def control_device(command):
    if "light on" in command:
        screen.fill((255, 255, 0))  # زرد برای روشن شدن چراغ
        pygame.display.update()
        print("Light turned ON")
    elif "light off" in command:
        screen.fill((0, 0, 128))  # آبی برای خاموش شدن چراغ
        pygame.display.update()
        print("Light turned OFF")
    else:
        print("Command not recognized.")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # بررسی فایل دستور از Flask API
    try:
        with open("command.txt", "r") as f:
            command = f.read()
            if command:
                control_device(command)
                with open("command.txt", "w") as f_clear:
                    f_clear.write("")  # پس از اجرا، فایل را خالی می‌کنیم
    except FileNotFoundError:
        pass

    time.sleep(1)

pygame.quit()