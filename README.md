# Traditional Smart Home Interoperability Simulation

This project simulates a traditional, centralized approach to IoT interoperability for smart homes using Zigbee motion sensors and BLE door locks.

## Folder Structure
- `cloud_server/`: Flask app to simulate the cloud controller
- `zigbee_gateway/`: Script to simulate motion detection
- `ble_gateway/`: Script to simulate BLE proximity
- `ble_door_lock/`: Script to poll unlock state
- `architecture/`: PNG diagram of architecture
- `docs/`: Workflow explanation and logs

## How to Run

1. Install requirements: `pip install -r requirements.txt`
2. Run the cloud server: `python cloud_server/app.py`
3. In other terminals:
   - Simulate motion: `python zigbee_gateway/send_motion.py`
   - Simulate proximity: `python ble_gateway/send_proximity.py`
   - Run door lock poller: `python ble_door_lock/poll_server.py`

## Requirements

- Python 3.8+
- Flask
- requests

## License
MIT
