# Digital Forensics 2023-24 Project Repository

## Descrizione

Benvenuti nel repository del progetto realizzato per la materia **Digital Forensics 2023-24**. 
Questo corso è tenuto dai docenti **Prof. Sebastiano Battiato** e **Luca Guarnera**. 
Lo scopo di questa repository è di documentare e discutere il progetto effetuato al termine del corso.

## Descrizione del progetto 

Il progetto consiste in uno strumento sviluppato in **Python** che permette di applicare vari filtri a una foto. Dopo ogni applicazione del filtro, l'immagine modificata viene salvata in una cartella denominata "**Elaborazione_Immagini**". I filtri implementati, utilizzando la libreria **cv2**, includono:

- Filtro media
- Filtro mediano
- Filtro laplaciano
- Filtro gaussiano
- Filtro di Wiener
- Filtro bilaterale

Inoltre, è stata implementata una semplice **interfaccia grafica** per facilitare l'uso dello strumento. 
Tramite un menu a tendina, è possibile visualizzare le foto presenti nella cartella "**Elaborazione_Immagini**".

## Installazione delle Librerie

Per eseguire il progetto, è necessario installare alcune librerie Python. Le librerie richieste sono:

- `cv2` (OpenCV)
- `numpy`
- `os` (inclusa in Python)
- `tkinter` (inclusa in Python)
- `Pillow` (PIL)
- `scipy`

Puoi installare queste librerie utilizzando `pip`. Esegui i seguenti comandi nel terminale:

```bash
pip install opencv-python
pip install numpy
pip install pillow
pip install scipy
```
## Esecuzione del Codice

Una volta installate le librerie necessarie, puoi eseguire il codice denominato `codice.py`. Segui questi passaggi:

1. **Clona il Repository**: Scarica il repository dal link fornito o clonalo utilizzando git.
    ```bash
    git clone https://github.com/VincenzoVillanova/Digital-Forensics.git
    cd Digital-Forensics
    ```

2. **Verifica le Librerie**: Assicurati di avere tutte le librerie necessarie installate.

3. **Esegui il Codice**: Esegui lo script Python `codice.py`.
    ```bash
    python codice.py
    ```
    
In questo esempio, `App` è la classe che implementa la tua interfaccia grafica e le funzionalità dei filtri. Assicurati di includere tutto il codice necessario per la tua applicazione all'interno del file `codice.py`.

## Risoluzione dei Problemi

Se incontri problemi durante l'installazione delle librerie o l'esecuzione del codice, verifica di avere una versione aggiornata di Python e di `pip`. Puoi aggiornare `pip` con il seguente comando:

```bash
pip install --upgrade pip
```

Se i problemi persistono, consulta la documentazione delle librerie specifiche o cerca soluzioni nei forum di supporto della community.
