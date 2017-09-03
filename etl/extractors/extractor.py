class Extractor:

    def __init__(self, config):
        self._config = config

    def on_extract_data(self):
        raise NotImplementedError