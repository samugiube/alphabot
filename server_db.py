import socket
import sqlite3

IP_PORTA = ("192.168.0.201", 4908)
BUFFER_SIZE = 4096

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(IP_PORTA)
    s.listen()
    print("Server in ascolto...")

    c, _ = s.accept()
    print("Client connesso")

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

    msg_ret = "Accesso negato"
    if row:
        msg_ret = "Accesso effettuato correttamente"

    c.send(msg_ret.encode())

    s.close()

if __name__ == "__main__":
    main()
