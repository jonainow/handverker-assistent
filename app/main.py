# app/main.py

from beregning.areal import beregn_veggareal
from beregning.materialmengde import beregn_antall_plater
from beregning.materialvalg import anbefal_materiale



def hovedmeny():
    print("=== Håndverker Assistent ===")
    print("1. Beregn veggareal")
    print("2. Beregn antall gipsplater")
    print("3. Avslutt")
    print("3. Anbefal materiale")
    print("4. Avslutt")


    valg = input("Velg et alternativ: ")

    if valg == "1":
        bredde = float(input("Bredde på vegg (i meter): "))
        høyde = float(input("Høyde på vegg (i meter): "))
        antall = int(input("Antall vegger: "))
        areal = beregn_veggareal(bredde, høyde, antall)
        print(f"\nTotalt veggareal: {areal:.2f} m²\n")

    elif valg == "2":
        areal = float(input("Oppgitt areal (i m²): "))
        plater = beregn_antall_plater(areal)
        print(f"\nDu trenger ca. {plater} plater (inkl. 10 % ekstra).\n")

    elif valg == "3":
        konstruksjon = input("Hva skal du bygge? (innervegg, yttervegg, bærende vegg, tak): ")
        miljø = input("Miljø (tørt, våtrom, utendørs): ")
        anbefaling = anbefal_materiale(konstruksjon, miljø)
        print(f"\n{anbefaling}\n")

    elif valg == "4":
        print("Avslutter.")



if __name__ == "__main__":
    hovedmeny()
