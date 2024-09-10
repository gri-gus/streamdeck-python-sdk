from pathlib import Path

from streamdeck_sdk.property_inspector import *

OUTPUT_DIR = Path(__file__).parent
TEMPLATE = Path(__file__).parent / "pi_template.html"


def main():
    pi = PropertyInspector(
        action_uuid="com.bestdeveloper.mytestplugin.myaction",
        elements=[
            Message(
                uid="my_message",
                heading="Example message",
                message_type=MessageTypes.INFO,
                text="Example message text",
            ),
        ]
    )
    pi.build(output_dir=OUTPUT_DIR, template=TEMPLATE)


if __name__ == '__main__':
    # Run to generate Property Inspector
    main()
