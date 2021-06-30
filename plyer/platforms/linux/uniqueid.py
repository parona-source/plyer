'''
Module of Linux API for plyer.uniqueid.
'''

from subprocess import run
from plyer.facades import UniqueID
from plyer.utils import whereis_exe


class LinuxUniqueID(UniqueID):
    '''
    Implementation of Linux uniqueid API.
    '''

    def _get_uid(self):
        completeprocess = run(
                ["dbus-uuidgen", "--get"],
                capture_output=True,
                text=True
                )
        if completeprocess.returncode == 0:
            return completeprocess.stdout.strip("\n")
        else:
            sys.stderr.write("`dbus-uuidgen --get` failed")
            return None


def instance():
    '''
    Instance for facade proxy.
    '''
    import sys
    if whereis_exe('dbus-uuidgen'):
        return LinuxUniqueID()
    sys.stderr.write("dbus-uuidgen not found.")
    return UniqueID()
