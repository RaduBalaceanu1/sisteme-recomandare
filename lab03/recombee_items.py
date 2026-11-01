import os
from pathlib import Path

import pandas as pd
from recombee_api_client.api_client import RecombeeClient, Region
from recombee_api_client.api_requests import SetItemValues, Batch
from recombee_api_client.exceptions import APIException

# TODO 1: Configurare credentiale Recombee (la fel ca la Lab 02)
DB_NAME = 'radu-balaceanu-lab-dev'
PRIVATE_TOKEN = os.environ["RECOMBEE_PRIVATE_TOKEN"]
REGION = Region.EU_WEST

client = RecombeeClient(DB_NAME, PRIVATE_TOKEN, region=REGION)

# TODO 2: Incarcarea aceluiasi dataset folosit la Lab 02
PATH_DATASET = (
    Path(__file__).resolve().parent.parent / "lab02" / "movies.csv"
)


def send_batch(requests):
    """Trimite lotul si verifica rezultatul fiecarui item."""
    results = client.send(Batch(requests))

    if len(results) != len(requests):
        raise RuntimeError("Raspuns incomplet pentru lotul trimis.")

    errors = [
        (request.item_id, result)
        for request, result in zip(requests, results)
        if not 200 <= result["code"] < 300
    ]

    if errors:
        for item_id, result in errors[:5]:
            print(f"Eroare la item-ul {item_id}: {result}")

        raise RuntimeError(
            f"Lotul contine {len(errors)} erori. Incarcarea este oprita."
        )


def send_items():
    """Functie care citeste dataset-ul si trimite item-urile in Recombee"""
    df = pd.read_csv(PATH_DATASET, dtype={"id": "string"})

    # Verificam datele inainte de trimitere
    required_columns = [
        "id", "title", "genres", "vote_average", "vote_count",
        "popularity", "runtime", "cast", "director", "keywords"
    ]

    missing_columns = set(required_columns) - set(df.columns)
    if missing_columns:
        raise ValueError(f"Lipsesc coloanele: {sorted(missing_columns)}")

    if not 100 <= len(df) <= 10000:
        raise ValueError("Dataset-ul trebuie sa contina 100–10.000 de item-uri.")

    df["id"] = df["id"].str.strip()

    if (
        df["id"].isna().any()
        or df["id"].eq("").any()
        or df["id"].duplicated().any()
    ):
        raise ValueError("ID-urile trebuie sa fie completate si unice.")

    if df["title"].isna().any():
        raise ValueError("Exista filme fara titlu.")

    # Verificam coloanele numerice inainte de primul lot
    for column in ["vote_average", "vote_count", "popularity", "runtime"]:
        df[column] = pd.to_numeric(df[column], errors="raise")

    if (df["vote_count"].dropna() % 1 != 0).any():
        raise ValueError("vote_count trebuie sa contina numere intregi.")

    print(f"Se trimit {len(df)} item-uri in Recombee...")

    requests = []
    total_sent = 0

    for index, row in df.iterrows():
        # TODO 3: Extrageti ID-ul unic al produsului din coloana corespunzatoare din CSV
        item_id = str(row['id'])

        # TODO 4: Mapati proprietatile definite anterior cu valorile din randul curent
        # Tipurile corespund proprietatilor definite la laboratorul 2
        property_types = {
            "title": str,
            "genres": str,
            "vote_average": float,
            "vote_count": int,
            "popularity": float,
            "runtime": float,
            "cast": str,
            "director": str,
            "keywords": str,
        }

        # Omitem valorile lipsa, fara sa eliminam filmele
        properties = {
            name: convert(row[name])
            for name, convert in property_types.items()
            if pd.notna(row[name])
        }

        # Adaugam request-ul de setare a valorilor pentru item
        # (SetItemValues creeaza automat item-ul daca acesta nu exista)
        requests.append(SetItemValues(item_id, properties, cascade_create=True))

        # Trimitem in loturi (batch) de cate 100 pentru eficienta
        if len(requests) == 100:
            send_batch(requests)
            total_sent += len(requests)
            requests = []
            print(f"Item-uri confirmate: {total_sent}/{len(df)}")

    # Trimitem si restul ramase (daca numarul total nu e multiplu de 100)
    if requests:
        send_batch(requests)
        total_sent += len(requests)
        print(f"Item-uri confirmate: {total_sent}/{len(df)}")

    print(f"Toate cele {total_sent} item-uri au fost trimise cu succes!")


if __name__ == "__main__":
    send_items()