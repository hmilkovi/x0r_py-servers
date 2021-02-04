Step 1:
Place the x0r_py-servers folder and all its contents into the box you want to run your server from.
and
Copy all the files you want to transfer in the xfil folder

Step 2:
Running the start-servers_x0r.py script will walk you through setting up a server.
The options will ask you to choose between setting up a https server with SSL, or a regular http server.  This script uses default keys created by x0r.
If you want to create fresh SSL keys to be used with your python https server then run gen-SSL-keys_start-server_x0r instead.
This way you can use fresh keys with each https instance if you want.

NOTE: While the server session is maintained the terminal window will hang to provide http responses from the https server. 
Open additional windows or background the session to have access to your terminal.


Step 3:
Access your server to retrieve your files from a remote host
if using SSL navigate to:

https://<IP>/xfil-SSL.html

if using a normal http server navigate to:

http://<IP>/xfil-plaintext.html

When you run the scripts it will give you the actual links to the servers

Step 4:
EXFIL !!!!!
