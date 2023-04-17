<p align="center">
    <a>
        <img src="https://raw.githubusercontent.com/gri-gus/streamdeck-python-sdk/main/assets/images/cover.png" alt="streamdeck-python-sdk">
    </a>
</p>

<p align="center">
    <a href="https://pypi.org/project/streamdeck-sdk" target="_blank">
        <img src="https://img.shields.io/pypi/v/streamdeck-sdk" alt="PyPI">
    </a>
    <a href="https://pypi.org/project/streamdeck-sdk" target="_blank">
        <img src="https://static.pepy.tech/badge/streamdeck-sdk" alt="PyPI">
    </a>
    <a href="https://opensource.org/licenses/Apache-2.0" target="_blank">
        <img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg" alt="Apache">
    </a>
    <a href="https://developer.elgato.com/documentation/stream-deck/sdk/overview/" target="_blank">
        <img src="https://badgen.net/badge/Elgato/doc/blue" alt="Elgato">
    </a>
</p>

# streamdeck-python-sdk

Library for creating Stream Deck plugins in Python.

**PyPi**: https://pypi.org/project/streamdeck-sdk/

**Supported operating systems:**

* MacOS: 10.14 or later
* Windows: 10 or later

**Supported Stream Deck application:** 6.0, 6.1

**Supported Python:** 3.7 or later

## Installation

```shell
pip install streamdeck-sdk
```

or

```shell
pip install streamdeck_sdk
```

## Features

* Easy use. You can quickly create your own plugin without having to understand how websockets and other complicated
  things work.
* Fully typed, using [pydantic](https://github.com/pydantic/pydantic).
* Includes image to base64 converters for easy installation of icons on keys.
* Includes a decorator for functions and methods to run on a separate thread.
* Exception logging and easy logging configuration.

## Examples

[LoremFlickr](https://github.com/gri-gus/loremflickr-streamdeck-plugin) - Plugin for installing images from LoremFlickr
to button. Supports MacOS and Windows.

---
> 🧑‍💻 Documentation under development