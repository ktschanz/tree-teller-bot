import yaml
import os.path

config = {}

basepath = os.path.abspath(os.path.dirname(__file__))

with open(basepath + '/config.yaml', 'r') as ymlfile:
    config = yaml.load(ymlfile, Loader=yaml.FullLoader)

config['trees_path'] = basepath + '/trees.csv'

