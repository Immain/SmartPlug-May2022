from datetime import timedelta
from wyze_sdk import Client
from wyze_sdk.errors import WyzeApiError

client = Client(email='Wyze_Email', password='Wyze_Password')

try:
    plug = client.plugs.info(device_mac='DeviceMac')
    print(f"power: on")
    print(f"online: {plug.is_online}")

    if plug.is_on:
        client.plugs.turn_off(device_mac=plug.mac, device_model=plug.product.model, after=timedelta(hours=3))
    else:
        client.plugs.turn_on(device_mac=plug.mac, device_model=plug.product.model)

except WyzeApiError as e:
    print(f"Got an error: {e}")

try:
    plug = client.plugs.info(device_mac='DeviceMac')
    print(f"power: off")
    print(f"online: {plug.is_online}")

    if plug.is_on:
        client.plugs.turn_off(device_mac=plug.mac, device_model=plug.product.model)


except WyzeApiError as e:
    print(f"Got an error: {e}")
