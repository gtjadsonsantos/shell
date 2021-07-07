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

        os.system(command)

    hass.services.register(DOMAIN, "command", command)
    return True
