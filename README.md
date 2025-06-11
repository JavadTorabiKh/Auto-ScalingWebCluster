# Ansible Infrastructure Automation 🚀

Welcome to the Ansible Infrastructure Automation project! This repository provides a robust framework for managing server infrastructure using Ansible, integrated with a GitLab CI/CD pipeline for automated linting, testing, and deployment. Whether you're setting up Docker, installing base packages, or configuring DNS, this project has you covered with a modular and scalable design.

![Ansible Logo](images.jpeg)

## ✨ Features

- Dynamic Inventory: Uses a Python script (env_inventory.py) to generate server lists from environment variables, eliminating static host files.
- Modular Roles: Organized roles for Docker and base package installation, with Molecule tests for validation.
- CI/CD Pipeline: Automated linting, testing, planning, and applying changes via GitLab CI.
- DNS Management: Dedicated playbook for DNS configuration.
- Error Handling: Retries and artifact logging for robust pipeline execution.

## 📋 Prerequisites
To use this project, ensure the following are set up:

1. Python 3 and pip:

- Install Python 3 and pip: 
```bash
    dnf install python3-pip  # For Rocky Linux
    apt install python3-pip  # For Ubuntu
```
2. Docker Engine:

- Install Docker CE following the official instructions: https://docs.docker.com/engine/install/


3. SSH Key Distribution:
- Copy the runner's public SSH key to managed servers:

```bash
    Copy the runner's public SSH key to managed servers:
    cat ~/.ssh/id_rsa.pub | ssh <user>@<server> 'mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys'
```

4. GitLab Environment Variables:

- Define server details in GitLab CI/CD Settings → Variables (e.g., SERVER1_DATA, SERVER2_DATA).
- Format: See ansible/inventory/env_inventory.py for details.



## 🗂️ Repository Structure
```plain
DevOpsAnsible/
├── .gitlab-ci.yml                  # Enhanced CI/CD pipeline
├── README.md                       # Updated documentation
├── CHANGELOG.md                    # Version history
├── LICENSE                         # MIT/Apache license
├── .ansible-lint                   # Linting rules
├── requirements.txt                # Python deps
├── tests/                          # Test directory
│   ├── molecule/                   # Molecule tests
│   └── test-requirements.txt       # Test dependencies
└── ansible/
    ├── ansible.cfg                 # Config
    ├── requirements.yml            # Galaxy roles
    ├── vault.yml                   # Encrypted secrets
    ├── inventory/
    │   ├── production/
    │   │   ├── hosts              # Prod hosts
    │   │   └── group_vars/
    │   │       ├── all.yml        # Common vars
    │   │       ├── docker.yml     # Docker-specific
    │   │       └── gitlab.yml     # GitLab-specific
    │   ├── staging/
    │   │   ├── hosts
    │   │   └── group_vars/
    │   └── env_inventory.py        # Dynamic inventory
    ├── playbooks/
    │   ├── site.yml                # Master playbook
    │   ├── docker.yml              # Docker setup
    │   ├── gitlab.yml              # GitLab setup
    │   ├── monitoring.yml          # Enhanced monitoring
    │   ├── backups.yml             # Backup system
    │   ├── security.yml            # Security hardening
    │   └── maintenance.yml         # Maintenance tasks
    └── roles/
        ├── common/                 # Enhanced common
        │   ├── tasks/
        │   │   ├── main.yml
        │   │   ├── packages.yml
        │   │   ├── security.yml
        │   │   ├── users.yml
        │   │   └── tuning.yml
        │   ├── handlers/
        │   ├── templates/
        │   └── defaults/
        ├── docker/                 # Enhanced Docker
        │   ├── tasks/
        │   │   ├── main.yml
        │   │   ├── install.yml
        │   │   ├── config.yml
        │   │   ├── compose.yml     # Docker Compose
        │   │   └── networks.yml    # Network config
        │   ├── templates/
        │   │   ├── daemon.json.j2
        │   │   └── docker-compose.yml.j2
        │   ├── defaults/
        │   └── vars/
        ├── gitlab/                 # Enhanced GitLab
        │   ├── tasks/
        │   │   ├── main.yml
        │   │   ├── install.yml
        │   │   ├── config.yml
        │   │   ├── runners.yml     # CI runners
        │   │   └── backup.yml      # GitLab backup
        │   ├── templates/
        │   │   ├── gitlab.rb.j2
        │   │   └── backup.sh.j2
        │   ├── defaults/
        │   └── vars/
        ├── monitoring/             # Enhanced monitoring
        │   ├── tasks/
        │   │   ├── main.yml
        │   │   ├── node_exporter.yml
        │   │   ├── cadvisor.yml    # Container monitoring
        │   │   └── alerts.yml      # Alert rules
        │   ├── templates/
        │   └── defaults/
        ├── backups/                # Enhanced backups
        │   ├── tasks/
        │   │   ├── main.yml
        │   │   ├── setup.yml
        │   │   ├── gitlab.yml
        │   │   └── docker.yml
        │   ├── templates/
        │   └── defaults/
        └── security/              # New security role
            ├── tasks/
            │   ├── main.yml
            │   ├── firewall.yml
            │   ├── ssh_hardening.yml
            │   └── audits.yml
            ├── templates/
            └── defaults/
```

## 🚀 Getting Started

1. Clone the Repository:
```bash
    git clone https://github.com/JavadTorabiKh/DevOpsAnsible.git
    cd DevOpsAnsible
```

2. Set Up GitLab CI:

- Configure environment variables in GitLab CI/CD Settings → Variables.
- Ensure your runner has access to the target servers via SSH.


3. Run Locally (Optional):

- Install dependencies:
```bash
    pip3 install --user ansible ansible-lint yamllint molecule molecule-docker docker
    ansible-galaxy install -r ansible/requirements.yml
```

4. Run the main playbook:
```bash
    ansible-playbook ansible/playbooks/main.yml -i ansible/inventory/env_inventory.py
```

## 🛠️ CI/CD Pipeline
The GitLab CI pipeline automates the following stages:

| Stage | Description |
|---------|---------|
| lint    | Runs yamllint and ansible-lint to ensure code quality.   |
| test    | Executes Molecule tests for roles in parallel (e.g., docker, packages_base).   |
| check_config    |  Simulates and applies DNS configuration changes.   |
| plan    | Simulates changes for the main playbook (--check --diff).   |
| apply    | Applies changes manually to target servers.   |


## Artifacts

- Logs are stored as artifacts for 1 week to debug failures.
- Use the GitLab UI to trigger the apply stage manually.

## 🧪 Testing with Molecule
Each role (docker, packages_base) includes Molecule tests:

- Navigate to ansible/roles/<role>/molecule/default/.

- Run tests:
```bash
    cd ansible/roles/docker
    molecule test
```

## 🛠️ Customization

- Add New Roles: Create a new directory under ansible/roles/ with tasks/main.yml and defaults/main.yml.
- Extend Inventory: Update env_inventory.py to support additional server attributes.
- Modify Pipeline: Adjust .gitlab-ci.yml to add new stages or jobs.

## 📝 Notes

- Ensure environment variables are securely stored in GitLab.
- Review ansible.cfg for custom Ansible settings (e.g., timeouts, SSH options).
- For large deployments, consider using a custom Docker image with pre-installed dependencies to reduce pipeline runtime.

## 🤝 Contributing
Contributions are welcome! Please:

1. Fork the repository.
2. Create a feature branch (git checkout -b feature/awesome-feature).
3. Commit changes (git commit -m 'Add awesome feature').
4. Push to the branch (git push origin feature/awesome-feature).
5. Open a pull request.

## 📧 Contact
For questions or support, reach out via [GitLab Issues](/issues) or email [javadtorabi462@gmail.com].

---

Powered by Ansible and GitLab CI/CD

