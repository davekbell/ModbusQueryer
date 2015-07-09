__author__ = 'dabell2'

import pyModbusTCP

from pyModbusTCP.client import ModbusClient

import time


def read_regs():

    howmany = input("\nHow many times to read? [5]: ")

    if not howmany:
        howmany = 5

    for i in range(int(howmany)):
        registers = c.read_holding_registers(0, 2)
        if registers:
            print("\n" + str(registers))
            time.sleep(1)
        else:
            print("\nRead Error")
    print("\nCompleted " + str(howmany) + " successful reads")


def write_regs():

    reg_value = input("\nWhat value to write? [555]: ")
    reg_addr = input("\nWhat address to write? [0]: ")

    if not reg_value:
        reg_value = 555
    else:
        reg_value = int(reg_value)

    if not reg_addr or reg_addr == "":
        reg_addr = 0

    if c.write_single_register(reg_addr,reg_value):
        print("\nWrote Register")
        time.sleep(0.5)


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

    for attempt in range(3):
        print("\nTrying to connect to " + host + ":" + str(port) + "...   Attempt " + str(attempt+1))
        if c.open():
            print("\nSuccessful Connection")
            failedconnection =  False
            time.sleep(0.5)
            choice = ""
            while choice != "q":
                choice = input("\nPress \n[r] to Read  \n[w] to Write \n[q] to Quit: ")
                if choice == "r":
                    print("\nChose Read")
                    read_regs()
                elif choice == "w":
                    print("\nChose Write")
                    write_regs()
                else:
                    if choice != "q":
                        print("\nInvalid choice")

            break
        else:
            print("Connection Attempt " + str(attempt+1) + " Failed")
            failedconnection = True

    if c.is_open and c.close():
        print("\nConnection Closed Successfully")
        time.sleep(0.5)
    elif failedconnection == True:
        print("\n Unable To Connect To Device")

    print("\nProgram Terminated")


else:
        print("\nNot a module")

#Write a program that writes values to the PLC every 1s.. sine wave between two boundaries say 0 to 100
#Write a program that reads every 1s.. if value over say 90 generate SNMP trap
#Take inputs for sine wave value bounds and and also for value that generates trap