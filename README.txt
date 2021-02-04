Step 1:
Place the x0r_py-servers folder and all its contents into the box you want to run your server from.
and
Place copy all the files you want to transfer in the xfil folder

Step 2:
Run the start-servers_x0r.py script to walk you through setting up a server.
The options will ask you to choose between setting up a https server with SSL, or a regular http server.
NOTE: While the server session is maintained the terminal window will hang to provide http responses from the https server. 
Open additional windows or background the session to have access to your terminal.


Step 3:
Access your server to retrieve your files
if using SSL navigate to:

https://<IP>/xfil-SSL.html

if using a normal http server navigate to:

http://<IP>/xfil-plaintext.html

When you run the script it will give you the actual link to the server

Step 4:
EXFIL !!!!!
