#!/usr/bin/python3
# This script generates fresh SSL keys to be used with your https server, if you don't mind using the default keys, or if you want to just run a basic http server use start-servers_x0r.py instead

from subprocess import call
import http.server, ssl
import time

prompt = "What do you want to name your key file? \n:"

key = input(prompt)
print (f"Making private key . . . .")
keygen = call(['openssl', 'genrsa', '-des3', '-out', f'{key}.key', '2048'])


prompt1 = (f'What do you want to call your root certificate pem file? \n:')
pem = input(prompt1)
print (f"Making Root Certificate PEM file . . ")
pemgen = call(['openssl', 'req', '-x509', '-new', '-nodes', '-key', f'{key}.key', '-sha256', '-days', '420', '-out', f'{pem}.pem'])


prompt2 = "Type Name:  "

name = input(prompt2)

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



print ("\n\nPreparing SSL . . .")
time.sleep(1.5)
#print (f"\n\n{name}\nThe PEM pass phrase to start your HTTPS server on {IP} is:\nx0rk3y")

server_address = (IP, 443)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket,
                             server_side=True,
                             certfile=f'{pem}.pem',
                             keyfile=f'{key}.key',
                             ssl_version=ssl.PROTOCOL_TLS)


spot_light(name)

print (f"\n{name}'s https server is awaiting connections . . . . ")
print (f" . . . .")
print (f"to access your server navigate to:\nhttps://{IP}/xfil-SSL.html")
httpd.serve_forever()

"""
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
"""
