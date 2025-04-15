# PresenseNode

**Smart room presence detection using ESP32-S3, BLE beacons, and edge AI — no cloud required.**

PresenseNode is a modular system for accurate, room-specific presence detection. It leverages a mix of Bluetooth Low Energy (BLE) beacon scanning, passive thermal sensing, and optional onboard AI (face recognition or ambient motion detection) — all processed locally on ESP32-S3 microcontrollers.

## 🌐 Why PresenseNode?

Traditional motion sensors are dumb. They can’t tell **who** is present, and they shut things off if you sit still too long. PresenseNode fixes that — blending Bluetooth, ambient heat, and camera-based identity to offer smart, low-power, privacy-respecting presence detection for automation systems like:

- **Home Assistant**
- **MQTT + Node-RED**
- **Amazon Alexa Routines**

---

## 🧩 Features

- 📍 **BLE Beacon Detection** (via BlueCharm or Tile beacons)
- 🌡️ **Thermal / Ambient Motion Presence** (AMG8833 / MLX90640 support)
- 📸 **Optional Face Recognition** using ESP32-S3 Sense camera
- ⚡ **Low Power Design** (sleeps between scans, event-driven)
- 📡 **MQTT Support** for integration with any smart home platform
- 🗣️ **Alexa / Google Assistant Trigger Support** via virtual switches
- 🔐 **Fully Local / Offline Operation**

---

## 🔧 Hardware

| Device                 | Function                          |
|------------------------|-----------------------------------|
| XIAO ESP32-S3 Sense    | Camera-based presence recognition |
| XIAO ESP32-C6          | BLE beacon scanner node           |
| BlueCharm Beacon       | Mobile tag carried by individual  |
| Optional: AMG8833      | Passive thermal presence sensor   |

---

## 📁 Folder Structure

