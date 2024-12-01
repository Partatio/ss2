import websockets
import asyncio
import Utils
import sys
import tkinter as tk
import tkinter.filedialog
import os
import threading
import asyncio
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from CommonClient import ClientCommandProcessor, CommonContext, gui_enabled, logger, server_loop, get_base_parser

class SS2CommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: CommonContext):
        super().__init__(ctx)

class SS2Context(CommonContext):
    command_processor = SS2CommandProcessor
    game = "System Shock 2"
    items_handling = 0b111  # full remote

    def __init__(self, server_address, password):
        super(SS2Context, self).__init__(server_address, password)
        self.send_index: int = 0
        self.syncing = False
        self.awaiting_bridge = False

    async def disconnect(self, allow_autoreconnect: bool = False):
        self.auth = None
        await super().disconnect(allow_autoreconnect)

    async def server_auth(self, password_requested: bool = False):
        # This is called to autentificate with the server.
        if password_requested and not self.password:
            await super(SS2Context, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    async def connection_closed(self):
        # This is called when the connection is closed (duh!)
        await super(SS2Context, self).connection_closed()

    # Do not touch this
    @property
    def endpoints(self):
        if self.server:
            return [self.server]
        else:
            return []

    async def shutdown(self):
        # What is called when the app gets shutdown
        await super(SS2Context, self).shutdown()

    def on_package(self, cmd: str, args: dict):
        # This is what is done when a package arrives.
        #if cmd in {"Bounced"}:
        #if cmd in {"LocationInfo"}:
        #if cmd in {"ReceivedItems"}:
        #if cmd in {"RoomUpdate"}:
        #if cmd in {"RoomInfo"}:
        #if cmd in {"Connected"}:
        return
    
    def run_gui(self):
        from kvui import GameManager

        class SS2Manager(GameManager):
            # logging_pairs for any separate logging tabs
            base_title = "Archipelago System Shock 2 Client"

        self.ui = SS2Manager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")

def print_error_and_close(msg):
    logger.error("Error: " + msg)
    Utils.messagebox("Error", msg, error=True)
    sys.exit(1)

def launch():
    async def main(args):
        ctx = SS2Context(args.connect, args.password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        await ctx.exit_event.wait()
        ctx.server_address = None

        await ctx.shutdown()

    SS2DirPath = tk.filedialog.askdirectory(title="Select System Shock 2 installation folder", 
                                            filetypes=[("SS2", "SS2")])
    print(SS2DirPath)

    parser = get_base_parser()
    args = parser.parse_args()

    import colorama

    colorama.init()
    asyncio.run(main(args))
    colorama.deinit()