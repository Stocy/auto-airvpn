#!/usr/bin/python3

import os
import random
import subprocess
from check import load_config, vpn_is_up

if __name__ == '__main__':
    conf = load_config()
    globals().update(conf)

    # Down airvpn if it is up
    exit_code = subprocess.run(["wg","show", wg_interface_name])
    if exit_code.returncode == 0:
        exit_code = subprocess.run(["wg-quick", "down", wg_interface_name])

    # Check internet connection is OK
    exit_code = subprocess.run(["ping", "-c 2", check_internet_website])
    if exit_code.returncode != 0:
        exit(122)

    # select from VPN configs
    wireguard_configs = []
    for file_name in os.listdir(configs_folder):
        if os.path.isfile(os.path.join(configs_folder, file_name)):
            wireguard_configs.append(file_name)
    n_configs = len(wireguard_configs)
    random_config_index = random.randint(0, n_configs-1)
    # print(n_configs)
    # print(random_config_index)

    selected_conf_path = configs_folder+wireguard_configs[random_config_index]
    exit_code = subprocess.run(["cp", selected_conf_path, "/etc/wireguard/"+wg_interface_name+".conf"])
    print(exit_code)
    exit_code = subprocess.run(["wg-quick", "up", wg_interface_name])
    print(exit_code)

    exit_code = subprocess.run(["ping", "-c 2",airvpn_dns_ip])
    print(exit_code)

    if exit_code.returncode == 0:
        exit(0)
    else: exit(123)

# exit_code = subprocess.run(["ping", "-c 2","192.168.4.55"])
# print(exit_code)
# print(exit_code)
# exit_code = subprocess.run(["/bin/false"])
# print(exit_code)
