from ansible.module_utils.basic import AnsibleModule


module_args = dict(
    avd_port=dict(type='int', required=True),
    cmd=dict(type='str', required=True),
)


def main():
    ansible_module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    env = " ".join([
        "export PATH=/data/data/com.termux/files/usr/bin:$PATH;",
        "export LD_PRELOAD=/data/data/com.termux/files/usr/lib/libtermux-exec.so;",
        "export PREFIX=/data/data/com.termux/files/usr;",
        "export TMPDIR=/data/data/com.termux/files/usr/tmp;",
        "export HOME=/data/data/com.termux/files/home; cd $HOME;",
    ])

    cmd = f'adb -s emulator-{ansible_module.params['avd_port']} shell \"run-as com.termux files/usr/bin/bash -lic \'{env} {ansible_module.params['cmd']}\'\"'

    rc, stdout, stderr = ansible_module.run_command(
        cmd,
        expand_user_and_vars=False,
    )

    ansible_module.exit_json(**{
        'rc': rc,
        'stdout': stdout,
        'stderr': stderr,
        'cmd': cmd
    })


if __name__ == '__main__':
    main()
