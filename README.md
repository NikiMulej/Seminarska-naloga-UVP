# Seminarska naloga - UVP

Program pridobi zgodovinske podatke o menjalnih tečajih 10 svetovnih valut 
(proti EUR) in ceni zlata za obdobje 2016-2025. Podatke shrani, obdela in 
analizira ter raziskuje volatilnost valut, vpliv pandemije covid-19, 
korelacijo med zlatom in valutami ter razlike med celinami. Rezultati so 
predstavljeni v Jupyter Notebooku z grafi in razlagami.

## Struktura projekta

- `pridobivanje_podatkov.py` - zajem HTML strani s tečaji valut (x-rates.com)
- `obdelava_podatkov.py` - obdelava HTML strani v podatki/valute.csv
- `pridobivanje_zlata.py` - zajem HTML strani s ceno zlata (goldpricetracker.com)
- `obdelava_zlata.py` - obdelava HTML strani v podatki/zlato.csv
- `podatki/drzave.csv` - ročno pripravljena tabela z državami, celinami in prebivalstvom
- `analiza.ipynb` - glavna analiza in vizualizacija podatkov

## Zagon

1. Namesti potrebne knjižnice:
```
pip install requests beautifulsoup4 pandas matplotlib
```
2. Poženi zajem in obdelavo podatkov (v tem vrstnem redu):
```
python pridobivanje_podatkov.py
python obdelava_podatkov.py
python pridobivanje_zlata.py
python obdelava_zlata.py
```
3. Odpri `analiza.ipynb` in poženi vse celice (Run All)