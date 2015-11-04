import os

def write_config(config, section, config_dict=None,**kwargs):
    config.add_section(section)
    if config_dict:
        for key in config_dict:
            config.set(section, key, config_dict[key])

    for key in kwargs:
        config.set(section, key, kwargs[key])
    print '========================================'

def django_manage(args):
    cmd = 'python ./manage.py ' + args
    os.system(cmd)
