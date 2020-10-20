.. title: push2talk - USB-Fußschalter zum Muten/Unmuten
.. slug: push2talk-usb-fussschalter-zum-mutenunmuten
.. date: 2020-10-17 23:12:33 UTC+02:00
.. tags: mikrocontroller, arduino, programmieren, usb, hid, atmel, mega32u4, teensy, prjc
.. category: basteln
.. link: 
.. description: Muten/Unmuten per Fußschalter 
.. type: text

.. figure:: /images/p2t_final.thumbnail.jpg
   :align: center
   :alt: Fertiges push2talk Gerät mit Fußschalter zum Anschluss via USB

   Fertiges push2talk Gerät mit Fußschalter zum Anschluss via USB


Durch COVID-19 hat auch bei mir die Zahl der Tele- und Videokonferenzen stark
zugenommen. Insbesondere dann, wenn viele Personen gleichzeitig teilnehmen,
finde ich es wichtig, wenn alle, die gerade nicht sprechen, ihr Mikrofon
stummstellen. So reduzieren sich störende Hintergrundgeräusche doch deutlich,
und man versteht diejenige Person, die gerade spricht, viel besser.

Leider klappt das mit dem Stummschalten, und auch das Wiederaktivieren des
Mikros nicht immer. Das haben wohl viele schon erlebt: Jemand vergisst das
Stummschalten und alle anderen Konferenz-Teilnehmer werden unfreiwillig Zeuge
von Geklapper, dem Schlürfen an einer Tasse oder sogar einem anderem, parallelem
Gespräch am Handy. Oder jemand anderes beteiligt sich an der eigentlichen
Diskussion und wundert sich, dass ein Feedback ausbleibt, bis sie oder er
feststellt, dass das eigene Mikrofon noch gemutet ist. 

Um da ein wenig Abhilfe zu schaffen, habe ich deshalb ein Gerät gebastelt,
welches ich in diesem Artikel vorstellen möchte.

.. TEASER_END

Herzstück dieses Geräts ist ein `PRJC Teensy 2.0 Board
<https://www.pjrc.com/store/teensy.html>`_.  Dieses Board besitzt einen `Atmel
MEGA32U4 Mikrocontroller
<http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-7766-8-bit-AVR-ATmega16U4-32U4_Summary.pdf>`_
mit einem USB 2.0 Device Module On-Chip, so dass man dieses Board bspw. als `USB
Human Interface Device (HID)
<https://de.wikipedia.org/wiki/Human_Interface_Device>`_ einsetzen kann. Dieses
Board kann also als USB-Maus oder -Tastatur fungieren.  In dem Projekt push2talk
habe ich das ausgenutzt, um auf Wunsch diejenigen Tastatur-Codes abzusetzen, die
das Muten/Unmuten des Mikrofons auslösen.

Auslösen kann ich das Absetzen der Tastatur-Codes über einen `Fußschalter
<https://duckduckgo.com/?q=pedal+switch+220v&t=h_&iar=images&iax=images&ia=images>`_,
der an einem GPIO des Teensy 2.0 hängt. Wird der Fußschalter gedrückt (fallende
Flanke am GPIO) wird der Tastatur-Code für das Unmuten ausgelöst. Nimmt man den
Fuß wieder vom Fußschalter, erzeugt dies eine steigende Flanke am GPIO und der
Tastatur-Code für das Muten wird vom MEGA32U4 an den Computer gesendet. Der
Vorteil des Fußschalters ist für mich, dass man die Hände frei hat für Tastatur
und Maus. Der Fußschalter dabei ist mit einem Cinch-Stecker an dem Gehäuse mit
dem Teensy 2.0 angeschlossen. Es kann also prinzipiell jede andere Art von
Taster verwendet werden.

Nun gibt es ja eine Reihe verschiedener Software für Tele- und Videokonferenzen,
die alle auch individuelle Tastatur-Codes für das Muten/Unmuten haben. Um nicht
immer mein push2talk-Gerät neu programmieren zu müssen, kann ich Tastatur-Codes,
die ich zuvor in der Software festgelegte habe, auswählen. Das geht über einen
Drucktaster im Gehäuse des push2talk-Geräts (im Bild am Anfang dieses Artikels
ist das der blaue Taster). Am besten öffnet man ein leeres Textdokument, setzt
den Cursor da hinein und drückt dann die blaue Taste. Push2talk gibt die
jeweilige Tastenkombination als Text aus.

Die Software für den Teensy habe ich in der `Arduino-IDE
<https://www.arduino.cc/en/Main/Software>`_ geschrieben. Die Arduino IDE läßt
sich so anpassen (`Beschreibung hier
<https://www.pjrc.com/teensy/teensyduino.html>`_), dass auch die PRJC
Teensy-Boards damit programmiert werden können.

Die Software für den Teensy kann `hier von meinem Github-Account
<https://github.com/rzbrk/push2talk>`_ heruntergeladen werden. Sie ist recht
simpel. Das Entprellen der Taster habe ich mit der Arduino-Bibliothek `bounce2
<https://github.com/thomasfredericks/Bounce2>`_ gemacht. Die aktuell
ausgewählten Tasten-Codes werden auch im EEPROM des Mikrocontrollers abgelegt.
So "erinnert" sich der Mikrocontroller an diese Einstellung auch bei einem
Power-Cycle.

Push2talk funktioniert bei mir schon seit mehreren Wochen sehr gut und ist
häufig im Einsatz. Allerdings gibt es auch Einschränkungen. Einige
Konferenz-Software hat Tastatur-Codes zum Muten/Unmuten, die auch dann
funktionieren, wenn das Programmfenster gerade nicht aktiv ist. Das ist so bspw.
bei Skype for Business (Windows+F4). Das heißt, ich kann in einer ganz anderen
Anwendung sein und die Fußtaste drücken, und das Mikrofon in Skype for Business
wird gemutet bzw. unmutet. Bei anderen Konferenz-Anwendungen, wie bspw. Webex,
Jitsi, BigBlueButton und vielen anderen funktioniert das nur, wenn das jeweilge
Anwendungsfenster des Konferenzprogramms aktiv ist. das ist natürlich nicht so
toll. Wenn man eh schon Tastatur/Maus verwenden muss, um in das richtige
Anwendungsfenster zu gelangen, kann man Tastatur/Maus ja auch zum Muten/Unmuten
verwenden.

Natürlich muss klar sein, dass diese Tastatur-Codes das Mikrofon nur
software-seitig ausschalten. Was der Rechner dann mit dem Audio macht, ob ein
Stream irgendwo hin übertragen oder sogar mitgeschnitten werden kann, steht auf
einem anderen Blatt (siehe auch `diesen Beitrag auf Fefes Blog zu einem
diesbezüglichen Bugreport zu BigBlueButton
<http://blog.fefe.de/?ts=a1a62f71>`_). Ein Freund hat mich darauf hingewiesen,
dass es in Bezug auf Daten- und Persönlichkeitsschutz am besten wäre, das
Mikrofon hardware-seitig ausschalten zu können. Richtig - allerdings ist das mit
den modernen, kompakten und teilweise via Funk oder USB angeschlossenen
Mikrofonen nicht mehr so einfach realisierbar.

Ich bin trotzdem zufrieden mit push2talk. Und ich habe eine Menge darüber
gelernt, wie ich MEGA32U4-basierte Mikrocontroller-Boards als HID-Devices
verwenden kann.

