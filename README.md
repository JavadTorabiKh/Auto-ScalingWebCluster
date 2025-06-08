# Ansible Infrastructure Automation 🚀

Welcome to the Ansible Infrastructure Automation project! This repository provides a robust framework for managing server infrastructure using Ansible, integrated with a GitLab CI/CD pipeline for automated linting, testing, and deployment. Whether you're setting up Docker, installing base packages, or configuring DNS, this project has you covered with a modular and scalable design.

![Ansible Logo](https://www.ansible.com/hubfs/2016_Images/AnsibleMark_RGB_RedWhite.png)
## ✨ Features

- Dynamic Inventory: Uses a Python script (env_inventory.py) to generate server lists from environment variables, eliminating static host files.
- Modular Roles: Organized roles for Docker and base package installation, with Molecule tests for validation.
- CI/CD Pipeline: Automated linting, testing, planning, and applying changes via GitLab CI.
- DNS Management: Dedicated playbook for DNS configuration.
- Error Handling: Retries and artifact logging for robust pipeline execution.

## 📋 Prerequisites
To use this project, ensure the following are set up:

Python 3 and pip:

Install Python 3 and pip: dnf install python3-pip (Rocky) or apt install python3-pip (Ubuntu).


Docker Engine:

Install Docker CE following the official instructions.


SSH Key Distribution:

Copy the runner's public SSH key to managed servers:
cat ~/.ssh/id_rsa.pub | ssh <user>@<server> 'mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys'




GitLab Environment Variables:

Define server details in GitLab CI/CD Settings → Variables (e.g., SERVER1_DATA, SERVER2_DATA).
Format: See ansible/inventory/env_inventory.py for details.



🗂️ Repository Structure
.
├── .gitlab-ci.yml                  # GitLab CI pipeline definition
├── README.md                      # You're reading it!
└── ansible
    ├── ansible.cfg                 # Ansible configuration
    ├── requirements.yml            # Ansible Galaxy dependencies
    ├── inventory
    │   └── env_inventory.py       # Dynamic inventory script
    ├── playbooks
    │   ├── main.yml               # Main playbook
    │   └── dns.yml                # DNS configuration playbook
    ├── roles
    │   ├── docker                 # Role for Docker setup
    │   └── packages_base          # Role for base package installation

🚀 Getting Started

Clone the Repository:
git clone <repository-url>
cd <repository-name>


Set Up GitLab CI:

Configure environment variables in GitLab CI/CD Settings → Variables.
Ensure your runner has access to the target servers via SSH.


Run Locally (Optional):

Install dependencies:
pip3 install --user ansible ansible-lint yamllint molecule molecule-docker docker
ansible-galaxy install -r ansible/requirements.yml


Run the main playbook:
ansible-playbook ansible/playbooks/main.yml -i ansible/inventory/env_inventory.py





🛠️ CI/CD Pipeline
The GitLab CI pipeline automates the following stages:



Stage
Description



lint
Runs yamllint and ansible-lint to ensure code quality.


test
Executes Molecule tests for roles in parallel (e.g., docker, packages_base).


check_config
Simulates and applies DNS configuration changes.


plan
Simulates changes for the main playbook (--check --diff).


apply
Applies changes manually to target servers.


Artifacts

Logs are stored as artifacts for 1 week to debug failures.
Use the GitLab UI to trigger the apply stage manually.

🧪 Testing with Molecule
Each role (docker, packages_base) includes Molecule tests:

Navigate to ansible/roles/<role>/molecule/default/.

Run tests:
cd ansible/roles/docker
molecule test



🛠️ Customization

Add New Roles: Create a new directory under ansible/roles/ with tasks/main.yml and defaults/main.yml.
Extend Inventory: Update env_inventory.py to support additional server attributes.
Modify Pipeline: Adjust .gitlab-ci.yml to add new stages or jobs.

📝 Notes

Ensure environment variables are securely stored in GitLab.
Review ansible.cfg for custom Ansible settings (e.g., timeouts, SSH options).
For large deployments, consider using a custom Docker image with pre-installed dependencies to reduce pipeline runtime.

🤝 Contributing
Contributions are welcome! Please:

Fork the repository.
Create a feature branch (git checkout -b feature/awesome-feature).
Commit changes (git commit -m 'Add awesome feature').
Push to the branch (git push origin feature/awesome-feature).
Open a pull request.

📧 Contact
For questions or support, reach out via [GitLab Issues](/issues) or email [your-email@example.com].

Built with ❤️ by [Your Name/Team]\

Powered by Ansible and GitLab CI/CD

