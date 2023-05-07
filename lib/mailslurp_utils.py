# mailslurp_utils.py

from mailslurp_client import ApiClient, Configuration, InboxControllerApi, WaitForControllerApi
from mailslurp_client.models import CreateInboxDto
from mailslurp_client.rest import ApiException


def create_mailslurp_inbox(api_key):
    configuration = Configuration()
    configuration.api_key['x-api-key'] = api_key
    api_client = ApiClient(configuration)
    inbox_controller = InboxControllerApi(api_client)

    try:
        new_inbox = inbox_controller.create_inbox()
        return new_inbox
    except ApiException as e:
        print("An exception occurred while creating the MailSlurp inbox: %s\n" % e)
        return None


def wait_for_latest_email(api_key, inbox):
    configuration = Configuration()
    configuration.api_key['x-api-key'] = api_key
    api_client = ApiClient(configuration)
    wait_for_controller = WaitForControllerApi(api_client)

    try:
        latest_email = wait_for_controller.wait_for_latest_email(inbox_id=inbox.id, timeout=60000, unread_only=True)
        return latest_email
    except ApiException as e:
        print("An exception occurred while waiting for the latest email: %s\n" % e)
        return None
