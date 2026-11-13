import socket

IP_PORTA = ("192.168.0.201", 4908)
BUFFER_SIZE = 4096

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(IP_PORTA)

    username = input("Inserire il nome utente -> ")
    password = input("Inserire la password -> ")

    s.send(f"{username}${password}".encode())
    data = s.recv(BUFFER_SIZE)
    msg = data.decode()
    print(msg)

    s.close()

if __name__ == "__main__":
    main()
