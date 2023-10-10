from dataclasses import dataclass


@dataclass
class SpecialProcessModel:
    impendance: str  # Impendance
    bankong: str  # Plated Half Holes:
    blind: str  # HDI(Buried/blind vias):
    via_in_pad: str  # Pad Hole:
    beveledge: str  # Beveling of G/F:
    pressing: str = ''  # Stack up
