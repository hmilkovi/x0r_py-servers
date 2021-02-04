#!/usr/bin/python3
# A script to spawn http or https servers for regular and encrypted file transfers
# x0r_sys
# standalone exe available for port to windows

import http.server, ssl
import time


prompt = "Type Name:  "

name = input(prompt)

def spot_light(username):

	print(f"    \nDONT FORGET!\n")
	time.sleep(1.2)
	print(f"------->{name}")
	time.sleep(1)
	print(f"   Please be neat\n")
	time.sleep(1)
	print(f"        AND\n")
	time.sleep(1)
	print(f"     0000000000")
	print(f"      00000000")
	print(f"       000000")
	print(f"        0000")
	print(f"         00\n")

	print(f"       DELETE")
	time.sleep(2)


prompt3 = "\nWhat IP do you want to host your server on?\nIP:  "

IP = input(prompt3)

prompt4 = "\nDo you want SSL encryption on your server?\nyes or no?: "
answer = input(prompt4)

if answer == "yes":
	print ("\n\nPreparing SSL . . .")
	time.sleep(1.5)
	print (f"\n\n{name}\nThe PEM pass phrase to start your HTTPS server on {IP} is:\nx0rk3y")

	server_address = (IP, 443)
	httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
	httpd.socket = ssl.wrap_socket(httpd.socket,
                               	server_side=True,
                              	 certfile='myCA.pem',
                              	 keyfile='myCA.key',
                              	 ssl_version=ssl.PROTOCOL_TLS)


	spot_light(name)

	print (f"\n{name}'s https server is awaiting connections . . . . ")
	print (f" . . . .")
	print (f"to access your server navigate to:\nhttps://{IP}/xfil-SSL.html")
	httpd.serve_forever()


elif answer == "no":
	print ("\nPreparing a python Simple HTTP server . . .")
	server_address = (IP, 8000)
	httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
	spot_light(name)
	print (f"\n{name}'s http server is awaiting connections . . . ")
	print(f" . . . .")
	print (f"to access your server navigate to:\nhttp://{IP}:8000/xfil-plaintext.html")
	httpd.serve_forever()


else:
	print (f"I don't understand . . sawwy")
