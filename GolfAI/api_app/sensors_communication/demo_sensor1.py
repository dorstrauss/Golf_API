import time

from paho.mqtt import client
import json

mqtt_broker = "mqtt.eclipseprojects.io"  # the address of our broker
receiver = client.Client("demo_sensor")  # creating the subscriber client
receiver.connect(mqtt_broker)

# swing data example
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.3748672,"Y":-1.05,"Z":-1.795133,"TIME": "2022-12-19 07:13:02.1+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.3749063,"Y":-1.049885,"Z":-1.79521,"TIME": "2022-12-19 07:13:02.12+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.3748696,"Y":-1.049886,"Z":-1.795247,"TIME": "2022-12-19 07:13:02.14+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.3748147,"Y":-1.049886,"Z":-1.795301,"TIME": "2022-12-19 07:13:02.16+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.3951789,"Y":-1.049697,"Z":-1.775126,"TIME": "2022-12-19 07:13:02.18+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.3951091,"Y":-1.049621,"Z":-1.775271,"TIME": "2022-12-19 07:13:02.2+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.3949691,"Y":-1.049623,"Z":-1.77541,"TIME": "2022-12-19 07:13:02.22+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.3947951,"Y":-1.049626,"Z":-1.77558,"TIME": "2022-12-19 07:13:02.24+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.3945882,"Y":-1.049629,"Z":-1.775784,"TIME": "2022-12-19 07:13:02.26+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'start', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.3943482,"Y":-1.049633,"Z":-1.776019,"TIME": "2022-12-19 07:13:02.28+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.3940759,"Y":-1.049638,"Z":-1.776288,"TIME": "2022-12-19 07:13:02.3+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.3940759,"Y":-1.049638,"Z":-1.776288,"TIME": "2022-12-19 07:13:02.316959+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.3940759,"Y":-1.049638,"Z":-1.776288,"TIME": "2022-12-19 07:13:02.316959+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.3937706,"Y":-1.049642,"Z":-1.776588,"TIME": "2022-12-19 07:13:02.32+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.3934335,"Y":-1.049648,"Z":-1.77692,"TIME": "2022-12-19 07:13:02.34+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.3930633,"Y":-1.049654,"Z":-1.777284,"TIME": "2022-12-19 07:13:02.36+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.3926618,"Y":-1.049661,"Z":-1.777678,"TIME": "2022-12-19 07:13:02.38+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.4658371,"Y":-1.048497,"Z":-1.705668,"TIME": "2022-12-19 07:13:02.4+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.4657761,"Y":-1.047524,"Z":-1.7067,"TIME": "2022-12-19 07:13:02.42+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.4651652,"Y":-1.047549,"Z":-1.707285,"TIME": "2022-12-19 07:13:02.44+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.4644689,"Y":-1.047579,"Z":-1.707953,"TIME": "2022-12-19 07:13:02.46+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.4636869,"Y":-1.047612,"Z":-1.708701,"TIME": "2022-12-19 07:13:02.48+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.4628212,"Y":-1.047648,"Z":-1.709532,"TIME": "2022-12-19 07:13:02.5+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.4618714,"Y":-1.047688,"Z":-1.710442,"TIME": "2022-12-19 07:13:02.52+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.4608383,"Y":-1.047731,"Z":-1.711433,"TIME": "2022-12-19 07:13:02.54+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.4608383,"Y":-1.047731,"Z":-1.711433,"TIME": "2022-12-19 07:13:02.557387+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.4608383,"Y":-1.047731,"Z":-1.711433,"TIME": "2022-12-19 07:13:02.557387+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.493313,"Y":-1.046413,"Z":-1.680276,"TIME": "2022-12-19 07:13:02.56+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.492173,"Y":-1.046285,"Z":-1.681544,"TIME": "2022-12-19 07:13:02.58+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.4908393,"Y":-1.046354,"Z":-1.682809,"TIME": "2022-12-19 07:13:02.6+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.489401,"Y":-1.046426,"Z":-1.684174,"TIME": "2022-12-19 07:13:02.62+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.4878589,"Y":-1.046504,"Z":-1.685637,"TIME": "2022-12-19 07:13:02.64+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.4862155,"Y":-1.046586,"Z":-1.6872,"TIME": "2022-12-19 07:13:02.66+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.5874951,"Y":-1.041566,"Z":-1.590938,"TIME": "2022-12-19 07:13:02.68+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.5863414,"Y":-1.039894,"Z":-1.593765,"TIME": "2022-12-19 07:13:02.7+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.584214,"Y":-1.040072,"Z":-1.595716,"TIME": "2022-12-19 07:13:02.72+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.581911,"Y":-1.040262,"Z":-1.597828,"TIME": "2022-12-19 07:13:02.74+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.5794349,"Y":-1.040465,"Z":-1.600101,"TIME": "2022-12-19 07:13:02.76+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.5767882,"Y":-1.04068,"Z":-1.602533,"TIME": "2022-12-19 07:13:02.78+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.5767882,"Y":-1.04068,"Z":-1.602533,"TIME": "2022-12-19 07:13:02.790089+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.5767882,"Y":-1.04068,"Z":-1.602533,"TIME": "2022-12-19 07:13:02.790089+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.6451652,"Y":-1.035163,"Z":-1.539671,"TIME": "2022-12-19 07:13:02.8+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.6424388,"Y":-1.034668,"Z":-1.542894,"TIME": "2022-12-19 07:13:02.82+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.6391541,"Y":-1.035002,"Z":-1.545844,"TIME": "2022-12-19 07:13:02.84+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.6356534,"Y":-1.035355,"Z":-1.548991,"TIME": "2022-12-19 07:13:02.86+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.6319399,"Y":-1.035726,"Z":-1.552335,"TIME": "2022-12-19 07:13:02.88+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.7456716,"Y":-1.024468,"Z":-1.44986,"TIME": "2022-12-19 07:13:02.9+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.7422497,"Y":-1.022844,"Z":-1.454906,"TIME": "2022-12-19 07:13:02.92+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.737673,"Y":-1.023456,"Z":-1.458872,"TIME": "2022-12-19 07:13:02.94+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.7328055,"Y":-1.024101,"Z":-1.463095,"TIME": "2022-12-19 07:13:02.96+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.7276522,"Y":-1.024773,"Z":-1.467575,"TIME": "2022-12-19 07:13:02.98+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.7222174,"Y":-1.025475,"Z":-1.47231,"TIME": "2022-12-19 07:13:03.0+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.7165051,"Y":-1.026201,"Z":-1.477295,"TIME": "2022-12-19 07:13:03.02+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.8005418,"Y":-1.015588,"Z":-1.40387,"TIME": "2022-12-19 07:13:03.04+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.7945921,"Y":-1.015391,"Z":-1.410019,"TIME": "2022-12-19 07:13:03.06+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.7878711,"Y":-1.016395,"Z":-1.415734,"TIME": "2022-12-19 07:13:03.08+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.7808251,"Y":-1.017437,"Z":-1.421741,"TIME": "2022-12-19 07:13:03.1+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.7734585,"Y":-1.018504,"Z":-1.428037,"TIME": "2022-12-19 07:13:03.12+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.9112924,"Y":-0.9986424,"Z":-1.310066,"TIME": "2022-12-19 07:13:03.14+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.904133,"Y":-0.99708,"Z":-1.318788,"TIME": "2022-12-19 07:13:03.16+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.8954924,"Y":-0.9986566,"Z":-1.325852,"TIME": "2022-12-19 07:13:03.18+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.8864456,"Y":-1.000283,"Z":-1.333272,"TIME": "2022-12-19 07:13:03.2+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.8770006,"Y":-1.001955,"Z":-1.341045,"TIME": "2022-12-19 07:13:03.22+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.8671659,"Y":-1.003669,"Z":-1.349167,"TIME": "2022-12-19 07:13:03.24+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.8671659,"Y":-1.003669,"Z":-1.349167,"TIME": "2022-12-19 07:13:03.253795+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.8671659,"Y":-1.003669,"Z":-1.349167,"TIME": "2022-12-19 07:13:03.253795+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.9412324,"Y":-0.9908695,"Z":-1.287897,"TIME": "2022-12-19 07:13:03.26+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.9307747,"Y":-0.9920927,"Z":-1.297135,"TIME": "2022-12-19 07:13:03.28+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.9195977,"Y":-0.9942145,"Z":-1.306189,"TIME": "2022-12-19 07:13:03.3+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.9080017,"Y":-0.9963776,"Z":-1.315622,"TIME": "2022-12-19 07:13:03.32+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.8959963,"Y":-0.9985753,"Z":-1.325429,"TIME": "2022-12-19 07:13:03.34+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.8959963,"Y":-0.9985753,"Z":-1.325429,"TIME": "2022-12-19 07:13:03.353485+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.8959963,"Y":-0.9985753,"Z":-1.325429,"TIME": "2022-12-19 07:13:03.353485+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.023587,"Y":-0.9754366,"Z":-1.220977,"TIME": "2022-12-19 07:13:03.36+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.011312,"Y":-0.9757387,"Z":-1.232951,"TIME": "2022-12-19 07:13:03.38+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.9977499,"Y":-0.9786245,"Z":-1.243625,"TIME": "2022-12-19 07:13:03.4+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.9837136,"Y":-0.9815611,"Z":-1.254728,"TIME": "2022-12-19 07:13:03.42+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.9692146,"Y":-0.9845286,"Z":-1.266256,"TIME": "2022-12-19 07:13:03.44+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.9542666,"Y":-0.9875284,"Z":-1.278206,"TIME": "2022-12-19 07:13:03.46+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-0.9388829,"Y":-0.9905465,"Z":-1.290572,"TIME": "2022-12-19 07:13:03.48+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.136914,"Y":-0.952132,"Z":-1.130956,"TIME": "2022-12-19 07:13:03.5+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.121944,"Y":-0.9502615,"Z":-1.147795,"TIME": "2022-12-19 07:13:03.52+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.104695,"Y":-0.9544629,"Z":-1.160843,"TIME": "2022-12-19 07:13:03.54+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.086897,"Y":-0.9587137,"Z":-1.17439,"TIME": "2022-12-19 07:13:03.56+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.068567,"Y":-0.9629982,"Z":-1.188436,"TIME": "2022-12-19 07:13:03.58+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.204341,"Y":-0.9315868,"Z":-1.084073,"TIME": "2022-12-19 07:13:03.6+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.18536,"Y":-0.9341256,"Z":-1.100516,"TIME": "2022-12-19 07:13:03.62+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.165049,"Y":-0.9394221,"Z":-1.115531,"TIME": "2022-12-19 07:13:03.64+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.144151,"Y":-0.9447525,"Z":-1.131097,"TIME": "2022-12-19 07:13:03.66+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.122686,"Y":-0.9501038,"Z":-1.147212,"TIME": "2022-12-19 07:13:03.68+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.100672,"Y":-0.9554563,"Z":-1.163871,"TIME": "2022-12-19 07:13:03.7+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.07813,"Y":-0.9608009,"Z":-1.181071,"TIME": "2022-12-19 07:13:03.72+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.255862,"Y":-0.9191934,"Z":-1.044945,"TIME": "2022-12-19 07:13:03.74+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.232978,"Y":-0.921302,"Z":-1.065722,"TIME": "2022-12-19 07:13:03.76+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.208295,"Y":-0.9280424,"Z":-1.083663,"TIME": "2022-12-19 07:13:03.78+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.183007,"Y":-0.9347776,"Z":-1.102215,"TIME": "2022-12-19 07:13:03.8+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.157137,"Y":-0.9414878,"Z":-1.121376,"TIME": "2022-12-19 07:13:03.82+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.379528,"Y":-0.8845438,"Z":-0.9559293,"TIME": "2022-12-19 07:13:03.84+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.353483,"Y":-0.8860862,"Z":-0.9804317,"TIME": "2022-12-19 07:13:03.86+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.325176,"Y":-0.8947152,"Z":-1.000111,"TIME": "2022-12-19 07:13:03.88+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.296179,"Y":-0.9033342,"Z":-1.020487,"TIME": "2022-12-19 07:13:03.9+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.266522,"Y":-0.9119199,"Z":-1.041559,"TIME": "2022-12-19 07:13:03.92+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.236232,"Y":-0.920446,"Z":-1.063324,"TIME": "2022-12-19 07:13:03.94+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.236232,"Y":-0.920446,"Z":-1.063324,"TIME": "2022-12-19 07:13:03.956031+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.236232,"Y":-0.920446,"Z":-1.063324,"TIME": "2022-12-19 07:13:03.956031+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.417373,"Y":-0.8701136,"Z":-0.9325143,"TIME": "2022-12-19 07:13:03.96+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.386274,"Y":-0.8758648,"Z":-0.9578621,"TIME": "2022-12-19 07:13:03.98+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.353502,"Y":-0.8861187,"Z":-0.9803805,"TIME": "2022-12-19 07:13:04.0+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.320036,"Y":-0.8962994,"Z":-1.003665,"TIME": "2022-12-19 07:13:04.02+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.285908,"Y":-0.9063768,"Z":-1.027716,"TIME": "2022-12-19 07:13:04.04+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.285908,"Y":-0.9063768,"Z":-1.027716,"TIME": "2022-12-19 07:13:04.053339+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.285908,"Y":-0.9063768,"Z":-1.027716,"TIME": "2022-12-19 07:13:04.053339+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.533223,"Y":-0.8343704,"Z":-0.8524057,"TIME": "2022-12-19 07:13:04.06+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.49861,"Y":-0.8386449,"Z":-0.8827452,"TIME": "2022-12-19 07:13:04.08+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.461717,"Y":-0.8512445,"Z":-0.9070387,"TIME": "2022-12-19 07:13:04.1+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.424055,"Y":-0.8637488,"Z":-0.9321968,"TIME": "2022-12-19 07:13:04.12+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.38566,"Y":-0.8761156,"Z":-0.9582246,"TIME": "2022-12-19 07:13:04.14+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.346571,"Y":-0.8883099,"Z":-0.9851198,"TIME": "2022-12-19 07:13:04.16+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.306825,"Y":-0.9002951,"Z":-1.01288,"TIME": "2022-12-19 07:13:04.18+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.618752,"Y":-0.8077267,"Z":-0.7935206,"TIME": "2022-12-19 07:13:04.2+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.578881,"Y":-0.8100966,"Z":-0.8310232,"TIME": "2022-12-19 07:13:04.22+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.53616,"Y":-0.8255295,"Z":-0.8583115,"TIME": "2022-12-19 07:13:04.24+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.49263,"Y":-0.8407835,"Z":-0.8865877,"TIME": "2022-12-19 07:13:04.26+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.448333,"Y":-0.855805,"Z":-0.9158621,"TIME": "2022-12-19 07:13:04.28+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.757593,"Y":-0.7525086,"Z":-0.7098972,"TIME": "2022-12-19 07:13:04.3+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.712466,"Y":-0.7589155,"Z":-0.7486193,"TIME": "2022-12-19 07:13:04.32+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.665,"Y":-0.777636,"Z":-0.7773648,"TIME": "2022-12-19 07:13:04.34+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.616627,"Y":-0.7961407,"Z":-0.8072323,"TIME": "2022-12-19 07:13:04.36+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.567398,"Y":-0.8143665,"Z":-0.8382362,"TIME": "2022-12-19 07:13:04.38+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.517361,"Y":-0.8322595,"Z":-0.8703811,"TIME": "2022-12-19 07:13:04.4+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.466567,"Y":-0.8497657,"Z":-0.9036676,"TIME": "2022-12-19 07:13:04.42+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.779667,"Y":-0.7436339,"Z":-0.6966982,"TIME": "2022-12-19 07:13:04.44+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.727939,"Y":-0.7527747,"Z":-0.7392873,"TIME": "2022-12-19 07:13:04.46+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.673945,"Y":-0.7742358,"Z":-0.771821,"TIME": "2022-12-19 07:13:04.48+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.619062,"Y":-0.7953086,"Z":-0.8056295,"TIME": "2022-12-19 07:13:04.5+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.619062,"Y":-0.7953086,"Z":-0.8056295,"TIME": "2022-12-19 07:13:04.519472+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.619062,"Y":-0.7953086,"Z":-0.8056295,"TIME": "2022-12-19 07:13:04.519472+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.890178,"Y":-0.6927663,"Z":-0.6370552,"TIME": "2022-12-19 07:13:04.52+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.833652,"Y":-0.7087111,"Z":-0.6776374,"TIME": "2022-12-19 07:13:04.54+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.775448,"Y":-0.7333524,"Z":-0.7112009,"TIME": "2022-12-19 07:13:04.56+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.716274,"Y":-0.7575455,"Z":-0.7461804,"TIME": "2022-12-19 07:13:04.58+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.656193,"Y":-0.7812175,"Z":-0.7825905,"TIME": "2022-12-19 07:13:04.6+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.595271,"Y":-0.8042921,"Z":-0.8204387,"TIME": "2022-12-19 07:13:04.62+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.533574,"Y":-0.8267009,"Z":-0.8597261,"TIME": "2022-12-19 07:13:04.64+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.533574,"Y":-0.8267009,"Z":-0.8597261,"TIME": "2022-12-19 07:13:04.65388+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.533574,"Y":-0.8267009,"Z":-0.8597261,"TIME": "2022-12-19 07:13:04.65388+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.992303,"Y":-0.6633134,"Z":-0.5643835,"TIME": "2022-12-19 07:13:04.66+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.929357,"Y":-0.6665217,"Z":-0.6241222,"TIME": "2022-12-19 07:13:04.68+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.864275,"Y":-0.6955245,"Z":-0.6602002,"TIME": "2022-12-19 07:13:04.7+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.798156,"Y":-0.7239638,"Z":-0.6978825,"TIME": "2022-12-19 07:13:04.72+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.731073,"Y":-0.7517042,"Z":-0.7372226,"TIME": "2022-12-19 07:13:04.74+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.731073,"Y":-0.7517042,"Z":-0.7372226,"TIME": "2022-12-19 07:13:04.755347+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.731073,"Y":-0.7517042,"Z":-0.7372226,"TIME": "2022-12-19 07:13:04.755347+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.143923,"Y":-0.5839663,"Z":-0.4921108,"TIME": "2022-12-19 07:13:04.76+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.07444,"Y":-0.5981399,"Z":-0.5474213,"TIME": "2022-12-19 07:13:04.78+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.003897,"Y":-0.6320606,"Z":-0.5840439,"TIME": "2022-12-19 07:13:04.8+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.932185,"Y":-0.6653237,"Z":-0.6224927,"TIME": "2022-12-19 07:13:04.82+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.859385,"Y":-0.6977955,"Z":-0.66282,"TIME": "2022-12-19 07:13:04.84+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.785582,"Y":-0.7293792,"Z":-0.7050412,"TIME": "2022-12-19 07:13:04.86+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.710862,"Y":-0.7599748,"Z":-0.7491644,"TIME": "2022-12-19 07:13:04.88+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.191899,"Y":-0.5669144,"Z":-0.4611872,"TIME": "2022-12-19 07:13:04.9+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.11443,"Y":-0.5785217,"Z":-0.5270489,"TIME": "2022-12-19 07:13:04.92+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.036373,"Y":-0.6167285,"Z":-0.5669006,"TIME": "2022-12-19 07:13:04.94+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.957123,"Y":-0.654044,"Z":-0.6088318,"TIME": "2022-12-19 07:13:04.96+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.87678,"Y":-0.6903028,"Z":-0.6529189,"TIME": "2022-12-19 07:13:04.98+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.305185,"Y":-0.5005468,"Z":-0.4142686,"TIME": "2022-12-19 07:13:05.0+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.221511,"Y":-0.5237297,"Z":-0.4747595,"TIME": "2022-12-19 07:13:05.02+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.137764,"Y":-0.5668808,"Z":-0.5153568,"TIME": "2022-12-19 07:13:05.04+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.052714,"Y":-0.6089858,"Z":-0.5583017,"TIME": "2022-12-19 07:13:05.06+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.966466,"Y":-0.6498713,"Z":-0.6036639,"TIME": "2022-12-19 07:13:05.08+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.879131,"Y":-0.6894089,"Z":-0.6514617,"TIME": "2022-12-19 07:13:05.1+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.790826,"Y":-0.7274699,"Z":-0.701705,"TIME": "2022-12-19 07:13:05.12+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.408442,"Y":-0.4672207,"Z":-0.3443379,"TIME": "2022-12-19 07:13:05.14+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.314546,"Y":-0.474013,"Z":-0.4314398,"TIME": "2022-12-19 07:13:05.16+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.223474,"Y":-0.5228392,"Z":-0.4736873,"TIME": "2022-12-19 07:13:05.18+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.131,"Y":-0.5704809,"Z":-0.5185211,"TIME": "2022-12-19 07:13:05.2+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.131,"Y":-0.5704809,"Z":-0.5185211,"TIME": "2022-12-19 07:13:05.218954+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.131,"Y":-0.5704809,"Z":-0.5185211,"TIME": "2022-12-19 07:13:05.218954+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.608432,"Y":-0.3290424,"Z":-0.2825249,"TIME": "2022-12-19 07:13:05.22+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.510397,"Y":-0.3618695,"Z":-0.3477331,"TIME": "2022-12-19 07:13:05.24+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.414828,"Y":-0.4177616,"Z":-0.3874105,"TIME": "2022-12-19 07:13:05.26+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.317598,"Y":-0.4723729,"Z":-0.4300309,"TIME": "2022-12-19 07:13:05.28+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.218823,"Y":-0.5254625,"Z":-0.475714,"TIME": "2022-12-19 07:13:05.3+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.118641,"Y":-0.5768661,"Z":-0.5244942,"TIME": "2022-12-19 07:13:05.32+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.017194,"Y":-0.6264073,"Z":-0.5763981,"TIME": "2022-12-19 07:13:05.34+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.017194,"Y":-0.6264073,"Z":-0.5763981,"TIME": "2022-12-19 07:13:05.354507+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.017194,"Y":-0.6264073,"Z":-0.5763981,"TIME": "2022-12-19 07:13:05.354507+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.676102,"Y":-0.311763,"Z":-0.2321352,"TIME": "2022-12-19 07:13:05.36+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.565302,"Y":-0.3290368,"Z":-0.3256619,"TIME": "2022-12-19 07:13:05.38+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.461891,"Y":-0.390705,"Z":-0.3674073,"TIME": "2022-12-19 07:13:05.4+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.35674,"Y":-0.4508826,"Z":-0.4123792,"TIME": "2022-12-19 07:13:05.42+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.249971,"Y":-0.5091944,"Z":-0.4608361,"TIME": "2022-12-19 07:13:05.44+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.249971,"Y":-0.5091944,"Z":-0.4608361,"TIME": "2022-12-19 07:13:05.453235+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.249971,"Y":-0.5091944,"Z":-0.4608361,"TIME": "2022-12-19 07:13:05.453235+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.920987,"Y":-0.1503601,"Z":-0.1486527,"TIME": "2022-12-19 07:13:05.46+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.801456,"Y":-0.1778932,"Z":-0.2406507,"TIME": "2022-12-19 07:13:05.48+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.693429,"Y":-0.2486941,"Z":-0.2778763,"TIME": "2022-12-19 07:13:05.5+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.583309,"Y":-0.3180299,"Z":-0.318661,"TIME": "2022-12-19 07:13:05.52+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.4712,"Y":-0.3854818,"Z":-0.3633184,"TIME": "2022-12-19 07:13:05.54+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.357268,"Y":-0.4508257,"Z":-0.4119079,"TIME": "2022-12-19 07:13:05.56+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.241691,"Y":-0.5138371,"Z":-0.4644735,"TIME": "2022-12-19 07:13:05.58+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-3.037017,"Y":-0.09016639,"Z":-0.09281588,"TIME": "2022-12-19 07:13:05.6+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.902261,"Y":-0.1093352,"Z":-0.2084059,"TIME": "2022-12-19 07:13:05.62+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.78705,"Y":-0.187575,"Z":-0.2453742,"TIME": "2022-12-19 07:13:05.64+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.66958,"Y":-0.2642337,"Z":-0.2861884,"TIME": "2022-12-19 07:13:05.66+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.549918,"Y":-0.3387083,"Z":-0.3313742,"TIME": "2022-12-19 07:13:05.68+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-3.181516,"Y":0.04642427,"Z":-0.08490729,"TIME": "2022-12-19 07:13:05.7+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-3.04787,"Y":-0.004958708,"Z":-0.1671727,"TIME": "2022-12-19 07:13:05.72+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.927588,"Y":-0.09142053,"Z":-0.2009933,"TIME": "2022-12-19 07:13:05.74+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.804694,"Y":-0.1760097,"Z":-0.2392972,"TIME": "2022-12-19 07:13:05.76+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.679313,"Y":-0.2582681,"Z":-0.2824206,"TIME": "2022-12-19 07:13:05.78+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.551649,"Y":-0.3379076,"Z":-0.3304448,"TIME": "2022-12-19 07:13:05.8+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.421927,"Y":-0.4146434,"Z":-0.3834313,"TIME": "2022-12-19 07:13:05.82+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-3.28571,"Y":0.08415294,"Z":-0.01844096,"TIME": "2022-12-19 07:13:05.84+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-3.128864,"Y":0.05495674,"Z":-0.1460916,"TIME": "2022-12-19 07:13:05.86+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-3.001858,"Y":-0.03863689,"Z":-0.179507,"TIME": "2022-12-19 07:13:05.88+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.872121,"Y":-0.1303663,"Z":-0.2175132,"TIME": "2022-12-19 07:13:05.9+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.739674,"Y":-0.2194458,"Z":-0.2608818,"TIME": "2022-12-19 07:13:05.92+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-3.39406,"Y":0.2114433,"Z":-0.0373832,"TIME": "2022-12-19 07:13:05.94+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-3.244684,"Y":0.1448299,"Z":-0.1201462,"TIME": "2022-12-19 07:13:05.96+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-3.112897,"Y":0.04320699,"Z":-0.1503108,"TIME": "2022-12-19 07:13:05.98+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.977961,"Y":-0.05614056,"Z":-0.1858987,"TIME": "2022-12-19 07:13:06.0+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.840008,"Y":-0.1526498,"Z":-0.2273422,"TIME": "2022-12-19 07:13:06.02+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.699292,"Y":-0.2459664,"Z":-0.274741,"TIME": "2022-12-19 07:13:06.04+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.699292,"Y":-0.2459664,"Z":-0.274741,"TIME": "2022-12-19 07:13:06.053476+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.699292,"Y":-0.2459664,"Z":-0.274741,"TIME": "2022-12-19 07:13:06.053476+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-3.442031,"Y":0.2353781,"Z":-0.01334596,"TIME": "2022-12-19 07:13:06.06+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-3.279398,"Y":0.1720627,"Z":-0.1126645,"TIME": "2022-12-19 07:13:06.08+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-3.141048,"Y":0.06429032,"Z":-0.1432426,"TIME": "2022-12-19 07:13:06.1+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.999403,"Y":-0.04095866,"Z":-0.1796409,"TIME": "2022-12-19 07:13:06.12+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.854565,"Y":-0.1429706,"Z":-0.2224633,"TIME": "2022-12-19 07:13:06.14+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.854565,"Y":-0.1429706,"Z":-0.2224633,"TIME": "2022-12-19 07:13:06.152353+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.854565,"Y":-0.1429706,"Z":-0.2224633,"TIME": "2022-12-19 07:13:06.152353+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-3.474742,"Y":0.2844609,"Z":-0.02971816,"TIME": "2022-12-19 07:13:06.16+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-3.314488,"Y":0.2002836,"Z":-0.1057956,"TIME": "2022-12-19 07:13:06.18+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-3.170402,"Y":0.08652951,"Z":-0.1361294,"TIME": "2022-12-19 07:13:06.2+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-3.022753,"Y":-0.02424642,"Z":-0.1730026,"TIME": "2022-12-19 07:13:06.22+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.871736,"Y":-0.1314259,"Z":-0.2168398,"TIME": "2022-12-19 07:13:06.24+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.717677,"Y":-0.2345844,"Z":-0.2677389,"TIME": "2022-12-19 07:13:06.26+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.560931,"Y":-0.3333041,"Z":-0.3257657,"TIME": "2022-12-19 07:13:06.28+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-3.484549,"Y":0.2328513,"Z":0.03169847,"TIME": "2022-12-19 07:13:06.3+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-3.294111,"Y":0.1828927,"Z":-0.108784,"TIME": "2022-12-19 07:13:06.32+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-3.143424,"Y":0.065603,"Z":-0.1421793,"TIME": "2022-12-19 07:13:06.34+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.989328,"Y":-0.04872666,"Z":-0.1819448,"TIME": "2022-12-19 07:13:06.36+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.831822,"Y":-0.1589746,"Z":-0.2292038,"TIME": "2022-12-19 07:13:06.38+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-3.52505,"Y":0.3148276,"Z":-0.009777188,"TIME": "2022-12-19 07:13:06.4+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-3.34848,"Y":0.227419,"Z":-0.09894017,"TIME": "2022-12-19 07:13:06.42+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-3.19347,"Y":0.1038933,"Z":-0.1304237,"TIME": "2022-12-19 07:13:06.44+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-3.034612,"Y":-0.01605544,"Z":-0.1693338,"TIME": "2022-12-19 07:13:06.46+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.872113,"Y":-0.1316448,"Z":-0.2162436,"TIME": "2022-12-19 07:13:06.48+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.706374,"Y":-0.2423834,"Z":-0.2712411,"TIME": "2022-12-19 07:13:06.5+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.706374,"Y":-0.2423834,"Z":-0.2712411,"TIME": "2022-12-19 07:13:06.519768+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.706374,"Y":-0.2423834,"Z":-0.2712411,"TIME": "2022-12-19 07:13:06.519768+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.537832,"Y":-0.3477951,"Z":-0.334373,"TIME": "2022-12-19 07:13:06.52+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.366949,"Y":-0.4474079,"Z":-0.4056446,"TIME": "2022-12-19 07:13:06.54+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.194216,"Y":-0.5407671,"Z":-0.4850175,"TIME": "2022-12-19 07:13:06.56+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.020149,"Y":-0.6274439,"Z":-0.5724064,"TIME": "2022-12-19 07:13:06.58+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.845288,"Y":-0.7070329,"Z":-0.6676803,"TIME": "2022-12-19 07:13:06.6+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.845288,"Y":-0.7070329,"Z":-0.6676803,"TIME": "2022-12-19 07:13:06.617922+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-1.845288,"Y":-0.7070329,"Z":-0.6676803,"TIME": "2022-12-19 07:13:06.617922+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-3.438943,"Y":-0.0126884,"Z":0.2316334,"TIME": "2022-12-19 07:13:06.62+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-3.16441,"Y":0.07576862,"Z":-0.131359,"TIME": "2022-12-19 07:13:06.64+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-3.006826,"Y":-0.03613874,"Z":-0.1770346,"TIME": "2022-12-19 07:13:06.66+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.847661,"Y":-0.1482691,"Z":-0.2240724,"TIME": "2022-12-19 07:13:06.68+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.685377,"Y":-0.255749,"Z":-0.2788749,"TIME": "2022-12-19 07:13:06.7+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.520393,"Y":-0.3581353,"Z":-0.3414737,"TIME": "2022-12-19 07:13:06.72+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.353145,"Y":-0.4549788,"Z":-0.4118765,"TIME": "2022-12-19 07:13:06.74+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.353145,"Y":-0.4549788,"Z":-0.4118765,"TIME": "2022-12-19 07:13:06.758388+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-2.353145,"Y":-0.4549788,"Z":-0.4118765,"TIME": "2022-12-19 07:13:06.758388+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-3.552251,"Y":0.217571,"Z":0.1146817,"TIME": "2022-12-19 07:13:06.76+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-3.325434,"Y":0.2067986,"Z":-0.1013635,"TIME": "2022-12-19 07:13:06.78+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-3.169865,"Y":0.08565994,"Z":-0.1357967,"TIME": "2022-12-19 07:13:06.8+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01)
print("published:" + json_data)
time.sleep(0.01)
position_data = {'NOTE':'end', 'SENSOR_ID':'1238', 'SWING_ID':'1', "X":-3.011177,"Y":-0.03312904,"Z":-0.1756931,"TIME": "2022-12-19 07:13:06.82+02:00"}
json_data = json.dumps(position_data, indent=4)
receiver.publish("POSITION", json_data, qos=0)
receiver.loop()  # ensure the message will be delivered
time.sleep(0.01) 
print("published:" + json_data)
time.sleep(0.01)
    

