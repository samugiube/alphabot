### Venerdì 23 ottobre 2026

Ciao Jason, spero che tu stia bene. Scrivo questo file per farti sapere quello che sono riuscito a fare alla lezione di oggi con l'Alphabot.

Ammetto di avere avuto qualche difficoltà all'inizio, per lo più perché c'era gente che ha avuto problemi con la micro sd, e i prof erano impegnati ad aiutare loro.

Alla fine sono riuscito a creare un programma (`primo_programma.py`), giusto per provare che la connessione tra robot e computer funzionasse.

Il file `libreria.py` è un file che ha condiviso Viola su Classroom. In più, ci hanno chiesto di scaricare WinSCP e Putty. Credo che tu possa averceli già dall'anno scorso, ma nel dubbio te lo dico.

Non so neanche se vedrai questo file prima della prossima volta, anzi, è molto probabile che ti dirò tutto io direttamente... :\)

Spero di rivederti presto a lezione.
Samu

### Venerdì 30 ottobre 2026

In questa lezione ci è stato chiesto di trovare un modo per comandare il robot premendo WASD sul computer.

Ho creato un socket TCP, ho messo `server_robot.py` sul robot, e ho fatto partire `client_pc.py` sul computer.

Per far funzionare il programma è necessario installare la libreria `pynput`.

L'Alphabot riconosce che i pulsanti vengono premuti, ma non ho ancora trovato un modo per fare in modo che il robot va avanti solo quando il pulsante è premuto.

### Venerdì 6 Novembra

Sono riuscito a far funzionare i pulsanti WASD.

Ho corretto il file `libreria.py`, e ora le funzioni `forward` e `backward` funzionano correttamente.

Ho aggiunto i comandi sui tasti L e K per aumentare o diminuire la velocità.

Quando va avanti, il robot tende a curvare verso destra. Non ho ancora capito il perché.

Ci hanno chiesto di fare qualcosa con i sensori di distanza, ma non ho ancora fatto nulla perché:
- Non ho capito quali pin sono collegati ai sensori
- Non ci è stato spiegato come utilizzare questi pin
- Nella `libreria.py` non ho trovato nulla sui sensori
