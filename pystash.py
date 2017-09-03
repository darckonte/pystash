from etl.pipeline import Pipeline

class PyStash:

    def __init__(self, pipeline):
        self._pipeline = pipeline

    def run(self):
        data = self._pipeline.extract()
        data = self._pipeline.process(data)
        self._pieline.load(data)


if __name__ == "__main__":
    pipeline = Pipeline("")
    pystash = PyStash()
    pystash.run()