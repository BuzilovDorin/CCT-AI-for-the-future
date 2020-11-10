# ---:> DATACLASSES <:---
# example
import datetime
from dataclasses import dataclass

@dataclass
class mushroom:
    name: str
    color: str
    capSize: int
    capShape: str
    stemLenght: int
    stemShape: str
    Active: bool

    def isActive(self):
        return(Active)

goldenmushroom = mushroom("Golden Teacher", "gold", 3, "open", 5, ['long', 'straight'], True)

print(f"This {goldenmushroom.name} is a {goldenmushroom.Active} Active mushroom")

