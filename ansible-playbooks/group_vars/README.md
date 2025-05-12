## Ansible Group Variables (group_vars) Documentation

### Purpose

This directory contains variable definitions that apply to specific host groups defined in your Ansible inventory. These variables help customize configurations for different server roles or environments.

Directory Structure

    group_vars/
    ├── all/                   # Variables for ALL hosts
    │   ├── common.yml         # Common variables
    │   └── vault.yml          # Encrypted variables (optional)
    ├── webservers.yml         # Web server specific variables
    ├── dbservers.yml          # Database server variables
    ├── production/            # Production environment vars
    ├── staging/               # Staging environment vars
    └── dev/                   # Development environment vars


### Best Practices

1. Organization

Keep variables scoped to their relevant groups

Use separate files for logical groupings (e.g., network.yml, security.yml)

Maintain environment-specific vars in separate subdirectories

2. Security
```bash
    # Encrypt sensitive data
    ansible-vault encrypt group_vars/production/secrets.yml
```

3. Variable Design

Use descriptive variable names

Document variables with comments

Set sane defaults in all/ directory

Override as needed in group-specific files