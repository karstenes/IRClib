import socket, ssl
from time import sleep
import threading
import string
class IRC:
    readbuffer = ""
    "IRC Module for python"
    def __init__(self, HOST, PORT, NICK, REALNAME, IDENT):
        print "New Connection"
        HOST = socket.gethostbyname(HOST)
        self.HOST = HOST
        self.PORT = str(PORT)
        self.NICK= NICK
        self.REALNAME = REALNAME
        self.IDENT = IDENT
        self.s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # For later use: self.s = ssl.wrap_socket(sock, ca_certs="cacert.pem", cert_reqs=ssl.CERT_REQUIRED)
        self.s.connect((HOST, PORT))
        self.s.send("NICK %s\r\n" % NICK)
        self.s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
        self.rb="ReadBuffer"
        while True:
            self.readbuffer=self.readbuffer+self.s.recv(1024)
            temp=string.split(self.readbuffer, "\n")
            self.readbuffer=temp.pop( )
            for self.line in temp:
                self.line=string.rstrip(self.line)
                self.line=string.split(self.line)
                print " ".join(self.line)
                if(self.line[0]=='PING'):
                    self.s.send("PONG %s\r\n" % self.line[1])
                    print("Ponged")
            if len(self.line) >= 3:
                if self.line[3] == ":+i":
                    break
    def read(self, type):
        if type.lower() == "nick":
            if self.line[2][:1] != "#":
                self.line[2] = self.line[0][1:self.line[0].strip(":").find("!")+1]
            return [self.line[0][1:self.line[0].strip(":").find("!")+1], self.line[2], " ".join(self.line[3:])[1:]]
        else:
            return [self.line[0], self.line[2], " ".join(self.line[3:])[1:]]
    def ping(self):
        "Handles Pinging"
        self.readbuffer=self.readbuffer+self.s.recv(1024)
        temp=string.split(self.readbuffer, "\n")
        self.readbuffer=temp.pop( )
        for self.line in temp:
            self.line=string.rstrip(self.line)
            self.line=string.split(self.line)
            self.p=" ".join(self.line)
            if(self.line[0]=='PING'):
                self.s.send("PONG %s\r\n" % self.line[1])
                print("Ponged")
    def send(self, message, channel):
        self.s.send("PRIVMSG %s :%s\r\n" % (channel, message))
    def join(self, channel):
        self.s.send("JOIN %s\r\n" % channel)
    def leave(self, channel):
        self.s.send("LEAVE %s\r\n" % channel)
    def action(self, action, channel):
        self.send("\001ACTION "+action, channel)
    
