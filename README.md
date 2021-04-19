# Giteo

[![GitHub version](https://badge.fury.io/gh/BoxingOctopus%2Fgiteo.svg)](https://badge.fury.io/gh/BoxingOctopus%2Fgiteo)
[![PyPI version](https://badge.fury.io/py/giteo.svg)](https://badge.fury.io/py/giteo)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/giteo)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/giteo)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/giteo)
![Docker Image Version (latest semver)](https://img.shields.io/docker/v/tuxotaku/giteo)

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

Giteo is a CLI-based URL shortener written in Python which uses GitHub's [git.io](https://git.io) URL shortening service.

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

- Python 3.7+
- Pipenv
- Docker (Optional)

### Development Setup

1. Fork this repo
2. Set up your Pipenv environment (`pipenv install`)
3. Set up your Docker environment (`docker build -t giteo:latest .`) (Optional)

### Installing

#### Bare Metal Install

`pip install giteo`

#### Docker Install

`docker pull TuxOtaku/giteo:latest`

## Usage <a name = "usage"></a>

### Bare Metal

`giteo --url <url_to_be_shortened> --code <shortened_url_suffix>`

### Docker
`docker run --rm TuxOtaku/giteo:latest --url <url_to_be_shortened> --code <shortened_url_suffix>`
