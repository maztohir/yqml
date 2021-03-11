import argparse
import sys

class Args:

  @staticmethod
  def parse():
    try:
        parser        = argparse.ArgumentParser()
        parser.add_argument('--input', dest='input', required=True)
    
        args = parser.parse_args()
        return args

    except KeyboardInterrupt:
        sys.exit(0)
