# app/beregning/bjelke.py

"""Enkle beregninger for dimensjonering av bjelker."""

from math import pow


def beregn_bjelkehoyde(spenn_m, last_kN_per_m, material="tre"):
    """Beregn anbefalt bjelkehøyde i mm for en bjelke med jevnt fordelt last.

    Parametre
    ---------
    spenn_m: Lengde mellom bærepunkt i meter.
    last_kN_per_m: Last i kN per meter langs bjelken.
    material: Materialtype ("tre", "limtre" eller "stål").
    """
    materialstyrke = {"tre": 5.0, "limtre": 8.0, "stål": 20.0}
    f = materialstyrke.get(material.lower(), materialstyrke["tre"])

    # Forenklet bøyemoment for jevnt fordelt last: M = qL^2/8
    moment_kNm = last_kN_per_m * pow(spenn_m, 2) / 8

    # Antar bjelke med bredde = h/2 og formel M = f*h^3/12  [kN•m]
    h_cm = pow(12 * moment_kNm / f, 1 / 3)
    return round(h_cm * 10)  # Returner mm
