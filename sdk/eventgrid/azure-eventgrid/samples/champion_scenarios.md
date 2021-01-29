## Send Scenarios

### Send a Single EventGridEvent as a strongly typed object

```Python
import os
from azure.eventgrid import EventGridPublisherClient, EventGridEvent
from azure.core.credentials import AzureKeyCredential

topic_key = os.environ["EG_ACCESS_KEY"]
endpoint = os.environ["EG_TOPIC_HOSTNAME"]

credential = AzureKeyCredential(topic_key)
client = EventGridPublisherClient(endpoint, credential)

event = EventGridEvent(
		event_type="Contoso.Items.ItemReceived",
		data={
			"itemSku": "Contoso Item SKU #1"
		},
		subject="Door1",
		data_version="2.0"
	)

client.send(event)
```

### Send a Single CloudEvent as a strongly typed object

```Python
import os
from azure.eventgrid import EventGridPublisherClient, CloudEvent
from azure.core.credentials import AzureKeyCredential

topic_key = os.environ["CLOUD_ACCESS_KEY"]
endpoint = os.environ["CLOUD_TOPIC_HOSTNAME"]

credential = AzureKeyCredential(topic_key)
client = EventGridPublisherClient(endpoint, credential)

event = CloudEvent(
        type="Contoso.Items.ItemReceived",
        source="/contoso/items",
        data={
            "itemSku": "Contoso Item SKU #1"
        },
        subject="Door1"
    )

client.send(event)
```

### Send multiple EventGridEvents as strongly typed objects

```Python
import os
from azure.eventgrid import EventGridPublisherClient, EventGridEvent
from azure.core.credentials import AzureKeyCredential

topic_key = os.environ["EG_ACCESS_KEY"]
endpoint = os.environ["EG_TOPIC_HOSTNAME"]

credential = AzureKeyCredential(topic_key)
client = EventGridPublisherClient(endpoint, credential)

event0 = EventGridEvent(
		event_type="Contoso.Items.ItemReceived",
		data={
			"itemSku": "Contoso Item SKU #1"
		},
		subject="Door1",
		data_version="2.0"
	)

event1 = EventGridEvent(
		event_type="Contoso.Items.ItemReceived",
		data={
			"itemSku": "Contoso Item SKU #2"
		},
		subject="Door1",
		data_version="2.0"
	)

client.send([event0, event1])
```

### Send multiple CloudEvents as a strongly typed objects

```Python
import os
from azure.eventgrid import EventGridPublisherClient, CloudEvent
from azure.core.credentials import AzureKeyCredential

topic_key = os.environ["CLOUD_ACCESS_KEY"]
endpoint = os.environ["CLOUD_TOPIC_HOSTNAME"]

credential = AzureKeyCredential(topic_key)
client = EventGridPublisherClient(endpoint, credential)

event0 = CloudEvent(
        type="Contoso.Items.ItemReceived",
        source="/contoso/items",
        data={
            "itemSku": "Contoso Item SKU #1"
        },
        subject="Door1"
    )
event1 = CloudEvent(
        type="Contoso.Items.ItemReceived",
        source="/contoso/items",
        data={
            "itemSku": "Contoso Item SKU #2"
        },
        subject="Door1"
    )

client.send([event0, event1])
```

### Send a Single EventGridEvent as a Dictionary

```Python
import os
from azure.eventgrid import EventGridPublisherClient
from azure.core.credentials import AzureKeyCredential
from datetime import datetime

topic_key = os.environ["EG_ACCESS_KEY"]
endpoint = os.environ["EG_TOPIC_HOSTNAME"]

credential = AzureKeyCredential(topic_key)
client = EventGridPublisherClient(endpoint, credential)

event = {
    "eventType": "Contoso.Items.ItemReceived",
    "data": {
		"itemSku": "Contoso Item SKU #1"
	},
	"subject": "Door1",
	"dataVersion": "2.0",
    "id": "randomuuid1",
    "eventTime": datetime(2021, 1, 21, 17, 37)
}

client.send(event)
```

### Send a Single CloudEvent as a dictionary

```Python
import os
from azure.eventgrid import EventGridPublisherClient, CloudEvent
from azure.core.credentials import AzureKeyCredential

topic_key = os.environ["CLOUD_ACCESS_KEY"]
endpoint = os.environ["CLOUD_TOPIC_HOSTNAME"]

credential = AzureKeyCredential(topic_key)
client = EventGridPublisherClient(endpoint, credential)

event = {
        "type": "Contoso.Items.ItemReceived",
        "source": "/contoso/items",
        "data": {
            "itemSku": "Contoso Item SKU #1"
        },
        "subject": "Door1",
        "specversion": "1.0",
        "id": "randomclouduuid1"
}

client.send(event)
```

### Send multiple EventGridEvents as dictionaries

```Python
import os
from azure.eventgrid import EventGridPublisherClient, EventGridEvent
from azure.core.credentials import AzureKeyCredential
from datetime import datetime

topic_key = os.environ["EG_ACCESS_KEY"]
endpoint = os.environ["EG_TOPIC_HOSTNAME"]

credential = AzureKeyCredential(topic_key)
client = EventGridPublisherClient(endpoint, credential)

event0 = {
    "eventType": "Contoso.Items.ItemReceived",
    "data": {
		"itemSku": "Contoso Item SKU #1"
	},
	"subject": "Door1",
	"dataVersion": "2.0",
    "id": "randomuuid11",
    "eventTime": datetime(2021, 1, 21, 17, 37)
}

event1 = {
    "eventType": "Contoso.Items.ItemReceived",
    "data": {
		"itemSku": "Contoso Item SKU #2"
	},
	"subject": "Door1",
	"dataVersion": "2.0",
    "id": "randomuuid12",
    "eventTime": datetime(2021, 1, 21, 17, 37)
}

client.send([event0, event1])
```

### Send multiple CloudEvents as dictionaries

```Python
import os
from azure.eventgrid import EventGridPublisherClient, CloudEvent
from azure.core.credentials import AzureKeyCredential

topic_key = os.environ["CLOUD_ACCESS_KEY"]
endpoint = os.environ["CLOUD_TOPIC_HOSTNAME"]

credential = AzureKeyCredential(topic_key)
client = EventGridPublisherClient(endpoint, credential)

event0 = {
        "type": "Contoso.Items.ItemReceived",
        "source": "/contoso/items",
        "data": {
            "itemSku": "Contoso Item SKU #1"
        },
        "subject": "Door1",
        "specversion": "1.0",
        "id": "randomclouduuid11"
}

event1 = {
        "type": "Contoso.Items.ItemReceived",
        "source": "/contoso/items",
        "data": {
            "itemSku": "Contoso Item SKU #2"
        },
        "subject": "Door1",
        "specversion": "1.0",
        "id": "randomclouduuid12"
}

client.send([event0, event1])
```

### Send a single CustomEvent schema

```Python
import os
from azure.eventgrid import EventGridPublisherClient, CustomEvent
from azure.core.credentials import AzureKeyCredential

topic_key = os.environ["CUSTOM_SCHEMA_ACCESS_KEY"]
endpoint = os.environ["CUSTOM_SCHEMA_TOPIC_HOSTNAME"]

credential = AzureKeyCredential(topic_key)
client = EventGridPublisherClient(endpoint, credential)

event = CustomEvent(
		custom_event_type="Contoso.Items.ItemReceived",
		data={
			"itemSku": "Contoso Item SKU #2"
		},
		custom_subject="Door1",
		custom_data_version="2.0"
	)
client.send(event)
```

### Send CustomEvent schema as a dict

```Python
import os
from azure.eventgrid import EventGridPublisherClient, CustomEvent
from azure.core.credentials import AzureKeyCredential

topic_key = os.environ["CUSTOM_SCHEMA_ACCESS_KEY"]
endpoint = os.environ["CUSTOM_SCHEMA_TOPIC_HOSTNAME"]

credential = AzureKeyCredential(topic_key)
client = EventGridPublisherClient(endpoint, credential)

event = {
        "custom_event_type":"Contoso.Items.ItemReceived",
		"data":{
			"itemSku": "Contoso Item SKU #2"
		},
        "custom_subject":"Door1",
		"custom_data_version":"2.0"
}

client.send(event)
```

## Receive Scenarios

### Deserialize EventGrid Events payload

```Python
from azure.eventgrid import EventGridDeserializer

eg_storage_dict = "[{\"id\": \"56afc886-767b-d359-d59e-0da7877166b2\", \"topic\": \
	\"/SUBSCRIPTIONS/ID/RESOURCEGROUPS/rg/PROVIDERS/MICROSOFT.ContainerRegistry/test1\", \
	\"subject\": \"test1\", \"eventType\": \"Microsoft.AppConfiguration.KeyValueDeleted\",\
	 \"eventTime\": \"2018-01-02T19:17:44.4383997Z\",\
	 \"data\": {  \"key\":\"key1\",  \"label\":\"label1\",  \"etag\":\"etag1\"},\
	  \"dataVersion\": \"\", \"metadataVersion\": \"1\" },\
	  {\"id\": \"56afc886-767b-d359-d59e-0sdsd34343466b2\", \"topic\": \
	\"/SUBSCRIPTIONS/ID/RESOURCEGROUPS/rg/PROVIDERS/MICROSOFT.ContainerRegistry/test2\", \
	\"subject\": \"test2\", \"eventType\": \"Microsoft.AppConfiguration.KeyValueDeleted\",\
	 \"eventTime\": \"2020-01-02T19:17:44.4383997Z\",\
	 \"data\": {  \"key\":\"key2\",  \"label\":\"label2\",  \"etag\":\"etag2\"},\
	  \"dataVersion\": \"\", \"metadataVersion\": \"1\" }]"

deserialized_dict_events = EventGridDeserializer.deserialize_eventgrid_events(eg_storage_dict)

# to return raw json, we use the data param
for event in deserialized_dict_events:
	print(event.data)
	print(type(event.data))
```


### Deserialize CloudEvents payload

```Python
from azure.eventgrid import EventGridDeserializer

# all types of CloudEvents below produce same DeserializedEvent
cloud_custom_dict = "[{ \"id\":\"de0fd76c-4ef4-4dfb-ab3a-8f24a307e033\",\
    \"source\":\"https://egtest.dev/cloudcustomevent\",\
    \"data\":{\"team\": \"event grid squad\"},\
    \"type\":\"Azure.Sdk.Sample\",\
    \"time\":\"2020-08-07T02:06:08.11969Z\",\
    \"specversion\":\"1.0\" }]"

deserialized_dict_events = EventGridDeserializer.deserialize_cloud_events(cloud_custom_dict)

for event in deserialized_dict_events:
	# to return raw json, we use the data param
	print(event.data)
	print(type(event.data))
```

### Deserialize CloudEvents payload with bytes data

```Python
from azure.eventgrid import EventGridDeserializer

# all types of CloudEvents below produce same DeserializedEvent
cloud_custom_dict = "[{ \"id\":\"de0fd76c-4ef4-4dfb-ab3a-8f24a307e033\",\
    \"source\":\"https://egtest.dev/cloudcustomevent\",\
    \"data_base64\":\"Y2xvdWRldmVudA==\",\
    \"type\":\"Azure.Sdk.Sample\",\
    \"time\":\"2020-08-07T02:06:08.11969Z\",\
    \"specversion\":\"1.0\" }]"

deserialized_dict_events = EventGridDeserializer.deserialize_cloud_events(cloud_custom_dict)

for event in deserialized_dict_events:
	# to return raw json, we use the data param
	print(event.data)
	print(type(event.data))
```