from pynput import keyboard
import socket

IP_PORTA = ("192.168.0.201", 4908) # IP del robot
BUFFER_SIZE = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(IP_PORTA)

comandi = ["w", "a", "s", "d"]
tasto_premuto = None

def on_press(key):
    global tasto_premuto

    try:
        c = key.char.lower()
    except AttributeError:
        print("tasto senza lettera premuto")
        return

    if c in comandi and c != tasto_premuto:
        tasto_premuto = c
        print(f"{c} premuto")
        s.send(c.encode())

def on_release(key):
    global tasto_premuto

    if key == keyboard.Key.esc:
        return False

    try:
        c = key.char.lower()
    except AttributeError:
        print("tasto senza lettera rilasciato")
        return

    if c == tasto_premuto:
        print(f"{c} rilasciato")
        tasto_premuto = None
        s.send("p".encode())


def main():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    
    s.send("EXIT".encode())
    s.close()

if __name__ == "__main__":
    main()
