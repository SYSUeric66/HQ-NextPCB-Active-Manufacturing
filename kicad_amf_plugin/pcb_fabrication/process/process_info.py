from dataclasses import dataclass


@dataclass
class ProcessInfo:
    bheight: str  # PCB Thickness
    copper: str  # Finished Copper Weight
    insidecopper: str = '0'  # Inner Copper Weight
    pressing: str = ''  # Stack up
    lineweight: str  # Min Trace/Space Outer
    vias: str  # Min Drilled Hole
    color: str  # Solder Mask Color
    charcolor: str  # Silkscreen
    cover: str  # Via Process
    spray: str  # Surface Finish
    cjh: str or None  # SurfaceProcessCtrl
