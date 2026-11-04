from pynput import keyboard
import socket

IP_PORTA = ("192.168.1.107", 4908) # IP del robot
BUFFER_SIZE = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(IP_PORTA)

def on_press(key):
    c = getattr(key, "char")
    try:
        print(f"{key.char}")
        s.send(key.lower().encode())
    except AttributeError:
        print("ERRORE")

def on_release(key):
    print(f"{key} rilasciata")
    s.send("p".encode())

    if key == keyboard.Key.esc: return False

def main():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    
    s.send("EXIT".encode())
    s.close()

if __name__ == "__main__":
    main()
