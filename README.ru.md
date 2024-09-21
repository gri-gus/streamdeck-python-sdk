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

Библиотека для создания Stream Deck плагинов на Python.

**PyPi**: https://pypi.org/project/streamdeck-sdk/

**Поддерживаемые операционные системы:**

* MacOS: 10.14 or later
* Windows: 10 or later

**Поддерживаемые версии Stream Deck:** 6.0, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7

**Поддерживаемые версии Python:** 3.8 or later

## Установка

> ⚠️ Для корректной работы на Windows нужно включить поддержку `LongPaths` в
> системе: [manual](https://www.backupery.com/how-to-enable-ntfs-long-paths-in-windows/).
> Без этой настройки возможны проблемы с установкой!

```shell
pip install streamdeck-sdk
```

or

```shell
pip install streamdeck_sdk
```

## Возможности

* Простота использования. Вы можете быстро создать свой собственный плагин, не разбираясь в том,
  как работают веб-сокеты и другие технологии.
* Полная типизация с использованием [pydantic](https://github.com/pydantic/pydantic).
* Включает конвертер изображений в base64 для легкой установки значков на клавиши.
* Включает декоратор для функций и методов, запускаемых в отдельном потоке.
* Логирование исключений и простая настройка логирования.
* Debug режим через `PyCharm` или другие инструменты для отладки.
* Реализован полный протокол взаимодействия с приложением Stream Deck.
* Быстрый старт проекта через консольную команду `streamdeck_sdk startproject`.
* Сборка проекта через консольную команду `streamdeck_sdk build`.
* Генератор Property Inspector. Пишите код на Python и получите html и js для PI.

## ⚠️ Ограничения

1. Во время установки и обновления плагина должен быть доступен интернет.

### Windows

1. Зависимости плагина должны устанавливаться не дольше 30 секунд. Это особенность Stream Deck на Windows, так как
   программа перезапускает плагин, если в течение 30 секунд не было установлено websocket соединение. Поэтому нужен
   хороший интернет при установке и обновлении плагина.
2. Нужно включить поддержку `LongPaths` в реестре
   системы: [manual](https://www.backupery.com/how-to-enable-ntfs-long-paths-in-windows/).

   Без этой настройки созданные плагины не будут работать!

## Быстрый старт

1. Установите Python.
2. Создайте папку проекта и `venv`.
3. Перейдите в папку проекта, активируйте `venv` и установите библиотеку `streamdeck-sdk`:

```shell
pip install streamdeck-sdk
```

4. Выполните команду для старта проекта:

```shell
streamdeck_sdk startproject
```

После выполнения этого пункта появится папка `com.bestdeveloper.mytestplugin.sdPlugin` с тестовым проектом.

5. Соберите плагин с помощью команды:

```shell
streamdeck_sdk build -i com.bestdeveloper.mytestplugin.sdPlugin
```

6. Установите плагин `releases/{date}/com.bestdeveloper.mytestplugin.streamDeckPlugin` в приложение Stream Deck.
   Обычно устанавливается через двойной клик.

> ⚠️ После установки нужно подождать примерно 40 секунд. В это время устанавливаются зависимости.

7. Зайдите приложение Stream Deck в категорию `MyTestCategory` и установить действие `My action` на какую-либо кнопку.
8. Проверить работу действия `My action`. При нажатии происходит следующее:
    1. Открывается страница GitHub.
    2. Появляется ✅ на кнопке.

Далее отредактируйте проект в соответствии с официальной документацией [Stream Deck SDK](https://docs.elgato.com/sdk).

> ⚠️ Не забывайте редактировать файл `manifest.json` и название плагина.

## Debug режим

1. Выполните шаги 1-4 из раздела "Быстрый старт".
2. В файле `com.bestdeveloper.mytestplugin.sdPlugin/code/main.py`
   в параметрах StreamDeck укажите `debug=True`, как на примере:

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

3. Выполните шаги 5-7 из раздела "Быстрый старт".
4. Поставьте breakpoint в интересующем вас месте в `PyCharm`.
   К примеру, на строке:

```python
self.open_url("https://github.com/gri-gus/streamdeck-python-sdk")
```

5. Запустите файл `com.bestdeveloper.mytestplugin.sdPlugin/code/main.py` в режиме Debug в `PyCharm`.

> ⚠️ Если запустить только плагин в приложении Stream Deck, то реакции на нажатие кнопки не будет.

6. Нажмите кнопку на Stream Deck. Выполнение кода остановится на строке из пункта 4.

> ⚠️ Не забывайте установить `debug=False` при сборке готового плагина.

## Понимание использования

> Для начала ознакомьтесь с примерами плагинов ниже, а затем перейдите к этому разделу.

Давайте посмотрим на примере того, как работает метод `self.send_to_property_inspector`.

Посмотрим документацию от Elgato:

Вот объект, отправленный из плагина, когда вызывается
`self.send_to_property_inspector`: [click](https://docs.elgato.com/sdk/plugins/events-sent#sendtopropertyinspector)

Вот полученный объект в Property Inspector, когда вызывается
`self.send_to_property_inspector`: [click](https://docs.elgato.com/sdk/plugins/events-received#sendtopropertyinspector)

Вот исходный код метода для метода `self.send_to_property_inspector`:

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

Как мы видим, он принимает параметры функции и передает их объекту `events_sent_objs.SendToPropertyInspector`:

```python
class SendToPropertyInspector(BaseModel):
    action: str
    context: str
    payload: dict
    event: str = "sendToPropertyInspector"
```

Далее в методе `self.send` объект pydantic преобразуется в json и отправляется в Property Inspector плагина.

**Что такое `payload`?**

Это любой `dict`, который может преобразовываться в json.

**Как Property Inspector получает данные из `payload`?**

Чтобы ответить на этот вопрос, нужно посмотреть исходный код
[streamdeck-javascript-sdk](https://github.com/elgatosf/streamdeck-javascript-sdk).
В sdk есть метод
[onSendToPropertyInspector](https://github.com/elgatosf/streamdeck-javascript-sdk/blob/7d2ba3ce41620dbb6c2f2a69a158224f6d95ef22/js/property-inspector.js#L20)
и скорее всего его следует использовать так:

```js
$PI.onSendToPropertyInspector("com.ggusev.keyboard.write", jsn => {
    payload = jsn.payload; // I'm not sure about this, you need to test it
...
});
```

Вместо `"com.ggusev.keyboard.write"` вам нужно подставить название вашего `action`.

## Генератор Property Inspector

С помощью этого инструмента вы можете быстро писать свой Property Inspector на Python.
Код на html и js будет сгенерирован.

В шаблоне приложения из раздела `Быстрый старт` есть
файл `com.bestdeveloper.mytestplugin.sdPlugin/property_inspector/myaction_pi.py`,
в котором приведен пример генерации Property Inspector в
файл `com.bestdeveloper.mytestplugin.sdPlugin/property_inspector/myaction_pi.html`.

Вот элементы, доступные для генерации на Python:

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

> Вы можете писать свои кастомные элементы, к примеру как `LoremFlickrStatus`, а также редактировать `pi_template.html`
> на ваше усмотрение.

> `uid` - это будущий ключ в словаре `obj.payload.settings`.

> К `uid` применяются те же самые правила, что и к именованию переменных в Python.

> `uid` должен быть уникален в рамках одного файла для генерации Property Inspector.

> Все элементы, которые содержат `uid`, доступны для управления.

### Пример создания Property Inspector и управления полем

К примеру, вы сделали такой Property Inspector и сгенерировали его:

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

Тогда в `Action` плагина вы можете использовать примерно такой код для того, чтобы получить значение из поля `My input`,
а затем изменить значение, если это необходимо:

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

После выполнения `self.set_settings` значение поля `My input` изменится на `12345`.

## Примеры

[LoremFlickr](https://github.com/gri-gus/loremflickr-streamdeck-plugin) - Плагин для установки изображений на кнопку
с сайта LoremFlickr. Поддерживает MacOS и Windows.

[Proxy Manager](https://github.com/gri-gus/proxymanager-streamdeck-plugin) - Плагин для включения и
отключения прокси на MacOS. Периодически опрашивает состояние proxy через отдельный поток.

[One-time password](https://github.com/gri-gus/otp-streamdeck-plugin) - Плагин для генерации одноразовых паролей,
как в Google Authenticator. Имеет несколько Actions. Поддерживает MacOS и Windows.
