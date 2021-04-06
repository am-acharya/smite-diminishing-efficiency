""" assumptions
    calculating MS from the leather/hunter cowl build when not near an ally
    calculating MS from winged blade when not slowed
"""
from movement_speed import ms_calculator
from item import Item

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

def ms_growth_tracker(base_ms, build_path):
    ms_range = []
    item_list = []
    filtered_build_path = [item for item in build_path if isinstance(item, Item)]
    for new_item in filtered_build_path:
        if(new_item.is_starter_upgrade()):
            # TODO append starter upgrade even if starter is not found
            item_list[:] = [new_item if old_item.is_starter() else old_item for old_item in item_list]
        else:
            item_list.append(new_item)
        ms_range.append(ms_calculator(base_ms, item_list))
    print([item.get_name() for item in item_list])
    print(ms_range)

ms_growth_tracker(TYR_BASE_MS, HUNTERS_COWL)

