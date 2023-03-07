##################
3. Getting Started
##################

We will install Docker in WSL (there are some problems with getting the network working between WSL and docker containers)

.. note::

    Ansible is being used to configure virtual machines, we can configure containers (normally we create an image that we will reuse)

.. code-block:: bash

    # Upgrade all WSL packages
    sudo apt update && sudo apt upgrade

    # Install dependencies
    sudo apt -y install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt add -

    # Add new repository
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

    # Pull all the new changes from the new added repository
    sudo apt update
    sudo apt -y install docker-ce docker-ce.cli containerd.io

    # Run docker service
    sudo service docker start

    # Check if docker is running
    sudo service docker start

    # Create a new interactive Ubuntu container named managed_node1 running bash
    docker run --name managed_node1 -it ubuntu bash 

    # Check running containers
    docker ps

    # Find out IPAddress
    docker inspect -f "{{ .NetworkSettings.IPAddress }}" nginx

    # or
    docker exec -it managed_node1 bash
    hostname -I

    # To access via SSH server it needs an SSH server installed
    apt update && apt -y install openssh-server

    # allow to login as root account via SSH.
    echo "PermitRootLogin yes" >> /etc/ssh/sshd_config

    # change the password for the account
    passwd

    # start the SSH service on the container.
    /etc/init.d/ssh start

    # check that the service is running 
    /etc/init.d/ssh status

    # Exchange keys between systems
    ssh-copy-id root@172.17.0.2

.. note::

    There are 2 ways to connect to the: password or key. We prefer to use keys.

=====================================
Setup the configuration and inventory
=====================================

1. create a new file ``ansible.cfg``

.. code-block:: bash

    [defaults]
    inventory = inventory

2. create a new file ``inventory``

.. code-block:: bash

    [nodes]
    172.17.0.2             ansible_connection=ssh        ansible_user=root

===============
Running Ansible
===============

There are 2 ways of running Ansible:

1. Adhoc commands

.. code-block:: bash

    # This command will check if you have a connection to the managed nodes
    ansible nodes -m ping

    # This command will allow you to run a shell session on the managed node
    ansible nodes -m shell -a "hostname"

    # Create a new file in /tmp
    ansible nodes -m shell -a "touch /tmp/example1"

    # Check the newly created file
    ansible nodes -m shell -a "ls -l /tmp/example1"

2. Playbook

-----------------
File manipulation
-----------------
Create a new file ``create_new_file.yml``

.. code-block:: bash 

    - name: Create a new file
    hosts: nodes
    tasks:

        - name: Change file ownership, group, and permissions
          ansible.builtin.file:
            path: /tmp/example2
            owner: root
            group: root
            mode: '0644'
            state: touch

        - name: Remove previous file
          ansible.builtin.file:
            path: /tmp/example
            state: absent

-----------------
User manipulation
-----------------

Create a new file ``create_users_groups.yml``

.. code-block::

    - name: Create a new file
      hosts: nodes
      tasks:

        - name: Create multiple groups
          ansible.builtin.group:
            name: "{{ item }}"
            state: present
          loop:
            - developers
            - operators
            - admins

        - name: Add the user 'user1' with a specific uid 7654 and a primary group of 'developer'
          ansible.builtin.user:
            name: user1
            comment: User One
            uid: 7654
            group: developer

        - name: Add the user 'user2' with a bash shell, appending the group 'admins' and 'developers' to the user's groups
          ansible.builtin.user:
            name: user2
            shell: /bin/bash
            groups: admins,developers
            append: yes

        - name: Remove the user 'user1'
          ansible.builtin.user:
            name: user1
            state: absent
            remove: yes

        - name: Create a 2048-bit SSH key for user user3 in ~/user3/.ssh/id_rsa
          ansible.builtin.user:
            name: user3
            generate_ssh_key: yes
            ssh_key_bits: 2048
            ssh_key_file: .ssh/id_rsa

==================================
Where can we find Ansible modules?
==================================

#. ansible-doc documentation: ``ansible-doc user``
#. `Ansible docs <https://docs.ansible.com/ansible/latest/collections/ansible/builtin/index.html>`_

=======================================
How to debug when stuff is not working?
=======================================

#. Make sure that you're always checking if what you expect is there
#. Use ``debug`` statements
#. Use verbose ``-vvvv``