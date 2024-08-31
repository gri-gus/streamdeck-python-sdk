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

После выполнения этого пункта появится папка `com.bestdeveloper.mytestplugin.sdPlugin` с тестовым проектом
и файлы для сборки.

5. Соберите плагин с помощью команды:

```shell
streamdeck_sdk build -i com.bestdeveloper.mytestplugin.sdPlugin
```

6. Установите плагин `releases/{date}/com.bestdeveloper.mytestplugin.streamDeckPlugin` в приложение Stream Deck.
   Обычно устанавливается через двойной клик.

> ⚠️ После установки нужно подождать примерно 40 секунд. В это время устанавливаются зависимости.

7. Зайдите приложение Stream Deck в категорию `MyTestCategory` и установить действие `My action` на какую-либо кнопку.
8. Проверить работу действия `My action`. При нажатии происходит следующее:
    1. Открывается страница github.
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

## Примеры

[LoremFlickr](https://github.com/gri-gus/loremflickr-streamdeck-plugin) - Плагин для установки изображений на кнопку
с сайта LoremFlickr. Поддерживает MacOS и Windows.
