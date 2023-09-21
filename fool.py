from dataclasses import dataclass, asdict
import json


@dataclass
class C:
    x: int
    y: int


a = C(1, 3)
print(json.dumps(asdict(a)))
