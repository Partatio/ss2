from typing import ClassVar, Dict
from .options import SS2options
from .items import SS2items, SS2item
from .locations import SS2locations, SS2location
from worlds.AutoWorld import World
from worlds.generic.Rules import add_rule
from BaseClasses import Region, Location, Entrance, Item, ItemClassification
from worlds.LauncherComponents import launch_subprocess, components, Component, Type

from Utils import visualize_regions

def launch_client():
    from .Client import launch
    launch_subprocess(launch, "SS2Client")

components.append(Component("System Shock 2 Client", "SS2Client",
                  func=launch_client, component_type=Type.CLIENT))

class SS2World(World):
    """System Shock 2 item, enemy, skill, stat, and psi randomizer."""
    game = "System Shock 2"  # name of the game/world
    options_dataclass = SS2options  # options the player can set
    options: SS2options
    topology_present = True  # show path to required location checks in spoiler

    item_name_to_id = {name: data["id"] for name, data in SS2items.items()}
    location_name_to_id = {name: data["id"] for name, data in SS2locations.items()}
    item_name_groups = {}

    def add_item_to_group(self, name, group):
        if group in self.item_name_groups:
            self.item_name_groups.group.add(name)
        else:
            self.item_name_groups[group] = {name}

    def create_location(self, locname: str) -> SS2location:
        locdata = SS2locations[locname]
        return SS2location(self.player, locname, locdata["id"], locdata["region"])

    def has_functional_weapon(self, state):
        functional_weapon = (((state.hasgroup("Shotgun", self.player) or (state.hasgroup("Broken Shotgun", self.player) and (state.has("Repair Upgrade", self.player, 3) or state.has("Auto-Repair Unit", self.player)))) 
                                and state.has("Conventional Weapon Upgrade", self.player, 3)) or
                                ((state.hasgroup("Pistol", self.player) or (state.hasgroup("Broken Pistol", self.player) and (state.hasgroup("Repair Upgrade", self.player), 1 or state.hasgroup("Auto-Repair Unit", self.player))))
                                  and state.hasgroup("Conventional Weapon Upgrade", self.player)) or
                                ((state.hasgroup("Assault Rifle", self.player) or (state.hasgroup("Broken Assault Rifle", self.player) and (state.hasgroup("Repair Upgrade", self.player, 4) or state.hasgroup("Auto-Repair Unit", self.player))))
                                  and state.hasgroup("Conventional Weapon Upgrade", self.player)) or
                                ((state.hasgroup("Laser Pistol", self.player) or (state.hasgroup("Broken Laser Pistol", self.player) and (state.has("Repair Upgrade", self.player, 1) or state.has("Auto-Repair Unit", self.player)))) 
                                  and state.has("Energy Weapon Upgrade", self.player, 1)) or
                                (state.hasgroup("Laser Rapier", self.player) and state.has("Energy Weapon Upgrade", self.player, 4) and state.has("Agility Upgrade", self. player, 2)) or
                                ((state.hasgroup("EMP Rifle", self.player) or (state.hasgroup("Broken EMP Rifle", self.player) and (state.has("Repair Upgrade", self.player, 2) or state.has("Auto-Repair Unit", self.player)))) 
                                and state.has("Energy Weapon Upgrade", self.player, 6)) or 
                                ((state.hasgroup("Grenade Launcher", self.player) or (state.hasgroup("Broken Grenade Launcher", self.player) and (state.has("Repair Upgrade", self.player, 2) or state.has("Auto-Repair Unit", self.player)))) 
                                and state.has("Heavy Weapon Upgrade", self.player, 1)) or
                                ((state.hasgroup("Stasis Field Generator", self.player) or (state.hasgroup("Broken Stasis Field Generator", self.player) and (state.has("Repair Upgrade", self.player, 3) or state.has("Auto-Repair Unit", self.player)))) 
                                and state.has("Heavy Weapon Upgrade", self.player, 3) and state.has("Strength Upgrade", self.player, 3)) or
                                ((state.hasgroup("Fusion Cannon", self.player) or (state.hasgroup("Broken Fusion Cannon", self.player) and (state.has("Repair Upgrade", self.player, 4) or state.has("Auto-Repair Unit", self.player)))) 
                                and state.has("Heavy Weapon Upgrade", self.player, 6) and state.has("Strength Upgrade", self.player, 4)) or
                                (state.hasgroup("Crystal Shard", self.player) and state.has("Exotic Weapon Upgrade", self.player, 1) and state.has("Research Upgrade", self. player, 4) and state.has("Yttrium", self.player)) or
                                ((state.hasgroup("Viral Proliferator", self.player) or (state.hasgroup("Broken Viral Proliferator", self.player) and (state.has("Repair Upgrade", self.player, 4) or state.has("Auto-Repair Unit", self.player)))) 
                                and state.has("Exotic Weapon Upgrade", self.player, 4) and state.has("Technetium", self.player) and state.has("Tellurium", self.player)) or
                                ((state.hasgroup("Viral Proliferator", self.player) or (state.hasgroup("Broken Viral Proliferator", self.player) and (state.has("Repair Upgrade", self.player, 5) or state.has("Auto-Repair Unit", self.player)))) 
                                and state.has("Exotic Weapon Upgrade", self.player, 6) and state.has("Strength Upgrade", self.player, 3) and state.has("Agility Upgrade", self.player, 3), state.has("Research Upgrade", self.player, 6) and
                                state.has("Molybdenum", self.player) and state.has("Selenium", self.player)))
        return functional_weapon

    def create_regions(self) -> None:
        curoptions = "" #there is prob a way better way than this
        #if self.options.include_stats_skills_psi:
        #    curoptions += "StatsSkillsPsi,"

        if self.options.include_os_upgrades:
            curoptions += "OSUpgrades,"

        if self.options.include_chems:
            curoptions += "Chems,"

        if self.options.include_decorations:
            curoptions += "Decorations,"

        if self.options.include_starting_wrench:
            curoptions += "StartingWrench,"

        if self.options.many_is_victory:
            curoptions += "ManyIsVictory"



        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)
        #earth_region = Region("earth", self.player, self.multiworld)
        #self.multiworld.regions.append(earth_region)
        #station_region = Region("station", self.player, self.multiworld)
        #self.multiworld.regions.append(station_region)
        medsci1_region = Region("medsci1", self.player, self.multiworld)
        self.multiworld.regions.append(medsci1_region)
        medsci2_region = Region("medsci2", self.player, self.multiworld)
        self.multiworld.regions.append(medsci2_region)
        eng1_region = Region("eng1", self.player, self.multiworld)
        self.multiworld.regions.append(eng1_region)
        eng2_region = Region("eng2", self.player, self.multiworld)
        self.multiworld.regions.append(eng2_region)
        hydro2_region = Region("hydro2", self.player, self.multiworld)
        self.multiworld.regions.append(hydro2_region)
        hydro1_region = Region("hydro1", self.player, self.multiworld)
        self.multiworld.regions.append(hydro1_region)
        hydro3_region = Region("hydro3", self.player, self.multiworld)
        self.multiworld.regions.append(hydro3_region)
        ops1_region = Region("ops1", self.player, self.multiworld)
        self.multiworld.regions.append(ops1_region)
        ops2_region = Region("ops2", self.player, self.multiworld)
        self.multiworld.regions.append(ops2_region)
        ops3_region = Region("ops3", self.player, self.multiworld)
        self.multiworld.regions.append(ops3_region)
        ops4_region = Region("ops4", self.player, self.multiworld)
        self.multiworld.regions.append(ops4_region)
        rec1_region = Region("rec1", self.player, self.multiworld)
        self.multiworld.regions.append(rec1_region)
        rec2_region = Region("rec2", self.player, self.multiworld)
        self.multiworld.regions.append(rec2_region)
        rec3_region = Region("rec3", self.player, self.multiworld)
        self.multiworld.regions.append(rec3_region)
        command1_region = Region("command1", self.player, self.multiworld)
        self.multiworld.regions.append(command1_region)
        command2_region = Region("command2", self.player, self.multiworld)
        self.multiworld.regions.append(command2_region)
        rick1_region = Region("rick1", self.player, self.multiworld)
        self.multiworld.regions.append(rick1_region)
        rick2_region = Region("rick2", self.player, self.multiworld)
        self.multiworld.regions.append(rick2_region)
        rick3_region = Region("rick3", self.player, self.multiworld)
        self.multiworld.regions.append(rick3_region)
        many_region = Region("many", self.player, self.multiworld)
        self.multiworld.regions.append(many_region)
        shodan_region = Region("shodan", self.player, self.multiworld)
        self.multiworld.regions.append(shodan_region)

        for location, data in SS2locations.items():
            if data["option"] not in curoptions:
                continue

            loc = self.create_location(location)
            locregion = self.multiworld.get_region(data["region"], self.player)
            locregion.locations.append(loc)
            for reqitem, amount in data["reqitems"]:
                add_rule(loc, lambda state, ri = reqitem, a = amount: state.has(ri, self.player, a))
                
            for reqgroup in data["reqgroups"]:
                add_rule(loc, lambda state, rg = reqgroup: state.has_group(rg, self.player))


        menu_region.add_exits({"medsci1"})
        medsci1_region.add_exits({"medsci2", "eng1"}, {"medsci2": lambda state: state.has("Dead Power Cell", self.player, 2) and self.has_functional_weapon(state), "eng1": lambda state: state.has("Eng Access Audio Log", self.player) and self.has_functional_weapon(state)}) #dead power cell req is 2 because of the consumable progression items issue.  A better fix would be making powercells that specifically go to the gym or to medsci2.
        eng1_region.add_exits({"eng2", "hydro2"}, {"hydro2": lambda state: state.has("45m/dEx circuit board", self.player) and state.has("Fluidics Control Access Audio Log", self.player)})
        hydro2_region.add_exits({"hydro1", "hydro3", "ops2"}, {"hydro1": lambda state: state.has("Hydroponics Sector A access card", self.player), 
                                                               "hydro3": lambda state: state.has("Hydroponics Sector D access card", self.player),
                                                               "ops2": lambda state: state.has("Toxin-A", self.player, 4) and state.has("Vanadium", self.player) and state.has("Antimony", self.player, 2)
                                                               and state.has_group("Research", self.player) and state.has("Hydroponics Sector A access card", self.player) and state.has("Hydroponics Sector D access card", self.player)})
        ops2_region.add_exits({"rec1", "ops1", "ops3", "ops4"})
        rec1_region.add_exits({"command1", "rec2", "rec3"}, {"command1": lambda state: state.has("Quantum Simulation chip", self.player) and state.has("Linear Simulation chip", self.player) and state.has("Interpolated Simulation chip", self.player)
                                                             and state.has("Deck 5 Crew access card", self.player and state.has("Dead Power Cell", self.player, 2)) and state.has("Athletics access card", self.player)})
        command1_region.add_exits({"command2", "rick1"}, {"rick1": lambda state: state.has("Ops Override access card", self.player)})
        rick1_region.add_exits({"rick2"}, {"rick2": lambda state: state.has("Rickenbacker access Card", self.player)})
        rick2_region.add_exits({"rick3"})
        rick3_region.add_exits({"many"})
        many_region.add_exits({"shodan"})

        VictoryLoc = SS2location(self.player, "Victory", None)
        VictoryLoc.place_locked_item(SS2item("Victory", ItemClassification.progression, None, self.player))
        if self.options.many_is_victory:
            many_region.locations.append(VictoryLoc)
        else:
            shodan_region.locations.append(VictoryLoc)
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

        visualize_regions(self.multiworld.get_region("Menu", self.player), "my_world.puml")

        
            
    def create_item(self, name: str) -> SS2item:
        itemdata = SS2items[name]
        return SS2item(name, itemdata["classification"], itemdata["id"], self.player)

    def create_items(self) -> None:
        SS2itempool = []
        curoptions = ""
        #if self.options.include_stats_skills_psi:
        #    curoptions += "StatsSkillsPsi,"

        if self.options.include_os_upgrades:
            curoptions += "OSUpgrades,"

        if self.options.include_chems:
            curoptions += "Chems,"

        if self.options.include_decorations:
            curoptions += "Decorations,"

        if self.options.include_starting_wrench:
            curoptions += "StartingWrench,"

        if self.options.many_is_victory:
            curoptions += "ManyIsVictory"

        for item, data in SS2items.items():
            if data["option"] not in curoptions:
                continue
            newitem = self.create_item(item)
            if data["group"]:
                self.add_item_to_group(item, data["group"])
            amount = data["count"]
            while amount > 0:
                SS2itempool.append(newitem)
                amount -= 1
        
        self.multiworld.itempool.append(SS2itempool)