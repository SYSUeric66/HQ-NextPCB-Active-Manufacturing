from dataclasses import dataclass


@dataclass
class PersonalizedInfo:
    test: str  # Electrical Test
    shipment_report: str  # Delivery Report
    slice_report: str  # Microsection Analysis Report
    report_type: str  # Report Format
    beveledge: str  # Beveling of G/F
    review_file: str  # Approve Working Gerber:
    has_period: str  # Decided by period_format
    period_format: str or None  # UL Mark
    film_report: str  # Film
    pcb_note: str  # Special Requests
