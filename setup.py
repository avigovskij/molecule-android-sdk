from setuptools import setup


setup(
    name='molecule_adb',
    version='0.0.1',
    packages=['molecule_adb'],
    package_data={
        'molecule_adb': ('playbooks/**',)
    },
    include_package_data=True,
    install_requires=['molecule'],
    entry_points={
        'molecule.driver': [
            'molecule_adb = molecule_adb.driver:ADBMoleculeDriver'
        ]
    },
    zip_safe=True,
    python_requires='>=3.13',
)
