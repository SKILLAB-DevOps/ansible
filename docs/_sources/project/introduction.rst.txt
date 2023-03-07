###############
0. Introduction
###############

======
Task 1
======

#. Create a new project in your GitHub userspace with documentation for a new language. Language examples: ``go``, ``kotlin``, ``scala``, ``rust``, ``groovy``, ``ruby``
#. Setup the DocOps approach using ``sphinx``
#. Update documentation with:

    #. how to install language on the Linux machine
    #. how to run ``hello world``
    #. how to declare data structures
    #. how to use conditions and loops
    #. how to import libraries and manage dependencies
    #. how to build the code
    #. how to write tests and run tests
    #. what are the advantages compared with another language

======
Task 2
======

#. Create a new project in your GitHub userspace, with a chosen language, that:
    #. Create a webapp that has:
        #. route ``/health`` that will give you status code 200
        #. route ``/version`` that will read from a ``CHANGELOG.md`` file.
        #. update default route ``/`` based use the `adjective` and `name` from ``source_code/containers/random_name.py`` to generate a random string next to the number of times you've visited the website.
        #. route ``/python ``to load the data from ``https://en.wikipedia.org/wiki/Python_(genus)`` and print a random python.
    #. Create a CLI that will:
        #. extract information about hostname, network, user, storage, memory
        #. store all the output in a log
        #. read arguments from a configuration file: you can enable and disable different information collection.

======
Task 3
======

#. Based on the previous applications add:
    #. unit tests to make sure that all the functions are running correctly
    #. extract the coverage
    #. add README.md documentation on how to install and run the applications

======
Task 4
======

#. Run the previous applications in Docker:
    #. create Dockerfile
    #. upload it to DockerHub
    #. deploy using Docker Swarm

======
Task 5
======

#. Create GitHub workflow for CI Pipeline (build and test the code)