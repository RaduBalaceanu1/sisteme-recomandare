# Laborator 2 – Catalog de filme în Recombee

Autor: Balaceanu Radu

## Dataset

Proiectul utilizează fișierul `movies.csv`, care conține
4.803 înregistrări despre filme și 24 de coloane.

Sursa: https://www.kaggle.com/datasets/abdallahwagih/movies

Datele includ titluri, genuri, note medii, popularitate,
durată, actori, regizori și cuvinte-cheie.

Pentru acest laborator se păstrează fișierul CSV original.
Unele proprietăți au valori lipsă; acestea vor fi tratate
înainte de încărcarea filmelor într-un laborator ulterior.

## Proprietăți definite în Recombee

| Proprietate | Tip | Descriere |
|---|---|---|
| title | string | Titlul filmului |
| genres | string | Genurile filmului, păstrate ca text |
| vote_average | double | Nota medie |
| vote_count | int | Numărul de voturi |
| popularity | double | Indicatorul de popularitate din dataset |
| runtime | double | Durata în minute |
| cast | string | Actorii, păstrați ca text |
| director | string | Regizorul |
| keywords | string | Cuvintele-cheie, păstrate ca text |

Coloana `id` identifică filmele și nu este înregistrată
ca proprietate. La încărcarea ulterioară va fi utilizată
pentru `itemId`. Coloana `index` reprezintă numerotarea
rândurilor și nu este înregistrată ca proprietate.

## Instalare

Este necesar Python. Din folderul care conține scriptul:

```powershell
python -m pip install recombee-api-client pandas
```

## Configurare și rulare

Fișierul `movies.csv` trebuie să fie în același folder
cu `recombee_properties.py`.

În script, configurați `DB_NAME` pentru baza Recombee.
Regiunea utilizată este `Region.EU_WEST`.

În PowerShell, setați cheia privată pentru baza respectivă:

```powershell
$env:RECOMBEE_PRIVATE_TOKEN = 'CHEIA_TA_PRIVATA'
```

Rulați în același terminal, folosind mediul Python
în care au fost instalate bibliotecile:

```powershell
python .\recombee_properties.py
```

Cheia privată nu este inclusă în repository.

## Funcționare și rezultat

Scriptul citește CSV-ul, afișează numărul de înregistrări,
creează proprietățile prin `AddItemProperty` și verifică
schema prin `ListItemProperties`.

Rularea efectuată a confirmat citirea celor 4.803 înregistrări
și existența tuturor celor 9 proprietăți cu tipurile definite.

În acest laborator se înregistrează doar schema catalogului.
Filmele și interacțiunile utilizatorilor nu sunt încărcate.