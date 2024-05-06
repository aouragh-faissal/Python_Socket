import socket

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind(('', 50000))	
serveur.listen(5)

while True:
	client, infosClient = serveur.accept()
	print("Client connecte. Adresse " + infosClient[0])
	requete = client.recv(255)	
	print(requete.decode("utf-8"))
	reponse = "Bonjour, je suis le serveur"
	client.send(reponse.encode("utf-8"))
	print("Connexion fermee")
	client.close()
	
serveur.close()