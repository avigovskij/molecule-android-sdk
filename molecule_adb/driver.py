import os

from molecule.api import Driver


class ADBMoleculeDriver(Driver):
    def __init__(self, config=None):
        super(ADBMoleculeDriver, self).__init__(config)
        self._name = "molecule_adb"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def ansible_connection_options(self, instance_name):
        return super().ansible_connection_options(instance_name)

    @property
    def default_safe_files(self):
        return [self.instance_config]

    def default_ssh_connection_options(self):
        return self._get_ssh_connection_options()

    def login_cmd_template():
        pass

    def login_options(self, instance_name):
        return super().login_options(instance_name)

    def sanity_checks(self):
        # TODO: Add implement of android SDK availablility
        bin_requirements = ["emulator", "adb", "avdmanager"]

        for bin_requirement in bin_requirements:
            rc = os.system(f"which {bin_requirement}")
            if rc != 0:
                raise Exception(
                    f"Cannot continue! {bin_requirement} should be exported to PATH for correct {self.name} work!"
                )
