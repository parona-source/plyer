'''
Module of Linux API for plyer.uniqueid.
'''

from os.path import isfile
from plyer.facades import UniqueID


class LinuxUniqueID(UniqueID):
    '''
    Implementation of Linux uniqueid API.
    '''

    def _get_uid(self):
        with open("/etc/machine-id", "r") as machine_id_file:
            result = machine_id_file.read().strip("\n")
        return result


def instance():
    '''
    Instance for facade proxy.
    '''
    import sys
    if isfile("/etc/machine-id"):
        return LinuxUniqueID()
    sys.stderr.write("/etc/machine-id not found.")
    return UniqueID()
