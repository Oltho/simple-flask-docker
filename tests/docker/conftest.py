import os
import subprocess
import uuid

import pytest
import testinfra


# scope='session' uses the same container for all the tests;
# scope='function' uses a new container per test function.
@pytest.fixture(scope='session')
def host(request):
    IMAGE_NAME: str = os.getenv("TESTINFRA_DOCKER_IMAGE_NAME", "")
    SHOULD_BUILD: bool = (IMAGE_NAME == "")
    # build local ./Dockerfile
    if SHOULD_BUILD:
        IMAGE_NAME = f"simple_flask:testinfra-{str(uuid.uuid4())}"
        subprocess.check_call(['docker', 'build', '-t', IMAGE_NAME, '.'])
    # run a container
    docker_id = subprocess.check_output(
        ['docker', 'run', '-d', IMAGE_NAME]).decode().strip()
    # return a testinfra connection to the container
    yield testinfra.get_host("docker://" + docker_id)
    # at the end of the test suite, destroy the container
    subprocess.check_call(['docker', 'rm', '-f', docker_id])

    if SHOULD_BUILD:
        subprocess.check_call(['docker', 'image', 'rm', "-f", IMAGE_NAME])
