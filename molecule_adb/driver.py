import os
import yaml

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

    def load_instances_data(self):
        data = []
        try:
            with open(self.instance_config, 'r') as instance_data:
                data = yaml.safe_load(instance_data)
        except FileNotFoundError:
            pass

        return data

    @property
    def login_cmd_template(self) -> str:  # pragma: no cover
        return """ssh -i {private_ssh_key_file} {ansible_user}@{ansible_host} -p {ansible_port} -o StrictHostKeyChecking=no"""

    @property
    def default_ssh_connection_options(self) -> list[str]:  # pragma: no cover
        """SSH client options and returns a list.

        :returns: list
        """
        return [
            "StrictHostKeyChecking=no"
        ]

    def ansible_connection_options(
        self,
        instance_name: str,
    ):
        instances = self.load_instances_data()
        instance_data = {}
        for instance in instances:
            if instance['verbose_name'] == instance_name:
                instance_data = instance
                break

        return instance_data

    def login_options(self, instance_name):
        instances = self.load_instances_data()
        instance_data = {}
        for instance in instances:
            if instance['verbose_name'] == instance_name:
                instance_data = instance
                break
        else:
            raise Exception(f'Config for instance named "{instance_name}" not found!')

        return instance_data

    def sanity_checks(self):
        # TODO: Add implement of android SDK availablility
        bin_requirements = ["emulator", "adb", "avdmanager"]

        for bin_requirement in bin_requirements:
            rc = os.system(f"which {bin_requirement}")
            if rc != 0:
                raise Exception(
                    f"Cannot continue! {bin_requirement} should be exported to PATH for correct {self.name} work!"
                )
