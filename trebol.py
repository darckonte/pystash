import json
import argparse
from pprint import pprint


from etl.pipeline import Pipeline

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pipeline')

    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()

    pipeline_cfg = json.load(open(args.pipeline))
    for ppln in pipeline_cfg:
        print("Executing {}".format(ppln))
        pipeline = Pipeline(ppln['pipeline'])
        pipeline.execute()
