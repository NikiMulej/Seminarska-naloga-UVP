from bs4 import BeautifulSoup
import csv
import os

MESCI_KRATICE = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
MESEC_STEVILKA = {ime: i + 1 for i, ime in enumerate(MESCI_KRATICE)}

def razcleni_datoteko(pot_do_datoteke, valuta, leto):
    #Prebere shranjeno HTML datoteko in izlusci mesecna povprecja
    with open(pot_do_datoteke, "r", encoding="utf-8") as f:
        vsebina = f.read()

    juha = BeautifulSoup(vsebina, "html.parser")

    meseci_spani = juha.find_all("span", class_="avgMonth")
    tecaji_spani = juha.find_all("span", class_="avgRate")

    rezultati = []
    for mesec_span, tecaj_span in zip(meseci_spani, tecaji_spani):
        mesec_kratica = mesec_span.get_text(strip=True)
        vrednost = tecaj_span.get_text(strip=True)

        if mesec_kratica not in MESEC_STEVILKA:
            continue

        rezultati.append({
            "valuta": valuta,
            "leto": leto,
            "mesec": MESEC_STEVILKA[mesec_kratica],
            "menjalni_tecaj": float(vrednost),
        })

    return rezultati[:12]


def obdelaj_vse_datoteke():
    #Preide čez vse shranjene HTML datoteke in jih zbere v en CSV
    vse_vrstice = []
    mapa = "surovi_podatki"

    for ime_datoteke in sorted(os.listdir(mapa)):
        if not ime_datoteke.endswith(".html"):
            continue

        deli = ime_datoteke.replace(".html", "").split("_")
        valuta = deli[1]
        leto = int(deli[2])

        pot = os.path.join(mapa, ime_datoteke)
        vrstice = razcleni_datoteko(pot, valuta, leto)
        vse_vrstice.extend(vrstice)
        print(f"Obdelano: {ime_datoteke} -> {len(vrstice)} vrstic")

    with open("podatki/valute.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["valuta", "leto", "mesec", "menjalni_tecaj"])
        writer.writeheader()
        for vrstica in vse_vrstice:
            writer.writerow(vrstica)

    print(f"Shranjenih {len(vse_vrstice)} vrstic v podatki/valute.csv")


obdelaj_vse_datoteke()