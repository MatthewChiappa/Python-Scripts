# Matthew Chiappa
# CSC223
# 11/3/14

## imports
import optparse
from socket import *

## searches the specified port in the file
## and displays whether or not the port is open
def connScan(host, port, wFile):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((host, port))
        sock.send('ViolentPython\r\n')
        results = sock.recv(100)
        wFile.write('\n[+] %d/tcp open' % port)
        print '[+] %d/tcp open' % port
        wFile.write('\n[+] ' + str(results))
        print '[+] ' + str(results)
    except:
        wFile.write('\n[-] %d/tcp closed' % port)
        print '[-] %d/tcp closed' % port
    finally:
        sock.close() 
        
## all the ports and the host is inputted as parameters and
## connection to host is established then every for is iterated
## through a for loop to connScan
def scanPorts(host, ports, wFile):
    try:
        iP = gethostbyname(host)
    except:
        wFile.write("\n[-] Cannot resolve '%s': Unknown host" %host)
        print "[-] Cannot resolve '%s': Unknown host" %host
        return

    try:
        name = gethostbyaddr(iP)
        wFile.write('\nScan Results for: ' + name[0] + ":")
        print '\nScan Results for: ' + name[0] + ":"
    except:
        wFile.write('\nScan Results for: ' + iP + ":")
        print '\nScan Results for: ' + iP + ":"

    setdefaulttimeout(1)
    for port in ports:
        connScan(host, int(port), wFile)

## starts the scan process by scanning the file to get the host name
## and ports in the format: <IPAddress>:<PortNum>,<PortNum>,<PortNum>
def startScan(fileName, wFile):
    file = open(fileName, "r")
    for line in file:
        info = line.split(":")
        name = info[0]
        nums = info[1].split(",")
        portNums = map(int,nums)
        
        wFile.write("Scanning IP: " + name + " in Ports: " + ', '.join(map(str, portNums)))
        print "\nScanning IP: " + name + " in Ports: " + ', '.join(map(str, portNums))
            
        scanPorts(name, portNums, wFile)
        wFile.write("\n\n")
    file.close()
        
## gets the input file and creates the file and calls the startScan function    
def main():
    wFile = open("output.txt", "w")
    fileName = raw_input('Please enter the file name with extension: ')
    startScan(fileName, wFile)
    wFile.close()
    
## main is executed
main()
    