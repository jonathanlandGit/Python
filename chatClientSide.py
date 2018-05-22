# client side
import socket
import select
import sys
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print("Enter in proper format: script, IP address, port number")
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.connect((IP_address, Port))

userName = raw_input("Please enter a username: ")

while True:

    # we need to maintain a list of input streams as they connect
    sockets_list = [sys.stdin, server]
    
    """ Basically we have two options we have to take care: the
        user will give  manual input, or the server is sending a message to be printed on the screen to clients."""
    read_sockets, write_socket, error_socket = select.select(sockets_list, [], [])

    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
        
            print(" ")
            print(message)
            print("")
            print(userName + " >>")

        else:
            #we are including this here so that sys admin can still
            #see the traffic on network and the warnings listed
            #this is why this is included here
            message = sys.stdin.readline()
            
            ########Include the words/strings in the following variables for this to work##########
            badWords = (" ", " ", " ")
            worseWords = (" ", " ", " ")
            
            input_words = message.lower().split()

            for word in input_words:
                if word in badWords:
                    print("")
                    print("**SERVER WARNING: WATCH LANGUAGE**")
                    print("")
                    print(userName + " >>")
        
            for word in input_words:
                if word == "quit":
                    print("DISCONNECTING...")
                    server.send(userName + "**HAS SIGNED OUT**")
                    time.sleep(2)
                    exit(0)
        
            #server.send(message)
            print("")
            server.send("<" + userName + "> " + message)
            print("")
            sys.stdout.flush()

            #loop to check for worseWords, and if so remove connection
            for word in input_words:
                if word in worseWords:
                    print("**DISCONNECTING...")
                    print("")
                    server.send(userName + " **HAS BEEN DISCONNECTED**")
                    time.sleep(2)
                    exit(0)
                    #conn.close()

server.close()
