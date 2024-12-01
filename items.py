from typing import Dict, TypedDict
from BaseClasses import Item, ItemClassification

class SS2item(Item):
    game = "System Shock 2"

class ItemDict(TypedDict):
    id: int
    classification: ItemClassification
    count: int
    option: str
    group: str


SS2items: Dict[str, ItemDict] = {
    "Dead Power Cell": {"id": 45002,
            "classification": ItemClassification.progression,
            "count": 2,
            "option": "",
            "group": ""
                      },
    "Shotgun": {"id": 45004,
            "classification": ItemClassification.progression,
            "count": 1,
            "option": "",
            "group": "Shotgun"
                      },
    "Conventional Weapon Upgrade": {"id": 45006,
            "classification": ItemClassification.progression,
            "count": 3,
            "option": "",
            "group": ""
                      },
    "Eng Access Audio Log": {"id": 45008,
            "classification": ItemClassification.progression,
            "count": 1,
            "option": "",
            "group": ""
                      },
    "Hydroponics Sector A access card": {"id": 45010,
            "classification": ItemClassification.progression,
            "count": 1,
            "option": "",
            "group": ""
                      },
    "Hydroponics Sector D access card": {"id": 45012,
            "classification": ItemClassification.progression,
            "count": 1,
            "option": "",
            "group": ""
                      },
    "45m/dEx circuit board": {"id": 45014,
            "classification": ItemClassification.progression,
            "count": 1,
            "option": "",
            "group": ""
                      },
    "Fluidics Control Access Audio Log": {"id": 45016,
            "classification": ItemClassification.progression,
            "count": 1,
            "option": "",
            "group": ""
                      },
    "Toxin-A": {"id": 45018,
            "classification": ItemClassification.progression,
            "count": 4,
            "option": "",
            "group": ""
                      },
    "Vanadium": {"id": 45020,
            "classification": ItemClassification.progression,
            "count": 1,
            "option": "",
            "group": ""
                      },
    "Antimony": {"id": 45022,
            "classification": ItemClassification.progression,
            "count": 2,
            "option": "",
            "group": ""
                      },
    "Research": {"id": 45024,
            "classification": ItemClassification.progression,
            "count": 1,
            "option": "",
            "group": "Research"
                      },
    "Quantum Simulation chip": {"id": 45026,
            "classification": ItemClassification.progression,
            "count": 1,
            "option": "",
            "group": ""
                      },
    "Linear Simulation chip": {"id": 45028,
            "classification": ItemClassification.progression,
            "count": 1,
            "option": "",
            "group": ""
                      },
    "Interpolated Simulation chip": {"id": 45030,
            "classification": ItemClassification.progression,
            "count": 1,
            "option": "",
            "group": ""
                      },
    "Deck 5 Crew access card": {"id": 45032,
            "classification": ItemClassification.progression,
            "count": 1,
            "option": "",
            "group": ""
                      },
    "Athletics access card": {"id": 45034,
            "classification": ItemClassification.progression,
            "count": 1,
            "option": "",
            "group": ""
                      },
    "Ops Override access card": {"id": 45036,
            "classification": ItemClassification.progression,
            "count": 1,
            "option": "",
            "group": ""
                      },
    "Rickenbacker access Card": {"id": 45038,
            "classification": ItemClassification.progression,
            "count": 1,
            "option": "",
            "group": ""
                      },
}