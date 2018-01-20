import getpass
import sys
import telnetlib

user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

f = open('daftar_perangkat')

for line in f :
    print "configuring switch " + (line)
    HOST = line
    tn = telnetlib.Telnet(HOST)

    tn.read_until("username : ")
    tn.write(user + "\n")
    if password:
        tn.read_until("password: ")
        tn.write(password + "\n")

    tn.write("conf t \n")

    for n in range (1,11):
        tn.write ("vlan " + str(n) + "\n")
        tn.write("ruang_" + str(n) + "\n")

        tn.write("end\n")
        tn.write("wr\n")
        tn.write("exit\n")

        print tn.read_all()
