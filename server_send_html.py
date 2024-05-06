
import socket



serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind(('', 80))	
serveur.listen(5)
i=0

while True:
	client, infosClient = serveur.accept()
	print(i)
	print("Client connecte. Adresse ")
	print(infosClient)
	requete = client.recv(1024)
	print(requete.decode("utf-8"))
	heder = 'HTTP/1.0 200 OK\n Content-Type: text/html\n\n'
	res= '<html><body> <h1>Hello World</h1> this is my server!</body></html>'
	res_f = heder + res
	client.sendall(res_f.encode("utf-8"))
	print("Connexion fermee")
	i =i+1
	client.close()
	

serveur.close()