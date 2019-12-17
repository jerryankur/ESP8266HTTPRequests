#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
void setup() {
  Serial.begin(9600);
  Serial.println("Board booted");
  WiFi.begin("iitk");    //WiFi.begin("User","Password")        i used iitk to connect through IIT Kanpur campus network
  Serial.print("Connecting");
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println();
  Serial.print("Connected, IP address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  int i=0;
  if(WiFi.status()==WL_CONNECTED)
  {
    WiFiClient client;
    HTTPClient hc;
    hc.begin(client,"http://172.26.194.220:5000/data");
    hc.addHeader("Content-Type","application/json");
    hc.POST("{\"Counter\":i}");
    i++;
  }
  delay(1000);
}
