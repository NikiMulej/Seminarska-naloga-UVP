import requests
import time

LETA = range(2016, 2026)
MESECI = range(1, 13)

def pridobi_stran_zlata(leto, mesec):
    #Pošlje zahtevek na stran za dano leto/mesec in shrani surov HTML odgovor
    mesec_str = f"{mesec:02d}"
    url = f"https://goldpricetracker.com/history/{leto}-{mesec_str}/"
    odziv = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

    ime_datoteke = f"surovi_podatki/zlato_{leto}-{mesec_str}.html"
    with open(ime_datoteke, "w", encoding="utf-8") as f:
        f.write(odziv.text)

    return odziv.status_code


def pridobi_vse_strani_zlata():
    #Pridobi in shrani surove HTML-je, strani za ceno zlata za vsa leta in mesece
    for leto in LETA:
        for mesec in MESECI:
            print(f"Pridobivam zlato za {leto}-{mesec:02d}...")
            koda = pridobi_stran_zlata(leto, mesec)
            if koda != 200:
                print(f"  Opozorilo: streznik je vrnil kodo {koda}")
            time.sleep(0.5)

    print("Vse strani so shranjene v mapi surovi_podatki/")


pridobi_vse_strani_zlata()