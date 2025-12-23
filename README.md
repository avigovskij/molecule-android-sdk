# molecule-android-sdk
Molecule driver for managing android devices as targets via android sdk.

### Features

Provides a molecule driver that can be used to:

* Describe configuration of android devices as a code.
* Deploy android devices according to provided yaml-based configuration.
* Specify your own playbooks for following actions with created resources.
* Get access to created resources via Andorid OpenSSH implementation and [Termux shell](https://github.com/termux/termux-app)

### Requirements

* Python environment with package [molecule](https://docs.ansible.com/projects/molecule/);
* Android SDK installed on "hypervisor" machine (no Android Studio needed, you can use [sdkmanager](https://developer.android.com/tools/sdkmanager?hl=ru));


### Notes about developing and release project
Current project doesn't have team of developers. That's why there's no need to split developing process between branches and develop release cycle.

`develop` – branch with code that worked on developer's machine,
`releease` – branch with code that worsk on production-ready dedicated server.

In future it's obligatory to implement release process that will allow code to go through QA.
