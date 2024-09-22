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
    <a href="https://docs.elgato.com/sdk" target="_blank">
        <img src="https://badgen.net/badge/Elgato/doc/blue" alt="Elgato">
    </a>
</p>

<p align="center">
      <a href="https://github.com/gri-gus/streamdeck-python-sdk" target="_blank">
        <img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
    </a>
</p>

# streamdeck-python-sdk

Library for creating Stream Deck plugins in Python.

**Supported operating systems:**

* MacOS: 10.14 or later
* Windows: 10 or later

**Supported Python versions:** 3.8 or later

## Installation

> ⚠️ For correct operation on Windows, it is recommended to enable `LongPaths` support in
> the system: [manual](https://www.backupery.com/how-to-enable-ntfs-long-paths-in-windows/).
> Without this setting, problems with installation and use may occur!

```shell
pip install "streamdeck-sdk[dev]"
```

## Features

* Ease of use. You can quickly create your own plugin without having to understand how websockets and
  other technologies work.
* Fully typed, using [pydantic](https://github.com/pydantic/pydantic).
* Includes image to base64 converters for easy installation of icons on keys.
* Includes a decorator for functions and methods to run on a separate thread.
* Exception logging and easy logging configuration.
* Debug mode via `PyCharm` or other debugging tools.
* A complete protocol for interaction with the Stream Deck application has been implemented.
* Quick start of a project via the console command `streamdeck_sdk startproject`.
* Build the project using the `streamdeck_sdk build` console command.
* Property Inspector Generator. Write code in Python and get html and js for PI.

## ⚠️ Limitations

1. During installation and update of the plugin, the Internet must be available.

### Windows

1. Plugin requirements should take no longer than 30 seconds to install. This is a feature of Stream Deck on Windows,
   since the program restarts the plugin if a websocket connection has not been established within 30 seconds.
   Therefore, you need a good Internet connection when installing and updating the plugin.

## Examples

[LoremFlickr](https://github.com/gri-gus/loremflickr-streamdeck-plugin) - Plugin for installing images on a button from
the LoremFlickr site. Supports MacOS and Windows.

[Proxy Manager](https://github.com/gri-gus/proxymanager-streamdeck-plugin) - Plugin for enabling and disabling
proxies on MacOS. Periodically polls the proxy status through a separate thread.

[One-time password](https://github.com/gri-gus/otp-streamdeck-plugin) - Plugin for generating one-time passwords,
like in Google Authenticator. Has several Actions. Supports MacOS and Windows.

---

See full description and usage examples on
[GitHub](https://github.com/gri-gus/streamdeck-python-sdk)
