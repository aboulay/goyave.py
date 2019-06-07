from parser.exceptions import InvalidConfigurationFileException


class data_checker():
    @staticmethod
    def check_content_is_valid(content):
        if not content.get('targets'):
            raise InvalidConfigurationFileException()
        for target in content['targets']:
            if not target.get('name'):
                raise InvalidConfigurationFileException()
            if not target.get('url'):
                raise InvalidConfigurationFileException()
            if not target.get('format'):
                raise InvalidConfigurationFileException()
            if (not target.get('wanted_field') or
                    target['wanted_field'] is None):
                raise InvalidConfigurationFileException()
            if not target.get('main_output'):
                raise InvalidConfigurationFileException()
