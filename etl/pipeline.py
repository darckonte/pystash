import importlib
from pprint import pprint


class Pipeline:
    def __init__(self, pipeline_cfg):
        self._extractors = []
        self._processors = []
        self._loaders = []

        for item in pipeline_cfg['extractors']:
            module = importlib.import_module(item['module'])
            extractor = getattr(module, item['type'])(item['cfg_values'])
            self._extractors.append(extractor)



    def execute(self):
        for extractor in self._extractors:
            for data in extractor.on_extract_data():
                pprint(data)
                for processor in self._processors:
                    pdata = processor.on_process_data(data)
                    for loader in self._loaders:
                        loader.on_load_data(pdata)
