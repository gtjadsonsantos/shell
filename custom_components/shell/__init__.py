from homeassistant.core import (
    HomeAssistant,
    ServiceCall
) 
import os

from .const import (
    DOMAIN
)


def setup(hass:HomeAssistant, config):
    def command(call: ServiceCall):
        command = call.data.get("command",None)

        if command:
            os.system(command)

    def commands(call: ServiceCall):
        commands = call.data.get("commands",[str])

        if commands:
            for command in  commands:
                os.system(command)


    hass.services.register(DOMAIN, "command", command)
    hass.services.register(DOMAIN, "commands", commands)
    
    return True
