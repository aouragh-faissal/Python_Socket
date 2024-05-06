
import socket

adresseIP = "127.0.0.1"	
port = 80	

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((adresseIP, port))
print("Connecte au serveur")
print("Bonjour, je suis le client".encode("utf-8"))
client.send("Bonjour, je suis le client".encode("utf-8"))
reponse = client.recv(255)
print(reponse.decode("utf-8"))
print("Connexion fermee")
client.close()