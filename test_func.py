"""
    Tests for functions.
"""
import ipaddress

from ping_check import subnet_ip_parser, random_ip_from_subnet


def test_subnet_ip_parser():
    subnet_ip_address = subnet_ip_parser()
    assert subnet_ip_address == '192.168.0.0/24'


def test_random_ip_from_subnet():
    random_ip_addr = random_ip_from_subnet('192.168.0.0/24')
    subnet = ipaddress.ip_network('192.168.0.0/24')
    assert random_ip_addr in subnet
