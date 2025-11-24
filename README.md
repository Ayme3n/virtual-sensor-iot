Demo 

Simulated Sensor: Temperature and humidity values are generated randomly and sent to ThingsBoard every 5 seconds.

Dashboard: Real-time graphs and gauges visualize the sensor data.

Downlink Command: You can send a command (e.g., toggle a fan state) to the virtual sensor and see it received instantly.

Setup Steps
1. Create a Device and copy the DEVICE_ACCESS_TOKEN


2. Simulate Sensor Data

Install MQTT library ----->  pip install paho-mqtt


Run the Python script virtual_sensor.py 

python virtual_sensor.py


The script sends temperature and humidity data every 5 seconds.

3. Create a Dashboard

In ThingsBoard, go to Dashboards → + Add new dashboard

Add widgets (Line Chart for temperature, Gauge for humidity).

Link widgets to device telemetry.

View live updates as data arrives.

4. Send a Downlink Command

Example JSON payload:

{"fan_state":"ON"}


Observe the Python script receiving and printing the command.

