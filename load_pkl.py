import pickle
import argparse

def load_pickle(pickle_file):
  try:
    with open(pickle_file, 'rb') as f:
      pickle_data = pickle.load(f)
  except UnicodeDecodeError as e:
    with open(pickle_file, 'rb') as f:
      pickle_data = pickle.load(f, encoding='latin1')
  except Exception as e:
    raise
  return pickle_data


def main():
  parser = argparse.ArgumentParser(description='Load a pkl file')
  parser.add_argument('-f', '--filename', type=str, metavar='', required=True, help='Enter filename')
  args = parser.parse_args()
  pkl = load_pickle(args.filename)
  print(pkl)

if __name__ == '__main__':
  main()

