[← Înapoi la indexul general](../../README.md) | 🇬🇧 English Version TBA

**Acces Rapid:** [📄 Vezi `track.py`](../track.py)

---

# Laborator 1: Colectarea datelor implicite în sistemele de recomandare

În sistemele de recomandare moderne, o mare parte din date sunt colectate implicit — fără ca utilizatorul să introducă manual note sau calificative. În acest laborator, veți rula un server local în Python care extrage metadatele contextuale transmise prin protocolul HTTP (IP, profil dispozitiv, limbi preferate) și veți efectua o cerere de test utilizând browser-ul web.

## Cerințe preliminare

1. Asigurați-vă că ați configurat mediul virtual Python conform [Ghidului de instalare din rădăcină](../../README.md).
2. Asigurați-vă că aveți instalate pachetele din `requirements.txt`.
3. Aveți pregătit un browser web (ex.: Google Chrome, Mozilla Firefox, Safari).

## Instrucțiuni de rulare

### 1. Porniți serverul din terminal

Asigurați-vă că ați descărcat fișierul [📄 `track.py`](../track.py) în directorul `lab01`, apoi rulați-l din terminal:

```bash
python track.py
```

### 2. Accesați în browser următoarea adresă web:

- URL: `http://127.0.0.1:5000`

### 3. Completați numele complet în câmpul din formularul web care apare

Datele nu pleacă de pe calculatorul vostru. Server-ul rulează doar local.

### 4. Trimiteți cererea (click pe *Send*) și salvați răspunsul JSON primit

Salvația răspunsul JSON într-un fișier numit `track_Nume_Prenume.json` 

## Instrucțiuni de predare

Încărcați fișierul creat anterior pe platforma Moodle.

## Exemplu de output

Mai jos aveți un exemplu de output cu caracter demonstrativ. Output-ul final va fi diferit, în funcție de dispozitivul dvs. și de datele completate în formular.

```
{
  "device_context": {
    "browser": "Chrome 154.0.0",
    "device_type": "Desktop",
    "os": "Mac OS X 10.15.7",
    "raw_user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36"
  },
  "network": {
    "ip_address": "127.0.0.1"
  },
  "run_info": {
    "timestamp": 1791359394,
    "verification_hash": "c5d64b26b4b0"
  },
  "student": "Popescu Ion",
  "user_preferences_implicit": {
    "preferred_language": "en-US"
  }
}
```
