""" assumptions
    calculating MS from the leather/hunter cowl build when not near an ally
    calculating MS from winged blade when not slowed
"""
from movement_speed import ms_calculator

class Item:
    def __init__(self, name, ms, starter = False, upgrade = False):
        self.name = name
        self.ms = ms
        self.starter = starter
        self.upgrade = upgrade

TYR_BASE_MS = 375

HUNTERS_COWL = [
    Item('leather cowl', 5, True),
    Item('warrior tabi', 18),
    Item('shifters shield', 0),
    Item('witchblade', 7),
    Item('relic dagger', 7),
    Item('hunters cowl', 10, True, True),
    Item('winged blade', 7),
]

print(ms_calculator(TYR_BASE_MS, HUNTERS_COWL))
