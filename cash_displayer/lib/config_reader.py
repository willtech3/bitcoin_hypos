import configparser
import pkg_resources
from cash_displayer.lib.config_types import ConfigTypes

class ConfigReader:

  def __init__(self):
    self.config = configparser.ConfigParser()

  def value(self, config_type, key):
    self.config.read(pkg_resources.resource_filename('cash_displayer.config', config_type))
    # section header in this case is the same as
    # the file name without the extension suffix
    section_header = config_type[:-4]
    return self.config[section_header].get(key)

  def all_config_values(self, config_type):
    self.config.read(pkg_resources.resource_filename('cash_displayer.config', config_type))
    section_header = config_type[:-4]
    configuration_dict = dict()
    for key in self.config[section_header].keys():
      configuration_dict[key] = self.config[section_header].get(key)
    return configuration_dict
