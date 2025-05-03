# Ansible Playbooks

## 📌 Overview
This repository contains Ansible playbooks for automating infrastructure management and deployments.

## 🚀 Quick Start
1. Install requirements:
```bash
   ansible-galaxy install -r requirements.yml
```

2. Run a playbook:

```bash
    ansible-playbook -i inventory/prod playbooks/deploy.yml
```

--- 

## 📂 Structure

```bash
    ansible-playbooks/
    ├── inventory/      # Environment inventories
    ├── group_vars/     # Variable files
    ├── roles/          # Custom roles
    └── playbooks/      # Main playbooks
```

---

## 🔧 Usage

- Dry run: --check

- Limit hosts: -l webservers

- Vault: ansible-vault edit secrets.yml

---

## 📜 License

### **MIT License**

- [Official Docs](https://docs.ansible.com)