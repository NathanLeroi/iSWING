#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ESP8266WiFi.h>
#include <WiFiClient.h> 
#include <ESP8266WebServer.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_FXAS21002C.h>
#include <Adafruit_FXOS8700.h>

#define ARRAYSIZE 600

Adafruit_FXAS21002C gyro = Adafruit_FXAS21002C(0x0021002C);  
Adafruit_FXOS8700 accelmag = Adafruit_FXOS8700(0x8700A, 0x8700B);

int i, j;
float t = 0.00;
char Buffer[3][5000];   // multidimensional array to store the data

const char *ssid = "IMUWiFiNathan";  // ID of the WiFi access point I'll create
const char *password = "";     // Empty which means no password shall be required
ESP8266WebServer server(80);

/* Go to http://192.168.4.1 in a web browser */

void handleRoot() {   
                          
  server.send(200, "text/html", "0");
}


void buffer(){
  
  for(i=0; i<ARRAYSIZE; i++){
  
  sensors_event_t aevent;     //I'm here calling the sensors in order to collect some data
  sensors_event_t gevent;
  accelmag.getEvent(&aevent);
  gyro.getEvent(&gevent);

   
  dtostrf(t, 7, 2, &Buffer[0][i*7]);  // I'm saving data at specific interval in the array
  dtostrf(aevent.acceleration.x, 7, 2, &Buffer[1][i*7]);
  dtostrf(gevent.gyro.y, 7, 2, &Buffer[2][i*7]);

  t = t + 0.02;
  
  delay(20);   // setting up a refresh time of 20ms
  
}

for(j=1; j<ARRAYSIZE; j++){
  
  Buffer[0][j*7] = ',';     // I'm placing a "," to seperate each data point
  Buffer[1][j*7] = ',';     // preparing it for parsing/scraping with python
  Buffer[2][j*7] = ',';
  
}

  String html = Buffer[0];    //"Displaying" the lines of data as a formatted HTML txt
  html += "\n";                     
  html += Buffer[1];
  html +="\n";
  html += Buffer[2];

server.send(200, "text/html", html);

}


void setup() {
	
	delay(1000);
	Serial.begin(115200);

  if(!accelmag.begin(ACCEL_RANGE_2G)) //initializing the accelerometer
    {
      while(1);
    } 
  if(!gyro.begin(GYRO_RANGE_250DPS)) //initializing the gyroscope
    {
      while(1);
    }
 
	WiFi.softAP(ssid, password); // WiFi.softAP(ssid, password, channel);

	IPAddress myIP = WiFi.softAPIP();
	Serial.print("AP IP address: ");
	Serial.println(myIP);
	server.on("/", handleRoot);         
	server.on("/buffer", buffer); // activates buffer function when http://192.168.4.1/buffer requested
	server.begin();               // starting the server
	Serial.println("HTTP server started");
}

void loop() {
	server.handleClient();
}
