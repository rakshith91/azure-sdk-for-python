"""
FILE: cs5_publish_events_using_cloud_events_1.0_schema.py
DESCRIPTION:
    These samples demonstrate creating a list of CloudEvents and sending then as a list.
USAGE:
    python cs5_publish_events_using_cloud_events_1.0_schema.py
    Set the environment variables with your own values before running the sample:
    1) CLOUD_ACCESS_KEY - The access key of your eventgrid account.
    2) CLOUD_TOPIC_HOSTNAME - The topic hostname. Typically it exists in the format
    "<YOUR-TOPIC-NAME>.<REGION-NAME>.eventgrid.azure.net".
"""
from azure.eventgrid import EventGridPublisherClient, CloudEvent
from azure.core.credentials import AzureKeyCredential

topic_key = os.environ["CLOUD_ACCESS_KEY"]
topic_hostname = os.environ["CLOUD_TOPIC_HOSTNAME"]

credential = AzureKeyCredential(topic_key)
client = EventGridPublisherClient(topic_hostname, credential)

client.send([
    CloudEvent(
        type="Contoso.Items.ItemReceived",
        source="/contoso/items",
        data={
            "itemSku": "Contoso Item SKU #1"
        },
        subject="Door1"
    )
])
