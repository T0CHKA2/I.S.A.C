# This file is intended for testing various codes (from the Internet)
# and for the corresponding rewriting for the system "I.S.A.C."
import termcolor
import ctypes

kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

termcolor.cprint(f"{'-'*20}CREDIT{'-'*20}", "magenta", "on_cyan")
termcolor.cprint("Code by:                       T0CHKA", "white")
print()
termcolor.cprint("Voice lines:                   Reddit (Legit Mobile Cover User)", "white")
print()
termcolor.cprint("DLC Survival voice lines:      Demonikant", "white")
