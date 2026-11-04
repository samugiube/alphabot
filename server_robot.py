import libreria
import socket
import time

IP_PORTA = ("192.168.1.107", 4908) # IP del robot
BUFFER_SIZE = 4096

r = libreria.AlphaBot()

comandi = {
    "w": r.forward,
    "s": r.backward,
    "a": r.right,
    "d": r.left,
    "p": r.stop,
    "exit": r.stop
}

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(IP_PORTA)
    s.listen()
    print("ROBOT in attesa di connessioni....")

    c, _ = s.accept()
    print("ROBOT ha una connessione!")

    while True:
        data = c.recv(BUFFER_SIZE)
        msg = data.decode()
        print(f"<- {msg}")

        if msg.lower() in comandi:
            comandi[msg.lower()]()

        if msg.upper() == "EXIT":
            break

    c.close()

if __name__ == "__main__":
    main()
