# import ConfigParser
import configparser
from path_dir import *
from CommomUtil.write_log import *

class ReadConf(configparser.ConfigParser):
    def __init__(self,defaults=None):
        configparser.ConfigParser.__init__(self,defaults=None)
    def optionxform(self, optionstr):
        return optionstr

def get_conf(conf_section,pathconf=None):
    if pathconf == None:
        pathconf = config_dir + "configs.conf"
    conf = ReadConf()
    conf.read(pathconf)
    conf_result ={}
    if conf_section in conf.sections():
        for option in conf.options(conf_section):
            conf_result[option] = conf.get(conf_section, option)
        WriteLog.log_info('Read configfile success!')
        return conf_result
    else:
        WriteLog.log_error('"'+conf_section+'"'+" doesn't exist in configs.conf!")



if __name__ == "__main__":
    pathconf=config_dir + "configs.conf"
    a=get_conf("Config")
    b=get_conf("apiConfig")
    print(a)
    print(b)

