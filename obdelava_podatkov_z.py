from bs4 import BeautifulSoup
import csv
import os

def razcleni_datoteko_zlata(pot_do_datoteke, leto, mesec):
    #Prebere shranjeno HTML datoteko in izracuna mesecno povprecje cene zlata
    with open(pot_do_datoteke, "r", encoding="utf-8") as f:
        vsebina = f.read()

    juha = BeautifulSoup(vsebina, "html.parser")
    tabela = juha.find("table")

    if tabela is None:
        return None

    dnevne_cene = []
    vrstice = tabela.find_all("tr")

    for vrstica in vrstice[1:]:
        celice = vrstica.find_all("td")
        if len(celice) < 2:
            continue

        besedilo_cene = celice[1].get_text(strip=True)
        # odstranimo znak $ in vejice za tisočice, npr. "$1,592.30" -> "1592.30"
        besedilo_cene = besedilo_cene.replace("$", "").replace(",", "")

        try:
            cena = float(besedilo_cene)
            dnevne_cene.append(cena)
        except ValueError:
            continue

    if not dnevne_cene:
        return None

    povprecje = sum(dnevne_cene) / len(dnevne_cene)
    return {
        "leto": leto,
        "mesec": mesec,
        "cena_zlata": round(povprecje, 2),
    }


def obdelaj_vse_datoteke_zlata():
    #Preide cez vse shranjene HTML datoteke zlata in jih zbere v en CSV
    vse_vrstice = []
    mapa = "surovi_podatki"

    for ime_datoteke in sorted(os.listdir(mapa)):
        if not ime_datoteke.startswith("zlato_") or not ime_datoteke.endswith(".html"):
            continue

        del_imena = ime_datoteke.replace("zlato_", "").replace(".html", "")
        leto_str, mesec_str = del_imena.split("-")
        leto = int(leto_str)
        mesec = int(mesec_str)

        pot = os.path.join(mapa, ime_datoteke)
        vrstica = razcleni_datoteko_zlata(pot, leto, mesec)

        if vrstica is None:
            print(f"Opozorilo: {ime_datoteke} ni vrnila podatkov")
            continue

        vse_vrstice.append(vrstica)
        print(f"Obdelano: {ime_datoteke} -> povprecje {vrstica['cena_zlata']}")

    with open("podatki/zlato.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["leto", "mesec", "cena_zlata"])
        writer.writeheader()
        for vrstica in vse_vrstice:
            writer.writerow(vrstica)

    print(f"Shranjenih {len(vse_vrstice)} vrstic v podatki/zlato.csv")


obdelaj_vse_datoteke_zlata()