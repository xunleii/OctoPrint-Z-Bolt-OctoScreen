import json

zbolt_toolchanger_installed = True


default_menu_structure = """[
    {
        "name": "Home",
        "icon": "home",
        "panel": "home"
    },
    {
        "name": "Actions",
        "icon": "actions",
        "panel": "menu",
        "items": [
            {
                "name": "Move",
                "icon": "move",
                "panel": "move"
            },
            {
                "name": "Extrude",
                "icon": "filament",
                "panel": "extrude_multitool"
            },
            {
                "name": "Fan",
                "icon": "fan",
                "panel": "fan"
            },
            {
                "name": "Temperature",
                "icon": "heat-up",
                "panel": "temperature"
            },
            {
                "name": "Control",
                "icon": "control",
                "panel": "control"
            },
            {
                "name": "ToolChanger",
                "icon": "toolchanger",
                "panel": "toolchanger"
            }
        ]
    },
    {
        "name": "Filament",
        "icon": "filament",
        "panel": "filament_multitool"
    },
    {
        "name": "Configuration",
        "icon": "control",
        "panel": "menu",
        "items": [
            {
                "name": "Bed Level",
                "icon": "bed-level",
                "panel": "bed-level"
            },
            {
                "name": "ZOffsets",
                "icon": "z-offset-increase",
                "panel": "nozzle-calibration"
            },
            {
                "name": "Network",
                "icon": "network",
                "panel": "network"
            },
            {
                "name": "System",
                "icon": "info",
                "panel": "system"
            }
        ]
    }
]"""


class ZBoltOctoScreenSettings(object):
    def __init__(self, settings):
        self._settings = settings
        self.default_menu_structure = default_menu_structure

    def get_all(self):
        return {
            "filament_in_length": float(self._settings.get(["filament_in_length"])),
            "filament_out_length": float(self._settings.get(["filament_out_length"])),
            "gcodes": self._settings.get(["gcodes"]),
            "toolchanger": bool(self._settings.get(["toolchanger"])),
            "z_axis_inverted": bool(self._settings.get(["z_axis_inverted"])),
            "menu_structure": json.loads(self._settings.get(["menu_structure"])),
        }

    @staticmethod
    def default_settings():
        return dict(
            filament_in_length=750,
            filament_out_length=800,
            toolchanger=False,
            z_axis_inverted=True,
            gcodes=dict(auto_bed_level="G29"),
            menu_structure=default_menu_structure,
        )

    @staticmethod
    def template_vars():
        return dict(default_menu_structure=default_menu_structure)

