# server side
import socket
import select
import sys
from thread import *
import time
from time import sleep

"""first arg include the address domain of the socket.
    used when we have an Internet Domain with
    any two hosts. The second argument is the type of socket.
    SOCK_STREAM means that data or characters are read in
    a continuous flow."""
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# we need to check if sufficient arguments are provided
if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")
    exit()

# takes the first argument from command prompt as IP address
IP_address = str(sys.argv[1])

# takes second argument from command prompt as port number
Port = int(sys.argv[2])

"""
    we have to bind the server to an IP address and port number.
    Client has to know what server to connect to
    """
server.bind((IP_address, Port))

"""
    listens for active connections. number can vary
    """
server.listen(100)

#store clients in a list
list_of_clients = []

#main thread for client
def clientthread(conn, addr):

    # sends a message to the client whose user object is conn
    conn.send("Welcome to Chatroom")

    #boolean to exit out once we cancel a connection
    is_active = True

    #keep looking as long as conditions are true, otherwise close on account of conditions
    while True:
        
        try:
            message = conn.recv(2048)
    
            #code for traversing list to look for inappropriate words used in chat
            if message:
                # two levels of inappropriate words - obviously these can be changed or put
                # put within a text file to be read
                badWords = ("stupid", "idiot", "scalawag")
                worseWords = ("snoot", "sycophant", "knave")
                
                #w need to parse each word as it is streamed
                input_words = message.lower().split()
                
                #now loop through each parse word looking for badWords
                #if found give a warning
                for word in input_words:
                    if word in badWords:
                        print("**SERVER WARNING: WATCH LANGUAGE**")
            
                ###extra code###
                
                #loop to check for worseWords, and if so remove connection
                # for word in input_words:
                    #if word in worseWords:
                    # message_to_send = "<" + addr[0] + "> " + "HAS BEEN DISCONNECTED"
                    #broadcast(message_to_send, conn)
                    #time.sleep(2)
                    #conn.close()
                    #break;
                
                """prints the message and IP of user"""
                print("<" + addr[0] + "> " + message)
                
                # broadcast function sends to all clients
                message_to_send = message
                broadcast(message_to_send, conn)
        
            else:
                """if the message have no content, then we remove conn"""
                remove(conn)
    
        except:
            continue


"""broadcast method to go to all clients, except for the message
    if words are used"""
def broadcast(message, connection):
    for clients in list_of_clients:
        if clients != connection:
            try:
                clients.send(message)
            except:
                clients.close()
                remove(clients)

"""method removes the connection from the list"""
def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)


while True:
    """Accepts a connection request and stores paramms conn
        conn is a socket object for user. addr contains the IP
        of client that just connected"""
    conn, addr = server.accept()
    
    """we need to maintain a list of the clients that we are broadcasting
        so that we can add them"""
    list_of_clients.append(conn)
    
    # print client address
    print(addr[0] + " connected")
    
    # now we create the thread
    # each user gets a new thread
    start_new_thread(clientthread, (conn, addr))

conn.close()
server.close()
