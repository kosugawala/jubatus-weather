import argparse
import yaml

from jubatus.classifier.client import classifier
from jubatus.classifier.types import *
from jubaweather.version import get_version

def parse_options():
  parser = argparse.ArgumentParser()
  parser.add_argument(
    '-a',
    required = True,
    help     = 'analyze data file (YAML)',
    metavar  = 'FILE',
    dest     = 'analyzedata'
  )
  parser.add_argument(
    '-t',
    help     = 'train data file (CSV)',
    metavar  = 'FILE',
    dest     = 'traindata'
  )
  parser.add_argument(
    '-v',
    '--version',
    action   = 'version',
    version  = '%(prog)s ' + get_version()
  )
  return parser.parse_args()

def main():
  args = parse_options()

  client = classifier('127.0.0.1', 9199)

  # train
  num = 0
  if args.traindata:
    with open(args.traindata, 'rU') as traindata:
      for data in traindata:

        # skip comments
        if not len(data) or data.startswith('#'):
          continue
        num += 1

        season, avetemp, maxtemp, mintemp, pressure, humidity = map(str.strip, data.strip().split(','))
        num_values = [
          ['avetemp', float(avetemp)],
          ['maxtemp', float(maxtemp)],
          ['mintemp', float(mintemp)],
          ['pressure', float(pressure)],
          ['humidity', float(humidity)]
        ]
        d = datum([], num_values)
        train_data = [[season, d]]

        # train
        client.train('', train_data)

    # print train number
    print 'train ...', num
    
    # save train model
    print "save :", client.save('', "weather")

  # anaylze
  with open(args.analyzedata, 'r') as analyzedata:
    weather = yaml.load(analyzedata)
    for k, v in weather.iteritems():
      print str(k), "(", str(v['season']), ")"
      num_values = [
        ['avetemp', float(v['avetemp'])],
        ['maxtemp', float(v['maxtemp'])],
        ['mintemp', float(v['mintemp'])],
        ['pressure', float(v['pressure'])],
        ['humidity', float(v['humidity'])]
      ]
      d = datum([], num_values)
      analyze_data = [d]
      results = client.classify('', analyze_data)
      results[0].sort(key=lambda x: x.score, reverse=True)    
      for result in results:
          for i in range(5):
              print result[i].label, result[i].score
          print
