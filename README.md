# "I.S.A.C."
#### "I.S.A.C." - "Intelligent System Analytic Computer"
![ISAC](https://preview.redd.it/1ejpa2nuwyj21.jpg?width=1280&format=pjpg&auto=webp&s=4ca7c246d1a0f85af64ccb9f636e8415ba321f24)

"I.S.A.C." - "Intelligent System Analytic Computer" from the "Tom Clancy's The Division",
This voice assistant should be a copy of "I.S.A.C." from the game "Tom Clancy's The Division".
It will be based on the Raspberry Pi 3 and mainly from Adafruit components such as DHT22 and Ultimate GPS.
At the moment, the sound output system is implemented through the PyGame module.
It works, but it is useless and will remain until the "voice assistant brains" are made.
There is also an alarm clock, and a library of voice lines (which is implemented through a .py file (because I'm dumb :D)).

---

## Main functionality

The main and exclusive functionality will be that it will be completely autonomous in the sense that it can be taken
anywhere because of the battery, as well as exclusivity in that it will have a temperature sensor that will receive the
temperature in real time around it and will talk about whether the temperature has risen or has dropped (The output will
be implemented through the ISAC voice lines from the DLC Survival). It will also have a Combat mode (in which all
information will be displayed in a summary) and an emergency mode that will tell you how to do First Aid, call 911
(Or 112 for Russia) with a pre-recorded message and transmit your location using a GPS sensor. Into the GPS account.
When you leave any building, I.S.A.C will tell you that you are leaving the safe zone, and when you enter the metro or
at the entrance to the shopping center (you will have to mark the shopping center yourself), he will tell you that you
are entering a dark zone. More, probably, nothing new will be and standard commands of voice assistants (such as Alexa
or Alice) will be implemented.

---

## Parts

#### - Adafruit DHT22 Temperature Sensor
The DHT22 sensor will be used to monitor the temperature around itself in real time (every 5 to 10 minutes).

![AdafruitDHT22](https://i.ibb.co/26qtpD8/DOC004553860.jpg)
#### - Raspberry Pi 3
Raspberry Pi 3 will be the core of the entire system (Logic) through which everything will work

![RaspberryPi3](https://i.ibb.co/0Bph7DL/877fb653-7b43-4931-9cee-977a22571f65-3b-Angle-2-refresh.jpg)
#### - Adafruit Ultimate GPS

Through this sensor, data will be transmitted to 911 in emergency mode, as well as the voice assistant will say that you entered the safe zone, left it, etc.

![AdafruitUltimateGPS](https://i.ibb.co/19k27WR/746-11.jpg)
#### - ReSpeaker 4-Mic Array for Raspberry Pi
Absolutely the entire voice assistant will work through ReSpeaker, and the I.S.A.C. color will also be displayed. Nothing will work without it.

![ReSpeaker4-Mic](https://i.ibb.co/hF1jV2w/762071839-w600-h600-762071839.jpg)

*P.S. More parts will be included soon.*

### Credit

---
Code by: **[T0CHKA](https://twitter.com/t0chka2020)**

Voice lines by: Reddit ([**Legit Mobile Cover User**](https://www.reddit.com/r/thedivision/comments/4dco39/all_isac_voice_lines_all_languages/))

Survivor DLC Voice lines by: **[Demonikant]()**

Translated by:  Google (Lol yea, im very bad in english so sorry if something will sayed bad)
