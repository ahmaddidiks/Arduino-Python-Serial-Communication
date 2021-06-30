
union {
  struct {
    int data1;
    int data2;
    int data3;
  } param;
  byte packet[6];
} data;

union {
  struct {
    int data1;
    int data2;
    int data3;
  } param;
  byte packet[6];
} dataRecv;

void setup() {
  // put your setup code here, to run once:
Serial.begin(57600);
pinMode(2, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  data.param.data1 = 1;
  data.param.data2 = 2;
  data.param.data3 = 3;

  Serial.write(data.packet, sizeof(data.packet));

  if (Serial.available()) {
    Serial.readBytes(dataRecv.packet, sizeof(dataRecv.packet));
  }

  delay(100);
}
