from dataclasses import dataclass, asdict
import json
from enum import Enum


@dataclass
class A:
    bcc: str = 'alex'
    cc: str = 'alice'


@dataclass
class C(A):
    x: int = 1
    y: int = 2


a = C(None, None)
print(json.dumps(asdict(a)))
