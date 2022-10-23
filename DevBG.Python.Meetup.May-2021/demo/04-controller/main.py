import time
import multiprocessing

import paho.mqtt.client as mqtt
from queue import Queue

from monitoring import MonitoringProcess
from driver import DriverProcess


# MQTT Configuration
MQTT_HOST = "127.0.0.1"
MQTT_PORT = 1883


class State:
    SHUTDOWN = False
    ITERATION_SLEEP_SECONDS = 1
    MQTT_MESSAGES_QUEUE = Queue()

    MONITORING_QUEUE = multiprocessing.Queue()
    MONITORING_STOP = multiprocessing.Event()

    DRIVER_QUEUE = multiprocessing.Queue()
    DRIVER_STOP = multiprocessing.Event()


class MqttMessage:
    def __init__(self, message, client):
        self.message = message
        self.client = client


def log(msg):
    print(msg)


def mqtt_on_connect(client, userdata, flags, rc):
    log('Successfully connected to mosquitto server')
    client.subscribe('shutdown')
    client.subscribe('monitoring/info')


def mqtt_on_disconnect(client, userdata, rc):
    log('Successfully disconnected from mosquitto server')
    client.unsubscribe('shutdown')


def mqtt_on_message(client, userdata, message):
    payload = message.payload
    topic = message.topic

    log(f'Received payload "{payload}" to topic "{topic}"')

    State.MQTT_MESSAGES_QUEUE.put(
        MqttMessage(
            message=message,
            client=client
        )
    )


def mqtt_on_log(client, userdata, level, buff):
    # To output any error messages
    # print(level, buff)
    pass


def setup_mqtt_client():
    client = mqtt.Client(client_id='test')
    client.on_message = mqtt_on_message
    client.on_connect = mqtt_on_connect
    client.on_disconnect = mqtt_on_disconnect
    client.on_log = mqtt_on_log

    client.connect(
        host=MQTT_HOST,
        port=MQTT_PORT,
    )

    client.loop_start()

    return client


def process_pending_mqtt_messages():
    while not State.MQTT_MESSAGES_QUEUE.empty():
        message_obj = State.MQTT_MESSAGES_QUEUE.get()

        topic = message_obj.message.topic
        payload = message_obj.message.payload

        if topic == 'shutdown':
            if payload == b'true':
                State.MONITORING_STOP.set()
                State.DRIVER_STOP.set()
                State.SHUTDOWN = True

        if topic == 'monitoring/info':
            State.MONITORING_QUEUE.put(topic)


def main():
    client = setup_mqtt_client()

    log('Starting monitoring process...')
    monitoring = MonitoringProcess(
        messages_queue=State.MONITORING_QUEUE,
        stop_signal=State.MONITORING_STOP
    )
    monitoring.daemon = True
    monitoring.start()

    log('Starting driver process...')
    driver = DriverProcess(
        messages_queue=State.DRIVER_QUEUE,
        stop_signal=State.DRIVER_STOP
    )
    driver.daemon = True
    driver.start()

    while State.SHUTDOWN is False:
        log('Main loop iteration')
        time.sleep(State.ITERATION_SLEEP_SECONDS)

        # Process pending mqtt messages
        process_pending_mqtt_messages()

    print('The end')
    client.loop_stop()


if __name__ == '__main__':
    main()
