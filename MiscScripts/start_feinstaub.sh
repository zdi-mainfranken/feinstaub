#!/bin/bash
# /bin/sleep 10
# Now I am using the gpsd auto start config.
# gpsd -b /dev/ttyACM0 -F /var/run/gpsd.sock -G >> /home/pi/feinstaub/gpsd_daemon.log 2>&1 &
/bin/sleep 10
python web_feinstaub.py >> feinstaub_start_prozess.log 2>&1 &
