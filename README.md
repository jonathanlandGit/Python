# PythonChatroom_Land
NOTE: This program has been modified from the Python code found at https://www.geeksforgeeks.org/simple-chat-room-using-python/. Listed below are discuss the features that have been added, and further instructions on how to use the program, in light of the additional features. 

There are two sections to this overview: 
I. Features
II. Instructions

=============================================================

I. Features

1.	This program gives a message indicating a set format to compile and run the code at the command line (e.g., script IP port#). If the wrong format is entered, it gives a statement about what to enter for the correct format in order to connect with the server.  

2.	This program indicates when users have connected to the server.  

3.	When connected, on the server side, the IP address of each user shows up. This is important for system administrator since—if data is needed to be found or monitored in the chat room—the name of the user and the message also shows up each time a message is sent from client to client.

4.	This program is capable of having multiple clients connect from different computers (different IPs). So, the sockets allows for multiple clients, instead of it being communication between the server and one client.

5.	This program allows clients to choose their own chat room name. When clients have connected to the server, a greeting is displayed on the screen, and then they are asked to select a user name. The user name continues to remain on the screen as they send message back and forth from client to client. 

6.	There are two ways clients can leave the chat room. First, if they use a taboo word, and second if they decide to sign out by typing in a keyword to exit the program.

7.	If a user enters a taboo word, a “disconnected” message shows up on his or her screen, and the connection is removed. No more typing or sending of messages can be completed. Additionally, when the specific client has been disconnected, a message also shows up to the server and other clients that the specific client who used the taboo word has been disconnected (note: the program shows the user name of the client disconnected also, not just IP or a message with no IP or user name). 

8.	If a client signs out of the chat room for any reason, a message appears on the server and other client sides stating which client has left the chat room. 

=============================================================


II. Instructions

1.	Download or upload the two Python programs to your computer (e.g., chatServerSide and chatClientSide). Save the programs somewhere to a path you can find on your computer (NOTE: If you want to change the badwords or taboo first before running the program, open the on client side and change the words. If not, compile the program, and default exit words are already in the program).  

2.	Open terminal, or some other command line GUI, to compile the program and to get it up and running. 

3.	With the command line GUI open, compile the server side first. In the terminal, cd to the directory or desktop where you saved the Python programs (i.e., get in the correct path on your computer where the programs are), and then type… 

          python chatServerSide.py <yourIPaddress> <port#>   

          Note: If you are using python 3, you will want to type python 3, instead of just python. 

4.	A message should appear on the screen that the server is activated. If not it will tell you the correct format to type in the command to activate the server. After the connection, you have two options: You can either connect clients to the server on the same machine, or connect clients from other machines to the host machine. 
	
          a.	Connecting clients on host machine: Create/open a new command line GUI and type the following command: python     
          chatClientSide.py <yourIPaddress> <port#>
   
          b.	Connecting clients on different machines to host machine: You will want to have the client program downloaded on the 
          computer you are using and cd to where that program is saved in terminal to compile it. You will then follow the same procedure 
          for 4(a) and type: python chatClientSide.py <yourIPaddress> <port#>

5.	If you are on the host machine, you will see your own IP address appear on the server side and a greeting to the chat room on the client side. If not, you will not see the server side, but you get a greeting on the client side. 

6.	You will be asked to enter a user name, and this will remain throughout the chatting unless you either type “Quit” to exit the chat room or use a taboo word, in which case you will be disconnected from server.  

Note: Only the sys admin could see both user name and IP address. This would helpful if for some reason the chatting needed to be monitored or permissions set.  
