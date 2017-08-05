#!/usr/bin/env python

testinfra_hosts = [
    "docker://mrsum",
    "docker://mpsql",
]


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_http_connection(host):
    h = host.get_host('docker://mrsum')
    s = h.socket('tcp://0.0.0.0:8193')

    assert s.is_listening

def test_pgsql_connection(host):
    h = host.get_host('docker://mpsql')
    s = h.socket('tcp://0.0.0.0:5433')

    assert s.is_listening
