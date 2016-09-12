from helpers import docker_run


def test_kibana_user_is_uid_1000():
    assert docker_run('id --user kibana').out == '1000'


def test_operating_system_is_ubuntu_16_04():
    assert docker_run('cat /etc/issue').out.startswith('Ubuntu 16.04')
