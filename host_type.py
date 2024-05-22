import os
from prometheus_client import Enum


def determine_host_type() -> str:

    if os.environ.get('AM_I_IN_A_CONTAINER') is not None:
        return 'container'
    elif os.environ.get('AM_I_IN_A_VIRTUAL_MACHINE') is not None:
        return 'virtual machine'
    elif os.environ.get('AM_I_IN_A_PHYSICAL_SERVER') is not None:
        return 'physical server'
    else:
        return 'undefined'
