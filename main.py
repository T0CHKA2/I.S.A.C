import Adafruit_DHT  # Sensor module
import datetime
import time
# import random
import voice_var
import pygame
from termcolor import cprint
import ctypes

kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
now = datetime.datetime.now()
dht22_sensor = Adafruit_DHT.DHT22
humidity, temperature = Adafruit_DHT.read_retry(dht22_sensor, 26)
battle_mode = False  # I don't know what it will be, but something great it will be
emergency_mode = False
# The emergency mode will give you brief information, tell you what to do with the patient and
# possibly call 911 (For Ru - 112) and say a pre-recorded message
# (it will be built into the function). I don't know yet how it will be implemented,
# but I know that it is possible.

pygame.init()
cprint(f"{'-'*20}CREDIT{'-'*20}", "magenta", "on_cyan")
cprint("Code by:                       T0CHKA", "white")
print()
cprint("Voice lines:                   Reddit (Legit Mobile Cover User)", "white")
print()
cprint("DLC Survival voice lines:      Demonikant", "white")
isac_on_ready = pygame.mixer.Sound(voice_var.ISAC_Ready)
isac_on_ready.play()
time.sleep(1.68)  # On ready playing sound
pygame.quit()


if battle_mode is False:
    if -10 < temperature:
        pygame.init()
        isac_t_low = pygame.mixer.Sound(voice_var.isac_low_cold)
        isac_t_low.play()  # -10C
        pygame.quit()
    elif -20 < temperature:
        pygame.init()
        isac_t_medium = pygame.mixer.Sound(voice_var.isac_medium_cold)
        isac_t_medium.play()  # -20C
        pygame.quit()
    elif -30 < temperature:
        pygame.init()
        isac_t_v_low = pygame.mixer.Sound(voice_var.isac_high_cold)
        isac_t_v_low.play()  # -30C
        pygame.quit()
    else:
        pass
else:
    if temperature > -5:
        pygame.init()
        isac_t_b_normal = pygame.mixer.Sound(voice_var.isac_t_b_normal)
        isac_t_b_normal.play()  # -5C - +20C
        pygame.quit()
    elif temperature < -5:
        pygame.init()
        isac_t_b_cold = pygame.mixer.Sound(voice_var.isac_t_b_cold)
        isac_t_b_cold.play()  # -40C - -5C
        pygame.quit()
    elif temperature > 20:
        pygame.init()
        isac_t_b_hot = pygame.mixer.Sound(voice_var.isac_t_b_hot)
        isac_t_b_hot.play()  # +20C - +40C
        pygame.quit()
        #  Yes, I am aware that this kind of code writing can greatly worsen the work of I.S.A.C.
        #  I will deal with this code. When? I have no idea, when I will learn to do all this more optimized maybe.
        #  What is this? This is the temperature department. Its main task is to measure the temperature around itself
        #  every 5 - 10 minutes. So far, it is only 50% done.

# if now == "07:00:00":
#    pygame.init()
#    alarm = pygame.mixer.Sound(voice_var.alarm_clock)
#    alarm.play()
#    while pygame.mixer.music.get_busy():
#        continue
#    pygame.quit()
# else:
#    pass
# This feature is still under development. It will be an alarm clock
