from etl.extractors.extractor import Extractor


class CSVExtractor(Extractor):

    def __init__(self, config):
        super().__init__(config)
        self._header = []
        self._filename = config['filename']
        self._separator = config['separator']
        with open(self._filename) as csv:
            self._header = [head.strip() for head in csv.readline().split(self._separator)]

    def on_extract_data(self):
        with open(self._filename) as csv:
            for line in csv:
                linedata = [wrd.strip() for wrd in line.split(self._separator)]
                yield dict(zip(self._header, linedata))
