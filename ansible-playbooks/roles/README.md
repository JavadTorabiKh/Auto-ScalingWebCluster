# Ansible Roles Directory

## 📂 Directory Structure

```bash
    roles/
    ├── gitlab/ # Base system configurations
    ├── services/ # Web server setups (Nginx/Apache)
    └── postgresql/ # DB servers (PostgreSQL/MySQL)
```

---

## 🛠️ Usage

1. Create a new role:
```bash
   ansible-galaxy init roles/new_role_name
```

2. install community roles:

```bash
    ansible-galaxy install -p roles/ author.role_name
```

3. Reference in playbooks:

```yaml
    roles:
    - role: webserver
        vars:
        nginx_version: 1.25.0
```
---

## 🔧 Best Practices

- Keep roles atomic (single purpose)

- Use defaults/ for variables

- Document in meta/main.yml

- Test with Molecule

---

## 📜 Example Role Structure

```text
    role_name/
    ├── defaults/      # Lowest priority vars
    ├── files/         # Static files
    ├── handlers/      # Service handlers
    ├── meta/          # Dependencies
    ├── tasks/         # Main playbook
    ├── templates/     # Jinja2 templates
    └── vars/          # High priority vars
```


![Ansible Version](https://img.shields.io/badge/Ansible-roles-red?logo=ansible)