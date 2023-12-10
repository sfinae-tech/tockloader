"""
Interface for boards using esp-tool
"""

from .board_interface import BoardInterface


class EspTool(BoardInterface):
    def __init__(self, args):
        super(EspTool).__init__(args)

        self.esptool_venv_path = getattr(self.args, "esptool_venv")
        self.esptool_name = getattr(self.args, "esptool_name", "esptool.py")
