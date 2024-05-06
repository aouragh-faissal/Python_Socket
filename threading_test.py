import threading 

def compteur(nomThread):
	for i in range(100):
		print(nomThread + " : " + str(i))
		
threadA = threading.Thread(None, compteur, None, ("Thread A",), {}) 
threadB = threading.Thread(None, compteur, None, ("Thread B",), {}) 

threadA.start() 
threadB.start()