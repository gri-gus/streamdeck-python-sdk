import json
import logging
from typing import Union, Optional

import pydantic

from ..logger import log_errors
from ..sd_objs import events_sent_objs
from ..simple_ws.client import WebSocketClientApp

logger = logging.getLogger(__name__)


class SendMixin:
    ws: WebSocketClientApp

    @log_errors
    def send(
            self,
            data: Union[pydantic.BaseModel, dict, str]
    ) -> None:
        """
        Converts the data value to json and sends it.
        """
        if isinstance(data, pydantic.BaseModel):
            data = json.dumps(data.model_dump(), ensure_ascii=True)
        elif isinstance(data, dict):
            data = json.dumps(data, ensure_ascii=False)
        elif isinstance(data, str):
            pass
        else:
            logger.warning(f"Invalid data type {type(data)} to send. The message will not be sent! data={data}")
            return
        self.ws.send(data)


class EventsSendMixin(SendMixin):
    plugin_uuid: str

    def get_global_settings(
            self,
    ) -> None:
        """
        The plugin and Property Inspector can request the persistent global data using the getGlobalSettings event.
        The plugin or Property Inspector will receive asynchronously an event didReceiveGlobalSettings the p
        containing the global settings.

        https://docs.elgato.com/sdk/plugins/events-sent#getglobalsettings
        """
        message = events_sent_objs.GetGlobalSettings(
            context=self.plugin_uuid,
        )
        self.send(message)

    def get_settings(
            self,
            context: str,
    ) -> None:
        """
        The plugin and Property Inspector can request the persistent data stored for the action's
        instance using the getSettings event.

        https://docs.elgato.com/sdk/plugins/events-sent#getsettings

        :param context: A value to Identify the instance's action or Property Inspector. In the case of
            the Property Inspector, this value is received by the Property Inspector as parameter of
            the connectElgatoStreamDeckSocket function.
        """
        message = events_sent_objs.GetSettings(
            context=context,
        )
        self.send(message)

    def log_message(
            self,
            message: str,
    ) -> None:
        r"""
        The plugin and Property Inspector can use the logMessage event to write a debug message to the logs file.
        * Logs are saved to disk per plugin in the folder ~/Library/Logs/ElgatoStreamDeck/ on macOS
        and %appdata%\Elgato\StreamDeck\logs\ on Windows. Note that the log files are rotated each time
        the Stream Deck application is relaunched.

        https://docs.elgato.com/sdk/plugins/events-sent#logmessage

        :param message: A string to write to the logs file.
        """
        message = events_sent_objs.LogMessage(
            payload=events_sent_objs.LogMessagePayload(
                message=message,
            ),
        )
        self.send(message)

    def open_url(
            self,
            url: str,
    ) -> None:
        """
        The plugin and Property Inspector can tell the Stream Deck application to open URL in the
        default browser using the openUrl event.

        https://docs.elgato.com/sdk/plugins/events-sent#openurl

        :param url: An URL to open in the default browser.
        """
        message = events_sent_objs.OpenUrl(
            payload=events_sent_objs.OpenUrlPayload(
                url=url,
            ),
        )
        self.send(message)

    def send_to_property_inspector(
            self,
            action: str,
            context: str,
            payload: dict,
    ) -> None:
        """
        The plugin can send a payload to the Property Inspector using the sendToPropertyInspector event.
        The Property Inspector will receive asynchronously an event sendToPropertyInspector.

        https://docs.elgato.com/sdk/plugins/events-sent#sendtopropertyinspector

        :param action: The action's unique identifier.
        :param context: A value to identify the instance's action.
        :param payload: A JSON object that will be received by the Property Inspector.
        """
        message = events_sent_objs.SendToPropertyInspector(
            action=action,
            context=context,
            payload=payload,
        )
        self.send(message)

    def set_feedback(
            self,
            context: str,
            payload: dict,
    ) -> None:
        """
        (SD+)
        The plugin can send a setFeedback event to the Stream Deck application to dynamically change properties of
        items on the Stream Deck + touch display layout.

        https://docs.elgato.com/sdk/plugins/events-sent#setfeedback-sd

        :param context: A value to Identify the instance's action you want to modify.
        :param payload: A dict object.
            key: The key is a name of the element in layout to be changed with given value.
            value: The value to be set in key named layout element.
        """
        message = events_sent_objs.SetFeedback(
            context=context,
            payload=payload,
        )
        self.send(message)

    def set_feedback_layout(
            self,
            context: str,
            layout: str,
    ) -> None:
        """
        (SD+)
        The plugin can send a setFeedbackLayout event to the Stream Deck application to dynamically change the
        current Stream Deck + touch display layout. setFeedbackLayout can use the id of a built-in layout or
        a relative path to a custom layout JSON file. See Layouts for more information.

        https://docs.elgato.com/sdk/plugins/events-sent#setfeedbacklayout-sd

        :param context: A value to Identify the instance's action you want to modify.
        :param layout: A predefined layout identifier or the relative path to a json file that
            contains a custom layout.
        """
        message = events_sent_objs.SetFeedbackLayout(
            context=context,
            payload=events_sent_objs.SetFeedbackLayoutPayload(
                layout=layout,
            ),
        )
        self.send(message)

    def set_global_settings(
            self,
            payload: dict,
    ) -> None:
        """
        The plugin and Property Inspector can save persistent data globally. The data
        will be saved securely to the Keychain on macOS and the Credential Store on Windows. This API can
        be used to save tokens that should be available to every action in the plugin.
        Note that when the plugin uses this API, the Property Inspector will automatically receive
        a didReceiveGlobalSettings callback with the new settings. Similarly, when the Property Inspector uses
        this API, the plugin will automatically receive a didReceiveGlobalSettings callback with the new settings.
        This API has been introduced in Stream Deck 4.1.

        https://docs.elgato.com/sdk/plugins/events-sent#setglobalsettings

        :param payload: A JSON object which is persistently saved globally.
        """
        message = events_sent_objs.SetGlobalSettings(
            context=self.plugin_uuid,
            payload=payload,
        )
        self.send(message)

    def set_image(
            self,
            context: str,
            image: str,  # base64
            target: int = 0,
            state: Optional[int] = None,
    ) -> None:
        """
        The plugin can send a setImage event to the Stream Deck application to dynamically change the image displayed
        by an instance of an action.

        https://docs.elgato.com/sdk/plugins/events-sent#setimage

        :param context: A value to Identify the instance's action you want to modify.
        :param image: The image to display encoded in base64 with the image format declared in the mime
            type (PNG, JPEG, BMP, ...). svg is also supported. If not provided, the image is
            reset to the default image from the manifest.
            You can use functions from image_converters.py for convert image in base64.
        :param target: Specify if you want to display the title on the hardware and software (0),
            only on the hardware (1), or only on the software (2). Default is 0.
        :param state: A 0-based integer value representing the state of an action with multiple states. If not
            specified, the image is set to all states.
        """
        message = events_sent_objs.SetImage(
            context=context,
            payload=events_sent_objs.SetImagePayload(
                image=image,
                target=target,
                state=state,
            ),
        )
        self.send(message)

    def set_settings(
            self,
            context: str,
            payload: dict,
    ) -> None:
        """
        The plugin and Property Inspector can save data persistently for the action's instance using
        the setSettings event.
        Note that when the plugin uses this API, the Property Inspector will automatically receive a didReceiveSettings
        callback with the new settings. Similarly, when the Property Inspector uses this API, the plugin will
        automatically receive a didReceiveSettings callback with the new settings.
        The setSettings API is available since Stream Deck 4.0 for the plugin. Starting
        with Stream Deck 4.1, this API is available from the Property Inspector.

        https://docs.elgato.com/sdk/plugins/events-sent#setsettings

        :param context: A value to Identify the instance's action or Property Inspector. This value is received
            by the Property Inspector as a parameter of the connectElgatoStreamDeckSocket function.
        :param payload: A JSON object which is persistently saved for the action's instance.
        """
        message = events_sent_objs.SetSettings(
            context=context,
            payload=payload,
        )
        self.send(message)

    def set_state(
            self,
            context: str,
            state: int,
    ) -> None:
        """
        This function can be used by a plugin to dynamically change the state of an action supporting multiple states.

        https://docs.elgato.com/sdk/plugins/events-sent#setstate

        :param context: A value to identify the instance's action.
        :param state: A 0-based integer value representing the state requested.
        """
        message = events_sent_objs.SetState(
            context=context,
            payload=events_sent_objs.SetStatePayload(
                state=state,
            )
        )
        self.send(message)

    def set_title(
            self,
            context: str,
            title: str,
            target: int = 0,
            state: Optional[int] = None,
    ) -> None:
        """
        The plugin can send a setTitle event to the Stream Deck application to dynamically change the title
        displayed by an instance of an action.
        * Note: Show the title on your hardware or software using the Show Title checkbox in the Stream Deck window.

        https://docs.elgato.com/sdk/plugins/events-sent#settitle

        :param context: A value to Identify the instance's action you want to modify.
        :param title: The title to display. If there is no title parameter, the title is reset to the title set
            by the user.
        :param target: Specify if you want to display the title on the hardware and software (0), only on the
            hardware (1), or only on the software (2). Default is 0.
        :param state:  A 0-based integer value representing the state of an action with multiple states. If not
            specified, the title is set to all states.
        """
        message = events_sent_objs.SetTitle(
            context=context,
            payload=events_sent_objs.SetTitlePayload(
                title=title,
                target=target,
                state=state,
            ),
        )
        self.send(message)

    def set_trigger_description(
            self,
            context: str,
            *,
            long_touch: Optional[str] = None,
            push: Optional[str] = None,
            rotate: Optional[str] = None,
            touch: Optional[str] = None,
    ) -> None:
        """
        (SD+)
        Sets the trigger descriptions associated with an encoder (touch display + dial) action instance.
        All descriptions are optional; when one or more descriptions are defined all descriptions are
        updated, with undefined values having their description hidden in Stream Deck.
        To reset the descriptions to the default values defined
        within the manifest, an empty payload can be sent as part of the event.

        https://docs.elgato.com/sdk/plugins/events-sent#settriggerdescription-sd

        :param context: A value to identify the instance's action.
        :param long_touch: Optional value that describes the long-touch interaction with the touch display. When
            undefined the description will be hidden.
        :param push: Optional value that describes the push interaction with the dial. When undefined the
            description will be hidden.
        :param rotate: Optional value that describes the rotate interaction with the dial. When undefined
            the description will be hidden.
        :param touch: Optional value that describes the touch interaction with the touch display. When undefined
            the description will be hidden.
        """
        message = events_sent_objs.SetTriggerDescription(
            context=context,
            payload=events_sent_objs.SetTriggerDescriptionPayload(
                longTouch=long_touch,
                push=push,
                rotate=rotate,
                touch=touch,
            ),
        )
        self.send(message)

    def show_alert(
            self,
            context: str,
    ) -> None:
        """
        The plugin can send a showAlert event to the Stream Deck application to temporarily show an alert icon on the
        image displayed by an instance of an action.

        https://docs.elgato.com/sdk/plugins/events-sent#showalert

        :param context: A value to identify the instance's action.
        """
        message = events_sent_objs.ShowAlert(
            context=context,
        )
        self.send(message)

    def show_ok(
            self,
            context: str,
    ) -> None:
        """
        The plugin can send a showOk event to the Stream Deck application to temporarily show an OK checkmark icon on
        the image displayed by an instance of an action.

        https://docs.elgato.com/sdk/plugins/events-sent#showok

        :param context: A value to identify the instance's action.
        """
        message = events_sent_objs.ShowOk(
            context=context,
        )
        self.send(message)

    def switch_to_profile(
            self,
            device: str,
            profile: str,
            page: int,
    ) -> None:
        """
        The plugin can tell the Stream Deck application to switch to one of his preconfigured read-only profile
        using the switchToProfile event.
        * Note that a plugin can only switch to read-only profiles declared in its manifest.json file. If the profile
        field is missing or empty, the Stream Deck application will switch to the previously selected profile.

        https://docs.elgato.com/sdk/plugins/events-sent#switchtoprofile

        :param device: A value to identify the device.
        :param profile: The name of the profile to switch to. The name should be identical to the name provided
            in the manifest.json file.
        :param page: Page to show when switching to the profile; indexed from 0.
        """
        message = events_sent_objs.SwitchToProfile(
            context=self.plugin_uuid,
            device=device,
            payload=events_sent_objs.SwitchToProfilePayload(
                profile=profile,
                page=page,
            ),
        )
        self.send(message)
