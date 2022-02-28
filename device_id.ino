#include <sys/boardctl.h>

void setup() {
  uint8_t raw_id[CONFIG_BOARDCTL_UNIQUEID_SIZE];
  Serial.begin(115200);

  boardctl(BOARDIOC_UNIQUEID, (uintptr_t) raw_id);
  for (int i = 0; i < CONFIG_BOARDCTL_UNIQUEID_SIZE; i++) {
    Serial.print(raw_id[i], HEX);
  }
}

void loop() {
}
