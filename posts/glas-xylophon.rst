.. title: Glas Xylophon
.. slug: glas-xylophon
.. date: 2021-12-22 14:35:02 UTC+01:00
.. tags: mikrocontroller, arduino, programmieren, atmel, mega32u4, musik
.. category: basteln
.. link: 
.. description: 
.. type: text

.. |ss| raw:: html

   <strike>

.. |se| raw:: html

   </strike>

.. figure:: /images/glasxylo06.thumbnail.png
   :align: center
   :alt: Bild vom Glas-Xylophon
   
   Bild vom Glas-Xylophon

Inspiriert durch den Hackaday Artikel `Arduino plays the glasses
<https://hackaday.com/blog/?s=arduino+glasses>`_ habe ich beschlossen, in der
Vorweihnachtszeit ebenfalls ein Glas-Xylophon zu bauen. Ich verwende insgesamt
12 Weingläser und die Schlägel sind Holzperlen an Metallstäben, die von
einfachen Modellbau-Servos angetrieben werden. Das Herzstück ist ein `Sparkfun
Pro Micro <https://www.sparkfun.com/products/12640/>`_ mit einem Atmel MEGA32u4
Microcontroller. Der MEGA32u4 hat einen integrierten USB2.0-Controller, so dass
der Mikrocontroller von einem Betriebssystem als USB MIDI-Gerät erkannt werden
kann. Alles ist auf einer 80 x 30 cm Regalbodenplatte angeordnet. Für einen
zusätzlichen visuellen Effekt können die einzelnen Gläser von unten mit jeweils
einer programmierbaren RGB-LED (`WS2812b
<https://www.circuitgeeks.com/ws2812b-addressable-rgb-led-strip-with-arduino/>`_)
angesteuert werden.

.. TEASER_END

.. figure:: /images/glasxylo02.thumbnail.jpg
   :align: center
   :alt: Platine mit Miktrocontroller für das Glas-Xylophon

   Platine mit Miktrocontroller für das Glas-Xylophon

Die Pro Micro Microcontroller haben sich beim Programmieren jedoch als etwas
"zickig" herausgestellt. Das Programmieren über die USB-Schnittstelle aus der
Arduino IDE heraus war sehr unzuverlässig. Am Ende habe ich die AVR
ISP-Schnittstelle verwendet und als Programmiergerät kam einfach ein Arduino Uno
zum Einsatz, auf den ich vorher die ArduinoISP Firmware aufgespielt habe. Eine
gute Beschreibung dazu findet man `hier auf der Arduino-Webseite
<https://www.arduino.cc/en/pmwiki.php?n=Tutorial/ArduinoISP">`_. |ss| Trotzdem
blieb ein Problem: Mein Programm auf den Microcontroller scheint nicht allein zu
starten. Ich muss erst eine serielle Verbindung vom Computer zum Mikrocontroller
aufbauen, dann läuft es los. Warum das so ist, verstehe ich nicht. |se| [Update
2021/12/23: Kein Wunder, wenn man hinter dem ``Serial.begin()`` ein
``while(!Serial)`` stehen hat ...].

.. figure:: /images/glasxylo04.thumbnail.jpg
   :align: center
   :alt: Die Schlägel des Glas-Xylophons sind Metallstäbe mit Holzkugeln als    Köpfe, die von Servos angetrieben werden.

   Die Schlägel des Glas-Xylophons sind Metallstäbe mit Holzkugeln als Köpfe, die von Servos angetrieben werden.

Mit der `USB-MIDI Arduino-Bibliothek
<https://github.com/lathoub/Arduino-USBMIDI>`_ ist der Pro Micro im Handumdrehen
in ein USB MIDI-Gerät (MIDI: Musical Instrument Digital Interface) verwandelt,
welches MIDI-Kommandos (bspw. zum Spielen bestimmter Noten) empfangen kann. Die
von den Servos angetriebenen Schlägel sind in der Software des Pro Micro
einfach bestimmten Noten zugeordnet. Jedes MIDI ``NoteOn``-Kommando für einen
bestimmten Notenbereich (12 Noten, so viele wie Gläser bzw. Servos) triggert,
dass das jeweilige Servo den Schlägel an das Glas schlägt und anschließend
wieder in die Ausgangsposition zurückfährt. Ich habe die kleinen, schwachen 9g
Modellbauservos genommen, die sehr günstig zu bekommen, nicht sehr laut und auch
nicht zu kräftig sind, um das Glas zerstören zu können. Der Schlägel ist ein
flexibler, leichter Draht mit einer Holzperle, um ebenfalls eine Beschädigung
des Glases zu verhindern. 12 Servos würden eine Menge PWM-fähige IO-Leitungen am
Pro Micro benötigen. Deshalb habe ich ein separates `16-Kanal PWM-Modul PCA9685
<https://learn.adafruit.com/16-channel-pwm-servo-driver?view=all>`_
verwendet. Dieses Modul und der Pro Micro kommunizieren über I2C und das Modul
hat ausreichend Ausgänge für alle Servos.

Die WS2812b LEDs waren kein besonderes Problem. Ich hatte noch ausreichend
Einzelmodule herumliegen. Die einzelnen LEDs werden zusammen in Reihe an eine
Datenleitung und dann an einen Pin vom Mikrocontroller angeschlossen. Über die
`Arduino FastLED Bibliothek
<https://www.arduino.cc/reference/en/libraries/fastled>`_ ist die Programmierung
der LEDs ein Kinderspiel.

Auf meinem Computer habe ich den MIDI Sequencer `Rosegarden
<https://rosegardenmusic.com/>`_ installiert. MIDI Files bekannter
Weihnachtslieder gibt es bspw. `hier
<http://weihnachtslieder.michaelsmusik.bplaced.net/>`_. Bei polyphonen
MIDI-Files muss man sich natürlich zuerst den richtigen Track heraussuchen.
Anschließend habe ich die Noten in der Matrix-Ansicht in den richtigen
Notenbereich verschoben. Die Zwölf Gläser habe ich willkürlich den Noten C4 (c')
bis B4 (h') zugeordnet. Viele Lieder hatten allerdings eine größere
Noten-Dynamik als mir Töne auf meinem Glas-Xylophon zur Verfügung standen. Dann
habe ich einfach einzelne Noten verschoben, um es "passig" zu machen. Die
Schöpfer dieser Werke und alle Musikliebhaber mögen mir verzeihen ...

Am Ende müssen natürlich noch die Gläser gestimmt werden. Ich habe 12 identische
Weingläser vom Discounter verwendet, die aber durch geringfügige
Produktionsunterschiede unterschiedliche Eigenfrequenzen haben. Das habe ich
ausgenutzt und die Gläser bereits vorsortiert. Die Gläser lassen sich jetzt
durch Einfüllen von Wasser stimmen - je mehr Wasser, desto tiefer der Ton. Am
besten eignen sich "bauchige" Rotweingläser. Ich habe festgestellt, dass die
Wassermenge bis zu der Höhe, wo das Glas am breitesten ist, nicht wirklich
hörbar zum Stimmen beiträgt. Nur das Wasser darüber im konischen Teil des Glases
verändert die Eigenfrequenz hörbar.  Ich hatte von Anfang an nur 12 Gläser und
das letzte Glas mit dem tiefsten Ton war am Ende gut gefüllt. Füllt man das Glas
zu stark, erhält man nicht einen satten, tiefen Ton sondern das Glas klingt nur
"stumpf". Abgesehen davon, dass ich - wie gesagt - nicht mehr Gläser hatte oder
auf dem Brett hätte unterbringen können, hätte ich wegen der beschränkten
Füllmenge auch nicht wirklich viel mehr Töne realisieren können. Das Stimmen
habe ich rein "nach Gehör" gemacht, also ohne Stimmgerät oder ähnliches.

Mit dem Endergebnis bin ich ganz zufrieden, auch wenn es sicherlich noch einiges
zu verbessern gibt. Ich habe sogar noch ein 13. Servos vorgesehen, welches kleine Glöckchen
bewegen kann und als Percussion geplant war. Dadurch geht mir aber das Timing
kaputt. Ich habe schon eine Idee, wie ich das lösen könnte, allerdings ist das
eine etwas umfangreichere Änderung der Software auf dem Pro Micro, für die ich
vor Weihnachten keine Zeit mehr habe. |ss| Mich nervt auch der Workaround mit dem
Starten des Terminal-Programms, bevor das Programm auf dem Mikrocontroller
startet. Da ich den Pro Micro ja nun über die AVR ISP-Schnittstelle und nicht
über USB prorammiere, benötige ich vermutlich den Bootloader von Sparkfun nicht
mehr, den ich im verdacht habe. Aber auch das teste ich später mal. |se| [Update
2021/12/23: Lösung, siehe oben im Text.]

.. youtube:: 1BoEhzbZe9E
   :align: center

Frohe Festtage und einen guten Start ins neue Jahr!

