Int l_sensor = 0; 
Int pir_sensor = 0; 
Int out_relay = 0; 
Void setup()
{
pinMode(A0, INPUT); 
pinMode(2, INPUT); 
pinMode(8, OUTPUT); 
Serial.begin(9600);
}
Void loop()
{
l_sensor = analogRead(A0);
pir_sensor = digitalRead(2);
out_relay = 8;
If (l_sensor < 600) {
If (pir_sensor == HIGH) {
digitalWrite(8, HIGH);
delay(7000); 
} else {
digitalWrite(8, LOW);
delay(2000); 
}
} else {
digitalWrite(8, LOW);
Serial.println(l_sensor);
Delay(500);
}
}
