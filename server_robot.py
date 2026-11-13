import libreria
import socket
import sqlite3

IP_PORTA = ("192.168.0.201", 4908) # IP del robot
BUFFER_SIZE = 4096

r = libreria.AlphaBot()

comandi = {
    "w": r.forward,
    "s": r.backward,
    "a": r.right,
    "d": r.left,
    "p": r.stop,
    "l": r.increase_speed,
    "k": r.decrease_speed,
    "exit": r.stop
}

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(IP_PORTA)
    s.listen()
    print("ROBOT in attesa di connessioni....")

    c, _ = s.accept()
    print("ROBOT ha una connessione!")

    data = c.recv(BUFFER_SIZE)
    msg = data.decode()
    print(msg)

    username, password = msg.split("$")
    
    conn = sqlite3.connect("./alphabot.db")
    cur = conn.cursor()

    cur.execute("""
        SELECT *
        FROM utenti
        WHERE username = ?
            AND password = ?
    """, (username, password))
    row = cur.fetchone()
    print(row)

    if not row:
        c.send("Accesso negato".encode())
        c.close()
        exit()

    c.send("Accesso effettuato correttamente".encode())

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
