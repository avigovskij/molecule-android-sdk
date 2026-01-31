from ansible.module_utils.basic import AnsibleModule


module_args = dict(
    count=dict(type='int', required=True),
    range_min=dict(type='int', required=False, default=49152),
    range_max=dict(type='int', required=False, default=65535),
    step=dict(type='int', required=False, default=1)
)


def is_port_free(port_number):
    return True


def main(ansible_module):
    ports_found = []

    for _ in range(ansible_module.params["count"]):
        for port_number in range(ansible_module.params["range_min"], ansible_module.params["range_max"] + 1, ansible_module.params["step"]):
            if is_port_free(port_number) and port_number not in ports_found:
                ports_found.append(port_number)
    
    return ports_found

if __name__ == '__main__':
    try:
        ansible_module = AnsibleModule(
            argument_spec=module_args,
            supports_check_mode=True
        )
        ports = main(ansible_module)
        ansible_module.exit_json(
            changed=False,
            free_ports=ports
        )
    except Exception as exception:
        ansible_module.fail_json(
            msg="Cannot find the next opened port! %s" % exception
        )

