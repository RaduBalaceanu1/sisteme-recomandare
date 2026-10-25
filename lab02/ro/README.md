[← Înapoi la indexul general](../../README.md) | 🇬🇧 English Version TBA

**Acces Rapid:** [📄 Vezi `recombee_properties.py`](../recombee_properties.py)

---

# Laborator 2: Sistem de recomandare cu Recombee - înregistrare proprietăți

Pe parcursul următoarelor laboratoare veți lucra la dezvoltarea unui sistem de recomandare folosind platforma **Recombee**.

- **Link API oficial:** [Recombee API Reference](https://docs.recombee.com/api)
- **Limbajul de programare:** La alegere. *Recombee* pune la dispoziție SDK-uri oficiale în următoarele limbaje: JavaScript, Python, Java, Ruby, PHP, C#, Node.js.

## Cerințe preliminare

1. Asigurați-vă că ați configurat mediul virtual Python conform [Ghidului de instalare din rădăcină](../../README.md).
2. Asigurați-vă că aveți instalate pachetele din `requirements.txt`.
3. Aveți pregătit un browser web (ex.: Google Chrome, Mozilla Firefox, Safari).

## Cerințe de implementare

### 1. Alegerea dataset-ului

- **Volum:** Minim `100`, maxim `10K` de produse/item-uri (dacă setul inițial este prea mare, veți elimina rânduri).
- **Sursă:** Platforme de date deschise precum [Kaggle](https://www.kaggle.com/), [data.world](https://data.world/) sau site-uri similare.
- **Exemple de domenii:** Cărți, filme, muzică, electronice, produse de supermarket.
- **Proprietăți (Atribute):** Fiecare produs/item trebuie să aibă minimum `3` proprietăți definite (de ex., pentru laptopuri: nume, capacitate de stocare, preț).

### 2. Cont Recombee

Creați un cont în *Recombee* și oferiți acces profesorului în contul vostru astfel:

1. Intrați pe [Recombee Sign Up](https://www.recombee.com/) și creați-vă un cont gratuit (*Start Free*).
1. Intrați în contul vostru pe [Recombee Admin UI](https://admin.recombee.com/).
1. Mergeți în meniul din stânga la *Settings* => *Organization Users*.
1. Click pe *Invite User* și introduceți e-mailul indicat de profesor.
1. La secțiunea de permisiuni, bifați dreptul de *Edit* pe baza de date aferentă laboratorului (este necesar dreptul de *Edit* pentru ca profesorul să poată citi/genera cheile de test dacă scriptul dă erori de autentificare).

### 3. Înregistrarea atributelor în *Recombee*

- Folosind API-ul/SDK-ul oficial, implementați un script care transmite către *Recombee* numele proprietăților produselor și tipul lor de date (ex.: *string*, *int*, *double*, *boolean*, *timestamp*).

- **Notă:** Identificatorul unic al produsului (ex.: ID-ul din *Kaggle*) NU se înregistrează ca proprietate în catalog. *Recombee* îl gestionează nativ sub numele de `itemId` în momentul în care vom încărca produsele (în laboratorul următor).

#### Codul de pornire în *Python* (*boilerplate*)

Dacă veți lucra în *Python*, puteți porni  de la script-ul [📄 `recombee_properties.py`](../recombee_properties.py).

##### Instalare biblioteci

Înainte de a rula codul, trebuie să instalați  cele două biblioteci necesare din terminal:
```
pip install recombee-api-client pandas
```

##### Modificare cod

Modificați codul din fișier conform instrucțiunilor din `TODO`-uri, astfel încât să definiți în *Recombee* proprietățile aferente dataset-ului vostru.

### 4. Livrabile obligatorii

- **Repository:** Creați un repo public sau privat pe *GitHub*/*GitLab* în care urcați codul vostru sursă și dataset-ul folosit.
- **Documentație:** Creați un fișier `README.md` în care descrieți dataset-ul ales.
- **Predare:** Încărcați pe platforma Moodle un fișier cu extensie `.txt` care conține exclusiv link-ul către repository-ul vostru.

## Barem de notare

| Nr. | Criteriu    | Punctaj |
| - | -------- | ------- |
| 1 | Existența și validitatea dataset-ului (fișier `CSV` cu `100`-`10K` de intrări) | 30p |
| 2 | Documentația setului de date (`README.md`): conține descrierea domeniului ales, listează explicit minim 3 proprietăți și tipul lor. | 20p |
| 3 | Script-ul Python (sau în alt limbaj) funcțional și adaptat | 30p |
| 4 | Integrarea proprietăților în Recombee | 20p |
