from dotenv import load_dotenv
import os

class InternalConfigs:
    """
    """

    mappings = {
        'api': 'API',
        'achievement': 'ACH',
        'discord': 'DSC',
        'global': 'RUN',
        'custom': 'CST'
    }

    def __init__(self):
        load_dotenv()
        self.__vars = {}

        for var, value in os.environ.items():
            if var.startswith('IWK__'):
                _var = var.replace('IWK__', '').upper()
                self.__vars[_var] = value

    
    def get_attr(self, category, key):
        prefix = self.mappings[category]
        full_key = prefix + '__' + key
        full_key = full_key.upper()
        
        try:
            if category == 'custom':
                return int(self.__vars[full_key])
            return self.__vars[full_key]
        except KeyError:
            return None
            


