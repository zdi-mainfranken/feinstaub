# feinstaub 
Notwendig

--> config für eigenes wlan zuhause bzw am einsatzort

- Raspian Software: https://downloads.raspberrypi.org/raspbian_lite_latest
- Software für flshen der SD Karte https://www.balena.io/etcher/

Erste Schritte:
    
   1.Flashen des Images auf die SD Karte: https://www.raspberrypi.org/documentation/installation/installing-images/README.md
   2. SD Karte nach dem flashen in Raspi stecken und Tastatur, Strom und Monitor anschließen
   3. Nach dem ersten booten wird ein Neustart notwendig (Hintergrundinfo: Es werden für jedes Gerät indivuduelle Schlüssel erzeugt)
   4. Erstes Login: Benutzer: pi Kennwort: raspberry
   5. Starten der Konfiguration: sudo raspi-config
   6. Punkt 4 wählen [Localisation Options] und 
   6.a. Local auf de_de.UTF8 wählen und bestätigen
   6.b. Timezone auf Berlin setzten
   6.c. Keyboard auf German setzten
   6.d. Punkt 5 wählen [Interfacing Options] -> P2 SSH -> Auf ja stellen und mit Enter bestätigen
   6.d. Finish und mit reboot Raspberry neustarten
   
   7. Nach dem Neustart wieder einloggen -> ip a eingeben unter wlan0 steht 
   7.a.
