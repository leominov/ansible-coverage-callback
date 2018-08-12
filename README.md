# ansible-coverage-callback

Coverage Tool for Ansible.

## Requirements

* Ansible >=2.4

## Installation

* Copy `coverage.py` to your playbook callback directory (by default `callback_plugins/` in your playbook's root directory). Create the directory if it doesn't exist;
* Be sure to whitelist the plugin in your `ansible.cfg`:

```
[defaults]
callback_whitelist = coverage
```

## Skip coverage tag

You may skip task or tasks from coverage report by adding `skip_coverage` tag:

```
---
- name: Test handler
  command: whoami
  when:
    - test_var == False
  tags:
    - skip_coverage
```