#!/usr/bin/env python3

"""
Get reading from Nova PM Sensor SDS011
(dust sensor, air quality sensor, PM10, PM2,5)

Designed to run from cron and append CSV file.

Script tested using Python3.4 on Ubuntu 14.04.

TODO: choose by dev name using udev, add dev id info, python package pyudev
    udevadm info -q property --export /dev/ttyUSB0
"""

import os
import csv
import io

import logging
import datetime
import argparse

try:
    import serial
except ImportError:
    print('Python serial library required, on Ubuntu/Debian:')
    print('    apt-get install python-serial python3-serial')
    raise


LOG_FORMAT = '%(asctime)-15s %(levelname)-8s %(message)s'


def append_csv(filename, field_names, row_dict):
    """
    Create or append one row of data to csv file.
    """
    file_exists = os.path.isfile(filename)
    with io.open(filename, 'a', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile,
                                delimiter=',',
                                lineterminator='\n',
                                fieldnames=field_names)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row_dict)


def read_nova_dust_sensor(device='/dev/ttyUSB0'):
    dev = serial.Serial(device, 9600)

    if not dev.isOpen():
        dev.open()

    msg = dev.read(10)
    assert msg[0] == ord(b'\xaa')
    assert msg[1] == ord(b'\xc0')
    assert msg[9] == ord(b'\xab')
    pm25 = (msg[3] * 256 + msg[2]) / 10.0
    pm10 = (msg[5] * 256 + msg[4]) / 10.0
    checksum = sum(v for v in msg[2:8]) % 256
    assert checksum == msg[8]
    return {'PM10': pm10, 'PM2_5': pm25}


def main():
    logging.basicConfig(format=LOG_FORMAT, level=logging.INFO)

    parser = argparse.ArgumentParser(description='Read data from Nova PM sensor.')
    parser.add_argument('--device', default='/dev/ttyUSB0',
                        help='Device file of connected by USB RS232 Nova PM sensor')
    parser.add_argument('--csv', default=None,
                        help='Append results to csv, you can use year, month, day in format')
    args = parser.parse_args()

    data = read_nova_dust_sensor(args.device)
    logging.info('PM10=% 3.1f ug/m^3 PM2.5=% 3.1f ug/m^3', data['PM10'], data['PM2_5'])

    if args.csv:
        field_list = ['date', 'PM10', 'PM2_5']
        today = datetime.datetime.today()
        data['date'] = today.strftime('%Y-%m-%d %H:%M:%S')
        csv_file = args.csv % {'year': today.year,
                               'month': '%02d' % today.month,
                               'day': '%02d' % today.day,
                               }
        append_csv(csv_file, field_list, data)

if __name__ == '__main__':
    main()

