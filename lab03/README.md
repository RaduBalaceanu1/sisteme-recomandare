# Laborator 3 – Încărcarea filmelor în Recombee

Autor: Balaceanu Radu

## Dataset și configurare

Este utilizat același dataset ca la laboratorul 2:
`../lab02/movies.csv`, cu 4.803 filme.

Sursa: https://www.kaggle.com/datasets/abdallahwagih/movies

Datele sunt încărcate în baza Recombee `radu-balaceanu-lab-dev`,
regiunea `Region.EU_WEST`.

## Prelucrarea datelor

- Coloana `id` este citită ca text și mapată la `itemId`.
- Sunt verificate existența coloanelor și unicitatea ID-urilor.
- Proprietățile numerice sunt convertite la tipurile corespunzătoare.
- Proprietățile cu valori lipsă sunt omise; filmele sunt păstrate.
- Sunt trimise cele 9 proprietăți definite în laboratorul 2:
  title, genres, vote_average, vote_count, popularity,
  runtime, cast, director și keywords.

## Trimiterea datelor

Scriptul utilizează SDK-ul oficial Recombee:
- `SetItemValues`, cu `cascade_create=True`;
- `Batch`, cu maximum 100 de item-uri într-un lot.

Este verificat rezultatul fiecărei cereri din lot.
În cazul unei erori, încărcarea se oprește și afișează detalii.

## Rulare

Instalați bibliotecile în mediul Python folosit:

```powershell
python -m pip install recombee-api-client pandas
```

Din folderul principal al repository-ului, setați cheia privată
și rulați scriptul în același terminal:

```powershell
$env:RECOMBEE_PRIVATE_TOKEN = 'CHEIA_TA_PRIVATA'
python .\lab03\recombee_items.py
```

Cheia privată nu este inclusă în repository.

## Rezultat și verificare

Au fost încărcate cu succes 4.803 filme în 49 de loturi:
48 de loturi a câte 100 și un ultim lot de 3.

În Recombee Admin UI → Items s-a verificat vizual
existența celor 4.803 item-uri și afișarea atributelor.