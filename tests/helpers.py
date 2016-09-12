import shlex
from subprocess import Popen, PIPE


def run(command):
    print shlex.split(command)
    result = Popen(shlex.split(command), stdout=PIPE, stderr=PIPE)
    result.out = result.stdout.read().rstrip()
    return result


def docker_run(command):
    docker_command = "docker-compose run --rm kibana-ubuntu-base %s" % command
    return run(docker_command)
