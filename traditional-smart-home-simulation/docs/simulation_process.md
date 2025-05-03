# Simulation Process

## 1. Cloud Server
- Maintains internal state of last motion and proximity timestamps.
- Logic checks if both events are recent (within 10s).
- Returns unlock = true or false accordingly.

## 2. Event Triggers
- Zigbee gateway triggers motion.
- BLE gateway triggers proximity.

## 3. Polling Mechanism
- Door lock script polls every 5 seconds.
- Unlocks door if conditions met.

All communications are stateless HTTP POST/GET with JSON responses.
