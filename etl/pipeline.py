class Pipeline:
    def __init__(self, pipeline_cfg):
        self._extractors = []
        self._processors = []
        self._loaders = []

    def extract(self):
        data = []
        for extractor in self._extractors:
            data.append(extractor.on_extract_data())

        for processor in self._processors:
            processor.on_process_data(data)

        for loader in self._loaders:
            loader.on_load_data(data)