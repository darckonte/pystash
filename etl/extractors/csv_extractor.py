from etl.extractors.extractor import Extractor


class CSVExtractor(Extractor):

    def __init__(self, config):
        super().__init__(config)
        self._header = []
        self._filename = config['filename']
        self._separator = config['separator']
        self._chunk_size = config['chunk_size']
        with open(self._filename) as csv:
            self._header = [head.strip() for head in csv.readline().split(self._separator)]

    def on_extract_data(self):
        with open(self._filename) as csv:
            data = []
            csv.readline()
            finished = False
            while not finished:
                lines = csv.readlines(self._chunk_size)
                if lines:
                    for line in lines:
                        linedata = [wrd.strip() for wrd in line.split(self._separator)]
                        data.append(dict(zip(self._header, linedata)))

                    yield data
                finished = not lines

