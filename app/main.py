# app/main.py

from beregning.areal import beregn_veggareal

def hovedmeny():
    print("=== Håndverker Assistent ===")
    print("1. Beregn veggareal")
    print("2. Avslutt")
    
    valg = input("Velg et alternativ: ")
    
    if valg == "1":
        bredde = float(input("Bredde på vegg (i meter): "))
        høyde = float(input("Høyde på vegg (i meter): "))
        antall = int(input("Antall vegger: "))
        areal = beregn_veggareal(bredde, høyde, antall)
        print(f"\nTotalt veggareal: {areal:.2f} m²\n")
    else:
        print("Avslutter.")

if __name__ == "__main__":
    hovedmeny()
