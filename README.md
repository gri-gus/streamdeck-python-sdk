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

# streamdeck-python-sdk

Library for creating Stream Deck plugins in Python.

**PyPi**: https://pypi.org/project/streamdeck-sdk/

**Supported operating systems:**

* MacOS: 10.14 or later
* Windows: 10 or later

**Supported Stream Deck application:** 6.0, 6.1, 6.2

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

## How to use Documentation if it is not written?

> 🧑‍💻 Documentation under development

> To get started, take a look at the Examples of plugins below, then move on to this section.

Let's look at an example of how the `self.send_to_property_inspector` method works.

Let's look at the documentation from Elgato:

Here is the object sent from the plugin when
calling `self.send_to_property_inspector`: [click](https://docs.elgato.com/sdk/plugins/events-sent#sendtopropertyinspector)

Here is the resulting object in the Property inspector when
calling `self.send_to_property_inspector`: [click](https://docs.elgato.com/sdk/plugins/events-received#sendtopropertyinspector)

Here is the method source code for
the [self.send_to_property_inspector](https://github.com/gri-gus/streamdeck-python-sdk/blob/27652ed919cb85b94e91258487a2d2aba6087466/src/streamdeck_sdk/mixins.py#L177)
method:

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

As we can see, it accepts function parameters and transfers them to the
object [events_sent_objs.SendToPropertyInspector](https://github.com/gri-gus/streamdeck-python-sdk/blob/27652ed919cb85b94e91258487a2d2aba6087466/src/streamdeck_sdk/sd_objs/events_sent_objs.py#L121 ):

```python
class SendToPropertyInspector(BaseModel):
    action: str
    context: str
    payload: dict
    event: str = "sendToPropertyInspector"
```

Next in the
method [self.send](https://github.com/gri-gus/streamdeck-python-sdk/blob/27652ed919cb85b94e91258487a2d2aba6087466/src/streamdeck_sdk/mixins.py#L16)
the pydantic object is converted to json and sent to Property Inspector.

**What is `payload`?**

It's any `dict` you want. But there is a condition, it must be convertible to json.

**How Property inspector does receive payload data?**

To answer this question, you need to look at the source
code [streamdeck-javascript-sdk](https://github.com/elgatosf/streamdeck-javascript-sdk). As I understand, in their sdk
there is a
method [onSendToPropertyInspector](https://github.com/elgatosf/streamdeck-javascript-sdk/blob/7d2ba3ce41620dbb6c2f2a69a158224f6d95ef22/js/property-inspector.js#L20)
and most likely it should be used like this:

```js
$PI.onSendToPropertyInspector("com.ggusev.keyboard.write", jsn => {
    payload = jsn.payload; // I'm not sure about this, you need to test it
...
});
```

Instead of `"com.ggusev.keyboard.write"` you need to substitute the name of your action.

## Examples

[LoremFlickr](https://github.com/gri-gus/loremflickr-streamdeck-plugin) - Plugin for installing images from LoremFlickr
to button. Supports MacOS and Windows.

---
