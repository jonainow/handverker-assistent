# app/main.py

from beregning.areal import beregn_veggareal
from beregning.materialmengde import beregn_antall_plater


def hovedmeny():
    print("=== Håndverker Assistent ===")
    print("1. Beregn veggareal")
    print("2. Beregn antall gipsplater")
    print("3. Avslutt")

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

    else:
        print("Avslutter.")


if __name__ == "__main__":
    hovedmeny()
