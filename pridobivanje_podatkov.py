import requests
import time

# Seznam valut, ki jih primerjamo z EUR:
# USD - ameriski dolar
# GBP - britanski funt     
# CHF - svicarski frank               
# JPY - japonski jen                
# AUD - avstralski dolar
# CAD - kanadski dolar                 
# CNY - kitajski juan          
# TRY - turska lira                    
# ZAR - juznoafriski rand      
# BRL - brazilski real  
BAZNA_VALUTA = "EUR"    
VALUTE = ["USD", "GBP", "CHF", "JPY", "AUD", "CAD", "CNY", "TRY", "ZAR", "BRL"]

LETA = range(2016, 2026) 

def pridobi_stran(valuta, leto):
    #Poslje zahtevek na stran in shrani surov HTML odgovor v datoteko
    url = f"https://www.x-rates.com/average/?from={BAZNA_VALUTA}&to={valuta}&amount=1&year={leto}"
    odziv = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

    ime_datoteke = f"surovi_podatki/valuta_{valuta}_{leto}.html"
    with open(ime_datoteke, "w", encoding="utf-8") as f:
        f.write(odziv.text)

    return odziv.status_code


def pridobi_vse_strani():
    #Pridobi in shrani surove HTML strani za vse valute in vsa leta
    for valuta in VALUTE:
        for leto in LETA:
            print(f"Pridobivam {valuta} za leto {leto}...")
            koda = pridobi_stran(valuta, leto)
            if koda != 200:
                print(f"  Opozorilo: strežnik je vrnil kodo {koda}")
            time.sleep(0.5)

    print("Vse strani so shranjene v mapi surovi_podatki/")


pridobi_vse_strani()