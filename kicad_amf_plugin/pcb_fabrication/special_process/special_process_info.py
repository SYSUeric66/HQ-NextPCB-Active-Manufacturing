from dataclasses import dataclass


@dataclass
class SpecialProcessInfo:
    impendance: str  # Impendance
    bankong: str  # Plated Half Holes:
    blind: str  # HDI(Buried/blind vias):
    via_in_pad: str  # Pad Hole:
