from dataclasses import dataclass

from model.sighting import Sighting
from model.state import State


@dataclass
class Edge:
    S1: id
    S2: id
