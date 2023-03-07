###############
1. Installation
###############

All major platforms' installation instructions are available in the official Ansible documentation.
Please check https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html.

There are 2 types of installation:

#. Linux package

.. code-block:: bash
    
    sudo apt-get update
    sudo apt-get install software-properties-common
    sudo apt-add-repository --yes --update ppa:ansible/ansible
    sudo apt-get install ansible

#. Python package

.. code-block:: bash

    # Create and activate new virtual environment
    python3.11 -m venv venv
    . venv/bin/activate

    # Install Ansible
    pip install ansible
    
    # Check the installed version
    ansible --version

.. note::

    I recommend using the pip for development and testing upcoming features, but relying on the Linux package for production.

========================
Graphical User Interface
========================

Ansible is a ``cli`` application, but we can add a GUI interface for easy management - `AWX <https://github.com/ansible/awx>`_

Starting in version 18.0, the `AWX Operator <https://github.com/ansible/awx-operator>`_ is the preferred way to install AWX. Ansible operator is a Kubernetes operator, which means running it in a pod.

AWX can also alternatively be installed and run in `Docker <https://github.com/ansible/awx/blob/devel/tools/docker-compose/README.md>`_, but this install path is only recommended for development/test-oriented deployments and has no official published release.