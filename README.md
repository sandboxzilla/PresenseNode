# PresenseNode

**Smart room presence detection using ESP32-S3 and onboard face recognition — no cloud required.**

PresenseNode is a modular system for accurate, room-specific presence detection. It leverages a mix of onboard face detection and recognition using ESP32-S3 Sense — all processed locally on ESP32-S3 microcontrollers.

## 🌐 Why PresenseNode?

Traditional motion sensors are dumb. They can’t tell **who** is present, and they shut things off if you sit still too long. PresenseNode fixes that — blending Bluetooth, ambient heat, and camera-based identity to offer smart, low-power, privacy-respecting presence detection for automation systems like:

- **Home Assistant**
- **MQTT + Node-RED**
- **Amazon Alexa Routines**

## 🧩 Features

- 📍 **BLE Beacon Detection** (via BlueCharm or Tile beacons)
- 🌡️ **Thermal / Ambient Motion Presence** (AMG8833 / MLX90640 support)
- 📸 **Optional Face Recognition** using ESP32-S3 Sense camera
- ⚡ **Low Power Design** (sleeps between scans, event-driven)
- 📡 **MQTT Support** for integration with any smart home platform
- 🗣️ **Alexa / Google Assistant Trigger Support** via virtual switches
- 🔐 **Fully Local / Offline Operation**

## 🔧 Hardware

| Device                 | Function                          |
|------------------------|-----------------------------------|
| XIAO ESP32-S3 Sense    | Camera-based presence recognition |

## 📁 Folder Structure

PresenseNode/
├── firmware/           # ESP32 firmware (Arduino/IDF)
│   │   ├── presence_camera/
│   └── thermal_node/
├── scripts/            # Python utilities (embedding, config)
│   └── embed_faces.py
├── models/             # Trained face embedding data
│   └── face_embeddings.json
├── data/               # Captured image or thermal logs
├── README.md
└── requirements.txt

## 🚀 Setup Guide

### 1. Clone the Repo

git clone https://github.com/sandboxzilla/PresenseNode.git
cd PresenseNode
python3 -m venv venv
source venv/bin/activate

### 2. Install Python Tools

pip install -r requirements.txt

### 3. Train Face Recognition Model (Optional)

Place labeled images in:

FaceRecognition/
├── PersonA/
├── PersonB/
└── PersonC/

Run:

python scripts/embed_faces.py

This creates `face_embeddings.json` for on-device matching.

### 4. Flash ESP32-S3

- Open `firmware/presence_camera/` in PlatformIO or Arduino IDE.
- Configure Wi-Fi, MQTT broker, beacon UUIDs, and flash.

## 🧠 Local Recognition Logic

| Sensor            | Detected | Action                             |
|------------------|----------|------------------------------------|
| BLE Beacon        | Yes      | Publish `presence/room = true`     |
| Thermal Spike     | Yes      | Confirm room occupancy             |
| Face Match (S3)   | “Inci”   | Trigger `personC/room = active`       |
| Timeout (no input)| 10 min   | Publish `presence/room = false`    |

## 📡 Integration Options

- Home Assistant via MQTT Binary Sensors
- Alexa routines via virtual device bridging
- Dashboard presence logs via InfluxDB/Grafana

## 🛠️ Future Enhancements

- [ ] Adaptive scan rate based on movement
- [ ] BLE signal triangulation for zone precision
- [ ] Enclosure CADs for discreet mounting
- [ ] OTA update support
- [ ] Wake-word based override triggers

## 📜 License

MIT License — use, fork, contribute, automate your home.

## 🙌 Credits

Developed by [@sandboxzilla](https://github.com/sandboxzilla).  
Built with ❤️ for Cecilia, Inci, and the robot future.
