import cv2
import numpy as np
import os
import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
from scipy.signal import wiener

# Dimensione fissa per tutte le immagini
DIMENSIONE_FISSA = (400, 400)

# Funzione che ritorna l'immagine senza modificarla
def ritorna_immagine(immagine):
    return immagine

# Funzione che applica il filtro di media (blur) all'immagine
def applica_filtro_media(immagine):
    return cv2.blur(immagine, (5, 5))

# Funzione che applica il filtro gaussiano all'immagine
def applica_filtro_gaussiano(immagine):
    return cv2.GaussianBlur(immagine, (5, 5), 0)

# Funzione che applica il filtro laplaciano all'immagine
def applica_filtro_laplaciano(immagine):
    laplaciano = cv2.Laplacian(immagine, cv2.CV_64F)  # Applica il filtro Laplaciano
    laplaciano = np.uint8(np.absolute(laplaciano))  # Converte il risultato in uint8
    return laplaciano

# Funzione che applica il filtro mediano all'immagine
def applica_filtro_mediano(immagine):
    return cv2.medianBlur(immagine, 5)

# Funzione che applica il filtro di Wiener all'immagine
def applica_filtro_wiener(immagine):
    immagine_grigia = cv2.cvtColor(immagine, cv2.COLOR_BGR2GRAY)  # Converte l'immagine in scala di grigi
    immagine_wiener = wiener(immagine_grigia, (5, 5))  # Applica il filtro di Wiener
    
    # Clipping dei valori per assicurarci che siano nell'intervallo [0, 255]
    immagine_wiener = np.clip(immagine_wiener, 0, 255)
    
    immagine_wiener = np.uint8(immagine_wiener)  # Converte il risultato in uint8
    return cv2.cvtColor(immagine_wiener, cv2.COLOR_GRAY2BGR)  # Converte nuovamente in BGR


# Funzione che applica il filtro bilaterale all'immagine
def applica_filtro_bilaterale(immagine):
    return cv2.bilateralFilter(immagine, 9, 75, 75)

# Dizionario dei filtri disponibili
filtri = {
    "Filtri": ritorna_immagine,
    "Media": applica_filtro_media,
    "Gaussiano": applica_filtro_gaussiano,
    "Laplaciano": applica_filtro_laplaciano,
    "Mediano": applica_filtro_mediano,
    "Wiener": applica_filtro_wiener,
    "Bilaterale": applica_filtro_bilaterale
}

# Funzione per salvare l'immagine filtrata
def salva_immagine(immagine, nome_filtro, parametri):
    # Crea la directory di salvataggio nella stessa posizione del codice, se non esiste
    cartella_salvataggio = os.path.join(os.path.dirname(__file__), "Elaborazione_Immagini")
    if not os.path.exists(cartella_salvataggio):
        os.makedirs(cartella_salvataggio)
    nome_file = os.path.join(cartella_salvataggio, f"{nome_filtro}_{parametri}.png")
    cv2.imwrite(nome_file, immagine)  # Salva l'immagine
    aggiorna_menu_tendina()  # Aggiorna il menu a tendina dopo il salvataggio

# Funzione per ridimensionare l'immagine a una dimensione fissa
def ridimensiona_immagine(immagine, dimensione=DIMENSIONE_FISSA):
    return cv2.resize(immagine, dimensione)

# Funzione per caricare e visualizzare l'immagine principale
def carica_immagine():
    percorso_file = filedialog.askopenfilename()  # Apre una finestra di dialogo per scegliere il file
    if percorso_file:
        global immagine_originale, immagine_selezionata, immagine_filtrata
        immagine_originale = cv2.imread(percorso_file)  # Legge l'immagine dal percorso selezionato
        immagine_originale = ridimensiona_immagine(immagine_originale)  # Ridimensiona l'immagine
        immagine_selezionata = immagine_originale.copy()  # Crea una copia dell'immagine originale
        immagine_filtrata = None  # Inizializza l'immagine filtrata come None
        visualizza_immagini()  # Visualizza le immagini

# Funzione per aggiornare l'immagine selezionata dal menu a tendina
def aggiorna_immagine_selezionata(*args):
    percorso_immagine_selezionata = os.path.join(os.path.dirname(__file__), "Elaborazione_Immagini", menu_tendina.get())
    if os.path.exists(percorso_immagine_selezionata):
        global immagine_selezionata, immagine_filtrata
        immagine_selezionata = cv2.imread(percorso_immagine_selezionata)  # Legge l'immagine dal percorso selezionato
        immagine_selezionata = ridimensiona_immagine(immagine_selezionata)  # Ridimensiona l'immagine
        immagine_filtrata = None  # Inizializza l'immagine filtrata come None
        visualizza_immagini()  # Visualizza le immagini

# Funzione per applicare il filtro selezionato all'immagine
def applica_filtro():
    filtro_selezionato = var_filtro.get()  # Ottiene il filtro selezionato dal menu a tendina
    if immagine_selezionata is not None and filtro_selezionato in filtri:
        global immagine_filtrata
        immagine_filtrata = filtri[filtro_selezionato](immagine_selezionata)  # Applica il filtro selezionato
        immagine_filtrata = ridimensiona_immagine(immagine_filtrata)  # Ridimensiona l'immagine filtrata
        salva_immagine(immagine_filtrata, filtro_selezionato, "5x5")  # Salva l'immagine filtrata
        visualizza_immagini()  # Visualizza le immagini

# Funzione per visualizzare le immagini nel frame dedicato
def visualizza_immagini():
    for widget in frame_immagini.winfo_children():
        widget.destroy()  # Rimuove tutti i widget esistenti nel frame

    # Visualizza l'immagine originale
    if immagine_originale is not None:
        visualizza_immagine(immagine_originale, frame_immagini)

    # Visualizza l'immagine selezionata dal menu a tendina
    if immagine_selezionata is not None:
        visualizza_immagine(immagine_selezionata, frame_immagini)

    # Visualizza l'immagine con il filtro applicato
    if immagine_filtrata is not None:
        visualizza_immagine(immagine_filtrata, frame_immagini)

# Funzione per visualizzare un'immagine in un frame specifico
def visualizza_immagine(immagine, frame):
    b, g, r = cv2.split(immagine)  # Divide l'immagine nei canali BGR
    img = cv2.merge((r, g, b))  # Ricompone l'immagine nei canali RGB
    img = Image.fromarray(img)  # Converte l'immagine in un oggetto PIL
    img = ImageTk.PhotoImage(img)  # Converte l'immagine PIL in un oggetto ImageTk
    
    pannello = tk.Label(frame, image=img)  # Crea un widget Label con l'immagine
    pannello.image = img  # Salva una referenza dell'immagine per evitare la garbage collection
    pannello.pack(side="left", padx=10, pady=10)  # Posiziona il widget Label nel frame

# Funzione per aggiornare il menu a tendina con i file salvati
def aggiorna_menu_tendina():
    cartella_salvataggio = os.path.join(os.path.dirname(__file__), "Elaborazione_Immagini")
    if os.path.exists(cartella_salvataggio):
        lista_file = os.listdir(cartella_salvataggio)  # Ottiene la lista dei file nella cartella di salvataggio
        menu_tendina['values'] = lista_file  # Imposta i valori del menu a tendina
        menu_tendina.set("Seleziona input")  # Imposta il valore predefinito del menu a tendina

# Funzione per svuotare la cartella di salvataggio
def svuota_cartella():
    cartella_salvataggio = os.path.join(os.path.dirname(__file__), "Elaborazione_Immagini")
    if os.path.exists(cartella_salvataggio):
        for file in os.listdir(cartella_salvataggio):
            file_path = os.path.join(cartella_salvataggio, file)
            if os.path.isfile(file_path):
                os.remove(file_path)  # Rimuove il file
        aggiorna_menu_tendina()  # Aggiorna il menu a tendina dopo aver svuotato la cartella

# Variabili per le immagini
immagine_originale = None
immagine_selezionata = None
immagine_filtrata = None

# Creazione dell'interfaccia grafica
finestra = tk.Tk()  # Crea una finestra principale
finestra.title("Elaborazione Immagini")  # Imposta il titolo della finestra

# Frame per i pulsanti
frame_pulsanti = tk.Frame(finestra)  # Crea un frame per i pulsanti
frame_pulsanti.pack(pady=20)  # Posiziona il frame nella finestra con padding verticale

bottone_carica = tk.Button(frame_pulsanti, text="Carica Immagine", command=carica_immagine)  # Crea un pulsante per caricare l'immagine
bottone_carica.pack(side="left", padx=5)  # Posiziona il pulsante nel frame con padding orizzontale

var_filtro = tk.StringVar()  # Crea una variabile StringVar per il menu dei filtri
var_filtro.set("Filtri")  # Imposta un filtro predefinito

menu_filtri = tk.OptionMenu(frame_pulsanti, var_filtro, *filtri.keys())  # Crea un menu a tendina con i filtri disponibili
menu_filtri.pack(side="left", padx=5)  # Posiziona il menu a tendina nel frame con padding orizzontale

bottone_applica = tk.Button(frame_pulsanti, text="Applica Filtro", command=applica_filtro)  # Crea un pulsante per applicare il filtro
bottone_applica.pack(side="left", padx=5)  # Posiziona il pulsante nel frame con padding orizzontale

menu_tendina = ttk.Combobox(frame_pulsanti, state="readonly")  # Crea un menu a tendina per le immagini salvate
menu_tendina.pack(side="left", padx=5)  # Posiziona il menu a tendina nel frame con padding orizzontale
menu_tendina.bind("<<ComboboxSelected>>", aggiorna_immagine_selezionata)  # Associa un'azione al cambio di selezione nel menu a tendina

bottone_svuota = tk.Button(frame_pulsanti, text="Svuota Cartella", command=svuota_cartella)  # Crea un pulsante per svuotare la cartella
bottone_svuota.pack(side="left", padx=5)  # Posiziona il pulsante nel frame con padding orizzontale

# Controlla se la directory di salvataggio esiste e aggiorna il menu a tendina
if not os.path.exists(os.path.join(os.path.dirname(__file__), "Elaborazione_Immagini")):
    os.makedirs(os.path.join(os.path.dirname(__file__), "Elaborazione_Immagini"))
aggiorna_menu_tendina()

# Frame per visualizzare le immagini
frame_immagini = tk.Frame(finestra)  # Crea un frame per visualizzare le immagini
frame_immagini.pack()  # Posiziona il frame nella finestra

finestra.mainloop()  # Avvia il loop principale dell'interfaccia grafica
