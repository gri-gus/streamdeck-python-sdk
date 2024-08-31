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
    <a href="https://github.com/gri-gus/streamdeck-python-sdk/blob/main/README.md" target="_blank">
        <img src="https://img.shields.io/badge/lang-en-yellow.svg" alt="lang-ru">
    </a>
    <a href="https://github.com/gri-gus/streamdeck-python-sdk/blob/main/README.ru.md" target="_blank">
        <img src="https://img.shields.io/badge/lang-ru-yellow.svg" alt="lang-ru">
    </a>
</p>

# streamdeck-python-sdk

Library for creating Stream Deck plugins in Python.

**PyPi**: https://pypi.org/project/streamdeck-sdk/

**Supported operating systems:**

* MacOS: 10.14 or later
* Windows: 10 or later

**Supported Stream Deck versions:** 6.0, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7

**Supported Python versions:** 3.8 or later

## Installation

```shell
pip install streamdeck-sdk
```

or

```shell
pip install streamdeck_sdk
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

## Quick Start

1. Install Python.
2. Create a project folder and `venv`.
3. Go to the project folder, activate `venv` and install the `streamdeck-sdk` library:

```shell
pip install streamdeck-sdk
```

4. Run the command to start the project:

```shell
streamdeck_sdk startproject
```

After completing this step, the folder `com.bestdeveloper.mytestplugin.sdPlugin` will appear with a test project.

5. Build the plugin using the command:

```shell
streamdeck_sdk build -i com.bestdeveloper.mytestplugin.sdPlugin
```

6. Install the `releases/{date}/com.bestdeveloper.mytestplugin.streamDeckPlugin` plugin into the Stream Deck
   application. Usually installed via double click.

> ⚠️ After installation, you need to wait about 40 seconds. At this time, requirements are installed.

7. Go to the Stream Deck application in the `MyTestCategory` category and set the `My action` action to any button.
8. Check the operation of the `My action` action.
   When clicked, the following happens:
    1. The GitHub page opens.
    2. ✅ appears on the button.

Next, edit the project in accordance with the official documentation [Stream Deck SDK](https://docs.elgato.com/sdk).
> ⚠️ Don't forget to edit the `manifest.json` file and the plugin name.

## Debug mode

1. Follow steps 1-4 from the "Quick Start" section.
2. In the file `com.bestdeveloper.mytestplugin.sdPlugin/code/main.py`
   in the StreamDeck parameters, specify `debug=True`, as in the example:

```python
if __name__ == '__main__':
    StreamDeck(
        actions=[
            MyAction(),
        ],
        debug=True,
        log_file=settings.LOG_FILE_PATH,
        log_level=settings.LOG_LEVEL,
        log_backup_count=1,
    ).run()
```

3. Follow steps 5-7 from the "Quick Start" section.
4. Place a breakpoint where you are interested in `PyCharm`.
   For example, on the line:

```python
self.open_url("https://github.com/gri-gus/streamdeck-python-sdk")
```

5. Run the file `com.bestdeveloper.mytestplugin.sdPlugin/code/main.py` in Debug mode in `PyCharm`.

> ⚠️ If you run only the plugin in the Stream Deck application, there will be no reaction to pressing the button.

6. Click the button on Stream Deck. The code execution will stop at the line from point 4.

> ⚠️ Don't forget to set `debug=False` when building the finished plugin.

## Understanding usage

> To get started, check out the sample plugins below, then continue on to this section.

Let's look at an example of how the `self.send_to_property_inspector` method works.

Let's look at the documentation from Elgato:

Here is the object sent from the plugin when
calling `self.send_to_property_inspector`: [click](https://docs.elgato.com/sdk/plugins/events-sent#sendtopropertyinspector)

Here is the resulting object in the Property inspector when
calling `self.send_to_property_inspector`: [click](https://docs.elgato.com/sdk/plugins/events-received#sendtopropertyinspector)

Here is the source code for the method `self.send_to_property_inspector` method:

```python
def send_to_property_inspector(
        self,
        action: str,
        context: str,
        payload: dict
):
    message = events_sent_objs.SendToPropertyInspector(
        action=action,
        context=context,
        payload=payload
    )
    self.send(message)
```

As we can see, it takes function parameters and passes them to the object `events_sent_objs.SendToPropertyInspector`:

```python
class SendToPropertyInspector(BaseModel):
    action: str
    context: str
    payload: dict
    event: str = "sendToPropertyInspector"
```

Next, in the `self.send` method, the pydantic object is converted to json and sent to the plugin’s Property Inspector.

**What is `payload`?**

This is any `dict` that can be converted to json.

**How does Property Inspector get data from `payload`?**

To answer this question, you need to look at the source
code [streamdeck-javascript-sdk](https://github.com/elgatosf/streamdeck-javascript-sdk).
There is a method in the sdk
[onSendToPropertyInspector](https://github.com/elgatosf/streamdeck-javascript-sdk/blob/7d2ba3ce41620dbb6c2f2a69a158224f6d95ef22/js/property-inspector.js#L20)
and most likely it should be used like this:

```js
$PI.onSendToPropertyInspector("com.ggusev.keyboard.write", jsn => {
    payload = jsn.payload; // I'm not sure about this, you need to test it
...
});
```

Instead of `"com.ggusev.keyboard.write"` you need to substitute the name of your `action`.

## Examples

[LoremFlickr](https://github.com/gri-gus/loremflickr-streamdeck-plugin) - Plugin for installing images on a button from
the LoremFlickr site. Supports MacOS and Windows.
