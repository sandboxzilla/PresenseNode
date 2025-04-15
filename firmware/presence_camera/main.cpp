#include <Arduino.h>
#include "esp_camera.h"

void setup() {
  Serial.begin(115200);
  Serial.println("ESP32-S3 Camera Booting...");
  // Camera init code would go here
}

void loop() {
  // Placeholder: trigger face detection
  delay(1000);
  Serial.println("Checking for face...");
}
