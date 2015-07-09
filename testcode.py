__author__ = 'dabell2'

import pyModbusTCP

from pyModbusTCP.client import ModbusClient

import time

if __name__ == "__main__":

    host = input("\nPlease enter IP address [127.0.0.1]: ")
    port = input("Please enter port [502]: ")

    if not host:
        host = "172.16.143.146"

    if not port:
        port = 502

    c = ModbusClient(timeout=5)
    c.host(host)
    c.port(port)

    print("\nTrying to connect to " + host + ":" + str(port))

    if c.open():
        print("Opened")

    print(c.is_open())

    if c.close():
        print("Closed")

    print(c.is_open())