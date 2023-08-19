#!/usr/bin/python3
import os
import subprocess
import yaml

def load_config():
    global dir
    dir = os.path.dirname(__file__)
    with open(dir+'/config.yaml', 'r') as file:
        script_config_values = yaml.safe_load_all(file)
        # print(type(script_config_values),script_config_values)
        config_dict = next(script_config_values)
        # print(type(config_dict),config_dict)
        return config_dict
        
        # print("here")

def vpn_is_up():
   exit_code = subprocess.run(["ping", "-c 2",airvpn_dns_ip])
   return bool(exit_code.returncode)
    # print("check , dns exit code ",exit_code.returncode )

def check_and_start_if_needed():
    if vpn_is_up():
        exit(0)
    else:
        exit_code = subprocess.run([dir+'/start.py'])
        
    exit(exit_code.returncode)

if __name__ == '__main__':
    conf = load_config()
    globals().update(conf)
    check_and_start_if_needed()

# directory/folder path
# print('getcwd:      ', os.getcwd())
# print('__file__:    ', __file__)
# print('dirname:     ', os.path.dirname(__file__))

#load script config from config.yaml 


# print(globals())
# print(configs_folder)




