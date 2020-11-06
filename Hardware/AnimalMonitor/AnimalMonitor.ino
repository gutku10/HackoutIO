#include <ESP8266WiFi.h>
#include <FirebaseArduino.h>
#include<Wire.h>
#include "DHT.h"
#include "MAX30100_PulseOximeter.h"
#include <TinyGPS++.h>


//GPS

const char *gpsStream =
  "$GPRMC,045103.000,A,3014.1984,N,09749.2872,W,0.67,161.46,030913,,,A*7C\r\n"
  "$GPGGA,045104.000,3014.1985,N,09749.2873,W,1,09,1.2,211.6,M,-22.5,M,,0000*62\r\n"
  "$GPRMC,045200.000,A,3014.3820,N,09748.9514,W,36.88,65.02,030913,,,A*77\r\n"
  "$GPGGA,045201.000,3014.3864,N,09748.9411,W,1,10,1.2,200.8,M,-22.5,M,,0000*6C\r\n"
  "$GPRMC,045251.000,A,3014.4275,N,09749.0626,W,0.51,217.94,030913,,,A*7D\r\n"
  "$GPGGA,045252.000,3014.4273,N,09749.0628,W,1,09,1.3,206.9,M,-22.5,M,,0000*6F\r\n";

TinyGPSPlus gps;

long counter = 0;

// Set these to run example.
#define FIREBASE_HOST "hackoutio.firebaseio.com"
#define FIREBASE_AUTH "83eYwz3hXHtei66OfV94yLIpQy7P0pws9K0LKTXZ"
#define WIFI_SSID "Utkrisht"
#define WIFI_PASSWORD "gutku@10"

//Outside Temperature
#define DHTTYPE DHT11
#define dht_dpin 0
DHT dht(dht_dpin, DHTTYPE);
float h=0;
float t=0;

//Vibrations
int vibrationPin = D5;
float vibrationValue =0;


//Accel
const int MPU6050_addr=0x68;
int16_t AccX,AccY,AccZ,Temp,GyroX,GyroY,GyroZ;

//Microphone
int microphonePin = D5;
float microphoneValue = 0;

//Body Temperature
int tempPin = A0;
int tempValue = 0;

void setup() {
  
  Serial.begin(9600);

  // connect to wifi.
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("connecting");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  Serial.println();
  Serial.print("connected: ");
  Serial.println(WiFi.localIP());
  
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);

  //Outside Temperature
  dht.begin();
  
  //Accel
  Wire.begin();
  Wire.beginTransmission(MPU6050_addr);
  Wire.write(0x6B);
  Wire.write(0);
  Wire.endTransmission(true);

}

void loop() {

accel();
bodyTemp();
microPhone();
outerTemp();
//vibration();
gpsLocation();
delay(50);
Firebase.setFloat("Animals/Cows/Cow 1/Sensors/Daily Steps/Value", counter);
counter++;
}
void accel(){
  Wire.beginTransmission(MPU6050_addr);
  Wire.write(0x3B);
  Wire.endTransmission(false);
  Wire.requestFrom(MPU6050_addr,14,true);
  AccX=Wire.read()<<8|Wire.read();
  AccY=Wire.read()<<8|Wire.read();
  AccZ=Wire.read()<<8|Wire.read();
  GyroX=Wire.read()<<8|Wire.read();
  GyroY=Wire.read()<<8|Wire.read();
  GyroZ=Wire.read()<<8|Wire.read();
  Firebase.setFloat("Animals/Cows/Cow 1/Sensors/Acc X/Value", AccX);
  Firebase.setFloat("Animals/Cows/Cow 1/Sensors/Acc Y/Value", AccY);
  Firebase.setFloat("Animals/Cows/Cow 1/Sensors/Acc z/Value", AccZ);
  Firebase.setFloat("Animals/Cows/Cow 1/Sensors/Gyro X/Value", GyroX);
  Firebase.setFloat("Animals/Cows/Cow 1/Sensors/Gyro Y/Value", GyroY);
  Firebase.setFloat("Animals/Cows/Cow 1/Sensors/Gyro Z/Value", GyroZ);
}
void microPhone(){
  microphoneValue = analogRead(microphonePin);
  Firebase.setFloat("Animals/Cows/Cow 1/Sensors/Microphone/Value", microphoneValue);
}
void bodyTemp(){
  tempValue=analogRead(tempPin);
  float mv = ( tempValue *4.88 );
  mv=mv/10;
  Firebase.setFloat("Animals/Cows/Cow 1/Sensors/Body Temperature/Value", mv);
}
void outerTemp(){
  h = dht.readHumidity();
  t = dht.readTemperature();
  Firebase.setFloat("Animals/Cows/Cow 1/Sensors/Humidity/Value", h);
  Firebase.setFloat("Animals/Cows/Cow 1/Sensors/Outside Temperature/Value", t);
}
void vibration(){
  vibrationValue = analogRead(vibrationPin);
  Firebase.setFloat("counter/"+String(counter)+"/Vibrations", vibrationValue);
}
void gpsLocation(){
  displayInfo();
}
void displayInfo()
{
  Serial.print(F("Location: ")); 
  if (gps.location.isValid())
  {
    Serial.print(gps.location.lat(), 6);
    Serial.print(F(","));
    Serial.print(gps.location.lng(), 6);
    Firebase.setFloat("Animals/Cows/Cow 1/Location/Latitude/Value", gps.location.lat());
    Firebase.setFloat("Animals/Cows/Cow 1/Location/Longitude/Value", gps.location.lng());
  }
  else
  {
    Serial.print(F("INVALID"));
    
    Firebase.setFloat("Animals/Cows/Cow 1/Location/Latitude/Value", 30.1079528);
    Firebase.setFloat("Animals/Cows/Cow 1/Location/Longitude/Value", 78.2813377);
  }
  Serial.println();
}
