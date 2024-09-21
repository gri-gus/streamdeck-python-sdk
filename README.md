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

> ⚠️ To work correctly on Windows, you need to enable `LongPaths` support in
> the system: [manual](https://www.backupery.com/how-to-enable-ntfs-long-paths-in-windows/).
> Without this setting, installation problems may occur!

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
* Property Inspector Generator. Write code in Python and get html and js for PI.

## ⚠️ Limitations

1. During installation and update of the plugin, the Internet must be available.

### Windows

1. Plugin requirements should take no longer than 30 seconds to install. This is a feature of Stream Deck on Windows,
   since the program restarts the plugin if a websocket connection has not been established within 30 seconds.
   Therefore, you need a good Internet connection when installing and updating the plugin.
2. You need to enable `LongPaths` support in the system
   registry: [manual](https://www.backupery.com/how-to-enable-ntfs-long-paths-in-windows/).

   Without this setting, the created plugins will not work!

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

⚠️ If you are using Windows and receive an error, then use the command:

```shell
streamdeck_sdk build -i com.bestdeveloper.mytestplugin.sdPlugin -F
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

## Property Inspector Generator

With this tool you can quickly write your Property Inspector in Python.
HTML and JS code will be generated.

In the application template from the `Quick Start` section there is a file
`com.bestdeveloper.mytestplugin.sdPlugin/property_inspector/myaction_pi.py`,
which provides an example of generating a Property Inspector into the file
``com.bestdeveloper.mytestplugin.sdPlugin/property_inspector/myaction_pi.html``.

Here are the elements available for generation in Python:

```python
from pathlib import Path

from streamdeck_sdk.property_inspector import *

OUTPUT_DIR = Path(__file__).parent
TEMPLATE = Path(__file__).parent / "pi_template.html"


class LoremFlickrStatus(BasePIElement):
    def get_html_element(self) -> str:
        res = """
    <div class="sdpi-item" style="max-height: 60px">
        <div class="sdpi-item-label">Website status</div>
        <div class="sdpi-item-value"
             style="background: #3D3D3D; height:26px; max-width: 56px; margin: 0 0 0 5px; padding: 0">
            <img src="https://img.shields.io/website?down_color=%233d3d3d&down_message=offline&label=&style=flat-square&up_color=%233d3d3d&up_message=online&url=https%3A%2F%2Floremflickr.com%2F"
                 alt="" style="height: 26px; max-width: 56px; margin: 0">
        </div>
    </div>
        """
        return res


def main():
    pi = PropertyInspector(
        action_uuid="com.ggusev.example.exampleaction",
        elements=[
            Heading(label="TEXT"),
            Textfield(
                label="Name",
                uid="name",
                required=True,
                pattern=".{2,}",
                placeholder="Input your name",
            ),
            Textfield(
                label="Text with default",
                uid="text_with_default",
                placeholder="Input default",
                default_value="default"
            ),
            Textfield(
                label="IP-Address",
                uid="my_ip_address",
                required=True,
                pattern=r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
                placeholder="e.g. 192.168.61.1",
            ),
            Textarea(
                label="Textarea",
                uid="textarea",
                placeholder="Input",
                max_length=100,
                info_text="100 max"
            ),
            Textarea(label="Textarea", uid="textarea_1", placeholder="Input", ),
            Password(
                label="Password",
                uid="password_input",
                required=True,
                pattern=".{2,}",
                placeholder="Input password",
                default_value="kitten",
            ),
            Heading(label="CHECKBOX & RADIO"),
            Radio(
                label="Union type",
                uid="union_type",
                items=[
                    RadioItem(
                        value="or",
                        label="or",
                        checked=False,
                    ),
                    RadioItem(
                        value="and",
                        label="and",
                        checked=True,
                    )
                ]
            ),
            Checkbox(
                label="Grayscale",
                items=[
                    CheckboxItem(
                        uid="grayscale_flag",
                        label="on",
                        checked=False,
                    ),
                ],
            ),
            Heading(label="FILE"),
            File(
                label="Select file",
                uid="my_file",
                accept=[".jpg", ".jpeg", ".png"],
            ),
            Heading(label="DATE & TIME"),
            DateTimeLocal(
                label="Select datetime",
                uid="my_datetime",
                default_value="2024-09-13T19:39",
            ),
            Date(
                label="Select date",
                uid="my_date",
                default_value="2019-01-15",
            ),
            Date(
                label="Select date",
                uid="my_date_1",
            ),
            Month(
                label="Select month",
                uid="my_month",
                default_value="2024-07",
            ),
            Week(
                label="Select week",
                uid="my_week",
                default_value="2024-W38",
            ),
            Time(
                label="Select time",
                uid="my_time",
                default_value="19:39",
            ),
            Heading(label="GROUP"),
            Group(
                label="My group",
                items=[
                    Radio(
                        label="Union type",
                        uid="my_group_union_type",
                        items=[
                            RadioItem(
                                value="or",
                                label="or",
                                checked=True,
                            ),
                            RadioItem(
                                value="and",
                                label="and",
                                checked=False,
                            )
                        ]
                    ),
                    Date(
                        label="Select date",
                        uid="my_group_my_date",
                        default_value="2019-01-15",
                    ),
                ]
            ),
            Heading(label="LINE"),
            Line(),
            Heading(label="COLOR"),
            Color(
                label="Color",
                uid="my_color",
                default_value="#240bda",
            ),
            Heading(label="PROGRESS & METER"),
            Meter(
                label="Meter",
                uid="my_meter_2",
                default_value=8,
                max_value=100,
            ),
            Meter(
                label="Meter",
                uid="my_meter_1",
                default_value=0.5,
                left_label="0",
                right_label="100",
            ),
            Progress(
                label="Progress",
                uid="my_progress_1",
                default_value=0.5,
            ),
            Progress(
                label="Progress",
                uid="my_progress_2",
                left_label="Min",
                right_label="Max",
                default_value=0.5,
            ),
            Heading(label="RANGE"),
            Range(
                label="Range",
                uid="my_range_2",
                min_value=0,
                max_value=50,
                default_value=20,
            ),
            Range(
                label="Range (+ll + rl)",
                uid="my_range_1",
                left_label="0",
                right_label="50",
                min_value=0,
                max_value=50,
                default_value=20,
            ),
            Range(
                label="Range(+stp)",
                uid="my_range_3",
                min_value=0,
                max_value=50,
                default_value=25,
                step=25,
            ),
            Range(
                label="Range(+dl +stp)",
                uid="my_range_4",
                min_value=0,
                max_value=50,
                default_value=25,
                datalist=["", "", "", ],
                step=25,
            ),
            Range(
                label="Range(+dl +lbl)",
                uid="my_range_5",
                min_value=0,
                max_value=100,
                default_value=25,
                datalist=["0", "50", "100", ],
            ),
            Heading(label="DETAILS"),
            Details(
                uid="my_full_width_details",
                full_width=True,
                heading="Full width details",
                text="""
                default open
                """,
                default_open=True,
            ),
            Details(
                uid="my_details_with_label",
                label="Details",
                heading="Info",
                text="My test info\nMy test info"
            ),
            Heading(label="MESSAGE"),
            Message(
                uid="my_message",
                heading="Example message",
                message_type=MessageTypes.INFO,
                text="Example message text",
            ),
            Message(
                uid="last_error",
                heading="Last error",
                message_type=MessageTypes.CAUTION,
                text="",
            ),
            Heading(label="SELECT"),
            Select(
                uid="my_select_1",
                label="Select",
                values=["1", "2", "3", "4"],
                default_value="2",
            ),
            Select(
                uid="my_select_2",
                label="Select 2",
                values=[],
            ),
            Heading(label="CUSTOM"),
            LoremFlickrStatus(),
        ]
    )
    pi.build(output_dir=OUTPUT_DIR, template=TEMPLATE)


if __name__ == '__main__':
    main()

```

> You can write your custom elements, for example as `LoremFlickrStatus`, and also edit `pi_template.html`
> at your discretion.

> `uid` is a future key in the `obj.payload.settings` dictionary.

> The same rules apply to `uid` as to variable naming in Python.

> `uid` must be unique within a single file for Property Inspector generation.

> All elements that contain `uid` are manipulable.

### Example of creating a Property Inspector and managing a field

For example, you made a Property Inspector like this and generated it:

```python
from pathlib import Path

from streamdeck_sdk.property_inspector import *

OUTPUT_DIR = Path(__file__).parent
TEMPLATE = Path(__file__).parent / "pi_template.html"


def main():
    pi = PropertyInspector(
        action_uuid="com.bestdeveloper.mytestplugin.myaction",
        elements=[
            Textfield(
                uid="my_input",
                label="My input",
                placeholder="Input text",
            ),
        ]
    )
    pi.build(output_dir=OUTPUT_DIR, template=TEMPLATE)


if __name__ == '__main__':
    # Run to generate Property Inspector
    main()
```

Then in the plugin's `Action` you can use code something like this to get the value from the `My input` field
and then change the value if needed:

```python
 def on_key_down(self, obj: events_received_objs.KeyDown):
    my_input_value = obj.payload.settings["my_input"]
    print(my_input_value)

    stngs = obj.payload.settings.copy()
    stngs["my_input"] = "12345"
    self.set_settings(
        context=obj.context,
        payload=stngs,
    )
```

After executing `self.set_settings` the value of the `My input` field will change to `12345`.

## Examples

[LoremFlickr](https://github.com/gri-gus/loremflickr-streamdeck-plugin) - Plugin for installing images on a button from
the LoremFlickr site. Supports MacOS and Windows.

[Proxy Manager](https://github.com/gri-gus/proxymanager-streamdeck-plugin) - Plugin for enabling and disabling
proxies on MacOS. Periodically polls the proxy status through a separate thread.

[One-time password](https://github.com/gri-gus/otp-streamdeck-plugin) - Plugin for generating one-time passwords,
like in Google Authenticator. Has several Actions. Supports MacOS and Windows.
