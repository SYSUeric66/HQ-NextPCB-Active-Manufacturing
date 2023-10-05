

try:
    from .kicad_amf_plugin.plugin.kicad_amf_action_plugin import KiCadAmfActionPlugin
    KiCadAmfActionPlugin().register()
except Exception as e:
    import logging
    logger = logging.getLogger()
    logger.debug(repr(e))
