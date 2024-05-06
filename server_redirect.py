import socket
import requests

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind(('', 50000))	
serveur.listen(5)

while True:
	client, infosClient = serveur.accept()
	print("Client connecte. Adresse " + infosClient[0])
	requete = client.recv(10000)
	#print(requete.decode("utf-8"))
	r = requests.get('https://hespress.com/')
	heder = 'HTTP/1.0 200 OK\n Content-Type: text/html\n\n'
	res_f = heder + r.text
	client.sendall(res_f.encode("utf-8"))
	print("Connexion fermee")
	client.close()
	
serveur.close()