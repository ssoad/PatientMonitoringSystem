#include <EtherCard.h>
#include <SimpleDHT.h>
#include <TimerOne.h>
#define STATIC 0  // set to 1 to disable DHCP (adjust myip/gwip values below)

int dht_pin = 8;
int counter = 0;
int t =0; 
SimpleDHT11 dht11(dht_pin);

// pin defs
int pressurePin = A3;
int HBSensor = 4;
int HBCount = 0;
int HBCheck = 0;
int TimeinSec = 0;
int HBperMin = 0;
int HBStartCheck = 0;

// variables
int val;

#if STATIC
// ethernet interface ip address
static byte myip[] = { 192,168,1,200 };
// gateway ip address
static byte gwip[] = { 192,168,1,1 };
#endif

// ethernet mac address - must be unique on your network
static byte mymac[] = { 0x74,0x69,0x69,0x2D,0x30,0x31 };

byte Ethernet::buffer[500]; // tcp/ip send and receive buffer
BufferFiller bfill;

void setup () {
  Serial.begin(9600);
   pinMode(HBSensor, INPUT);
  Timer1.initialize(800000); 
  Timer1.attachInterrupt( timerIsr );

  if (ether.begin(sizeof Ethernet::buffer, mymac) == 0) 
    Serial.println( "Try to access Ethernet controller");
  #if STATIC
  ether.staticSetup(myip, gwip);
  #else
  if (!ether.dhcpSetup())
    Serial.println("DHCP failed");
  #endif

  ether.printIp("IP:  ", ether.myip);
  ether.printIp("Gateway:  ", ether.gwip);  
  ether.printIp("DNS: ", ether.dnsip);
}

static word homePage() {
  byte temperature = 0;
  byte humidity = 0;
  int err = SimpleDHTErrSuccess;
  if ((err = dht11.read(&temperature, &humidity, NULL)) != SimpleDHTErrSuccess) {
    delay(2000);
    return;
  }
  int temp = (int)temperature;
  int hum = (int)humidity;
  val = analogRead(pressurePin)/8;
  
  // only for simulation ..hardware algorith might be diffrent
  bfill = ether.tcpOffset();
  bfill.emit_p(PSTR(
    "HTTP/1.0 200 OK\r\n"
    "Content-Type: application/json\r\n"
    "Pragma: no-cache\r\n"
    "\r\n"
    "{"
    "\"title\":\"my sensor update\"," 
    "\"heart_rate\":$D,"
    "\"temp\":$D,"
    "\"bmp\":$D,"
    "\"humidity\":$D"
  "}"
   ),
      HBperMin,temp,val, hum);
  return bfill.position();
}

void loop () {
   
  HBStartCheck = 1;
  if(HBStartCheck == 1)
  {
      if((digitalRead(HBSensor) == HIGH) && (HBCheck == 0))
      {
        HBCount = HBCount + 1;
        HBCheck = 1; 
      }
      
      if((digitalRead(HBSensor) == LOW) && (HBCheck == 1))
      {
        HBCheck = 0;    
      }
      
      if(TimeinSec == 10)
      {
          HBperMin = HBCount * 6;
          HBStartCheck = 0;
          HBCount = 0;
          TimeinSec = 0;
//          Serial.print("HB");
//          Serial.println(HBperMin);  
      }
  }         
  word len = ether.packetReceive();
  word pos = ether.packetLoop(len);
  if (pos)  // check if valid tcp data is received
    ether.httpServerReply(homePage()); // send web page data
}

void timerIsr()
{  
  if(HBStartCheck == 1)
  {
      TimeinSec = TimeinSec + 1;
  } 
}
