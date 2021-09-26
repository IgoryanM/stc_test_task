import argparse
import random
import ipaddress
from subprocess import Popen, PIPE

"""Linux-приложение, которое принимает на вход адрес подсети (например, ping.py 192.168.0.0/24), затем запускает 
команду ping (классический ping) для одного из адресов сети (например, 192.168.0.1), анализирует вывод, 
если адрес ответил на ping, вносит его в файл ping_ok, если не ответил в файл no_ping. """


def subnet_ip_parser():
    try:
        parser = argparse.ArgumentParser(description='subnet_IP_address')
        parser.add_argument('--addr', type=str, default='192.168.0.0/24', help='subnet_IP_address')

        subnet_ip_address = parser.parse_args().addr
        return subnet_ip_address

    except Exception as e:
        print(e)


def random_ip_from_subnet(subnet_ip_address):
    try:
        subnet = ipaddress.ip_network(subnet_ip_address)
        random_ip_addr = random.choice(list(subnet.hosts()))
        return random_ip_addr

    except Exception as e:
        print(e)


def host_ping(random_ip_addr, timeout=500, requests=1):
    if random_ip_addr:
        try:
            proc = Popen(f'ping {random_ip_addr} -w {timeout} -n {requests}', stdout=PIPE)
            proc.wait()

            if proc.returncode == 0:
                with open('ping_ok.txt', 'a') as f:
                    f.write(str(random_ip_addr) + '\n')

            else:
                with open('no_ping.txt', 'a') as f:
                    f.write(str(random_ip_addr) + '\n')

        except Exception as e:
            print(e)


if __name__ == '__main__':
    arg = subnet_ip_parser()
    random_ip = random_ip_from_subnet(arg)
    host_ping(random_ip)
