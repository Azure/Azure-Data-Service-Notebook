from adlmagics.magics.magic_with_result_base import MagicWithResultBase

class AdlaMagicBase(MagicWithResultBase):
    def __init__(self, cmd_name, session_service, presenter_factory, result_converter, adla_service):
        super(AdlaMagicBase, self).__init__(cmd_name, session_service, presenter_factory, result_converter)

        self._adla_service = adla_service