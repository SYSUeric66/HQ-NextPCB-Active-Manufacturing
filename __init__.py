from .kicad_amf_plugin.plugin import Plugin

try:
    Plugin().register()
except Exception as e:
    import logging
    logger = logging.getLogger()
    logger.debug(repr(e))
