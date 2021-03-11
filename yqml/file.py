import yaml

class File:
    def __init__(self, url):
        self._url = url
    
    @property
    def yaml_dict(self):
        with open(self._url, 'r') as stream:
            try:
                config_dict = yaml.safe_load(stream)
                return config_dict
            except yaml.YAMLError as exc:
                print(exc)
        return None

    @property
    def content(self):
        with open(self._url, 'r') as myfile:
            try:
                return myfile.read()
            except Exception as e:
                print(str(e))
                return None
