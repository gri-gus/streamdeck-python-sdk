import settings
from streamdeck_sdk import (
    StreamDeck,
    Action,
    events_received_objs,
)


class MyAction(Action):
    UUID = "com.bestdeveloper.mytestplugin.myaction"

    def on_key_down(self, obj: events_received_objs.KeyDown):
        self.open_url("https://github.com/gri-gus/streamdeck-python-sdk")
        self.show_ok(context=obj.context)


if __name__ == '__main__':
    StreamDeck(
        actions=[
            MyAction(),
        ],
        log_file=settings.LOG_FILE_PATH,
        log_level=settings.LOG_LEVEL,
        log_backup_count=1,
    ).run()
