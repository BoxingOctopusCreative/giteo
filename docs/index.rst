Welcome to giteo's documentation!
=================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Giteo
=====


.. image:: https://badge.fury.io/gh/BoxingOctopus%2Fgiteo.svg
   :target: https://badge.fury.io/gh/BoxingOctopus%2Fgiteo
   :alt: GitHub version


.. image:: https://badge.fury.io/py/giteo.svg
   :target: https://badge.fury.io/py/giteo
   :alt: PyPI version


.. image:: https://img.shields.io/pypi/wheel/giteo
   :target: https://img.shields.io/pypi/wheel/giteo
   :alt: PyPI - Wheel


.. image:: https://img.shields.io/pypi/implementation/giteo
   :target: https://img.shields.io/pypi/implementation/giteo
   :alt: PyPI - Implementation


.. image:: https://img.shields.io/pypi/pyversions/giteo
   :target: https://img.shields.io/pypi/pyversions/giteo
   :alt: PyPI - Python Version


.. image:: https://img.shields.io/docker/v/tuxotaku/giteo
   :target: https://img.shields.io/docker/v/tuxotaku/giteo
   :alt: Docker Image Version (latest semver)


.. image:: https://img.shields.io/pypi/l/giteo
   :target: https://img.shields.io/pypi/l/giteo
   :alt: PyPI - License


.. image:: https://img.shields.io/docker/cloud/build/tuxotaku/giteo
   :alt: Docker Cloud Build Status


About
-----

Giteo is a CLI-based URL shortener written in Python which uses GitHub's `git.io <https://git.io>`_ URL shortening service.

Getting Started
---------------

These instructions will get you a copy of the project up and running on your local machine.

Prerequisites
^^^^^^^^^^^^^


* Python 3.7+
* Pipenv
* Docker (Optional)

Development Setup
^^^^^^^^^^^^^^^^^


#. Fork this repo
#. Set up your Pipenv environment (\ ``pipenv install``\ )
#. Set up your Docker environment (\ ``docker build -t giteo:latest .``\ ) (Optional)

Installing
^^^^^^^^^^

Bare Metal Install
~~~~~~~~~~~~~~~~~~

``pip install giteo``

Docker Install
~~~~~~~~~~~~~~

``docker pull TuxOtaku/giteo:latest``

Usage
-----

Bare Metal
^^^^^^^^^^

``giteo --url <url_to_be_shortened> --code <shortened_url_suffix>``

Docker
^^^^^^

``docker run --rm TuxOtaku/giteo:latest --url <url_to_be_shortened> --code <shortened_url_suffix>``
