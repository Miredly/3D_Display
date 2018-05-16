#include <Adafruit_NeoPixel.h>
#include <math.h>

#define SIDE 8
//set up the pin that controls the LEDs, the type of LEDs (WS2812B) and the number of LEDs in the cube (8*8*8=512)
#define PIXEL_PIN 2 //the L3D cube requires pin 2
// How many NeoPixels are attached to the Arduino?
#define PIXEL_COUNT 512
// When we setup the NeoPixel library, we tell it how many pixels, and which pin to use to send signals.
// Note that for older NeoPixel strips you might need to change the third parameter--see the strandtest
// example for more information on possible values.
#define PIXEL_TYPE NEO_GRB + NEO_KHZ800
Adafruit_NeoPixel strip = Adafruit_NeoPixel(PIXEL_COUNT, PIXEL_PIN, NEO_GRB + NEO_KHZ800);


//millies()
//Make color structure
typedef struct {
  unsigned char red, green, blue;
} color;

color black;
color red;
color blue;
color green;
color pink;
color sun;

color Color_List[8];

bool should_run;
int index;

void setup() {
  index = 0;
  //  initTest();
  randomSeed(analogRead(0));
  Serial.begin(115200);
  //  int red = 255;
  //  int green = 0;
  //  int blue = 0;
  //    strip.setBrightness(25);
  strip.begin();
  strip.show();

  should_run = true;


  //Define colors with the color structure.
  black.red = 0;
  black.green = 0;
  black.blue = 0;


  red.red = 255;
  red.green = 0;
  red.blue = 0;

  blue.red = 0;
  blue.green = 0;
  blue.blue = 255;

  green.red = 0;
  green.green = 255;
  green.blue = 0;

  //  pink.red = 221;
  //  pink.green = 160;
  //  pink.blue = 221;

  pink.red = 255;
  pink.green = 0;  // for some reason, the cube gets weird with blended colors, aka values that are not primary colors or immediate blends of primary colors.
  pink.blue = 255;

  sun.red = 100;
  sun.blue = 6;
  sun.green = 26;

  Color_List[0] = red;
  Color_List[1] = red;
  Color_List[2] = green;
  Color_List[3] = green;
  Color_List[4] = blue;
  Color_List[5] = blue;
  Color_List[6] = pink;
  Color_List[7] = pink;

}

void loop() {

//  setPixel(3, 3, 3, sun);
//  setPixel(3, 3, 4, sun);
//  setPixel(3, 2, 3, sun);
//  setPixel(3, 2, 4, sun);
//  setPixel(4, 3, 3, sun);
//  setPixel(4, 3, 4, sun);
//  setPixel(4, 2, 3, sun);
//  setPixel(4, 2, 4, sun);

  int randx = int(random(8));
  int randy = int(random(3) + 3);
  while (should_run == true) {
    randx = random(8);
    randy = random(8);
    particalTrack(randx, randy);
    if (index > 3) {
      should_run = false;
      //      index++;
    }
  }
  //  particalTrack(randx, randy);
  fadePixel(15);
  strip.show();
  //  delay(1000);

}

void particalTrack(int start_x, int start_y) { //this function creates tracks that represent the way particals ricochet from molecule to molecule in an aurora

  float x = start_x;
  float y = start_y;
  float z = 7;

  float new_x = x;
  float new_y = y;
  float new_z = 0;

  int ii = z;

  //x, z, y
  setPixel(x, z, y, Color_List[ii]);

  int randnum = 0;

  while (ii > 0 ) {

    new_z = ii - 1;
    //    new_y = y;
    randnum = int(random(3));
    new_x = new_x + (1 - randnum);
    //    Serial.println(new_x);

    if (new_x < 7) {
      if (new_x > 0) {
        setPixel(new_x, new_z, new_y, Color_List[ii]);
      }
    }
    ii--;
    delay(50);
    fadePixel(15);
    strip.show();
    //    strip.begin();
  }

}

void setPixel(int x, int y, int z, color pix_color) {

  int index = (z * SIDE * SIDE) + (x * SIDE) + y;
  strip.setPixelColor(index, strip.Color(pix_color.red,  pix_color.green, pix_color.blue));

}

//returns the color value currently displayed at the x,y,z location
color getPixel(int x, int y, int z)
{
  int index = (z * SIDE * SIDE) + (x * SIDE) + y;
  uint32_t col = strip.getPixelColor(index);
  color pixelColor;
  pixelColor.red = (col >> 16) & 255;
  pixelColor.green = (col >> 8) & 255;
  pixelColor.blue = col & 255;
  return pixelColor;
}

void fadePixel(int fadespeed) {
  for (int x = 0; x < 8; x++) {
    for (int y = 0; y < 8; y++) {
      for (int z = 0; z < 8; z++) {
        color pixel = getPixel(x, y, z);
        if (pixel.red > 0) {
          pixel.red -= fadespeed;
          if (pixel.red < 0) {
            pixel.red = 0;
          }
        }
        if (pixel.green > 0) {
          pixel.green -= fadespeed;
          if (pixel.green < 0) {
            pixel.green = 0;
          }
        }
        if (pixel.blue > 0) {
          pixel.blue -= fadespeed;
          if (pixel.blue < 0) {
            pixel.blue = 0;
          }
        }
        setPixel(x, y, z, pixel);
      }
    }
  }
}

void initTest() {
  int i = 0;
  while (i < PIXEL_COUNT) {
    strip.setPixelColor(i - 1, 0, 0, 0);
    strip.setPixelColor(i, 255, 0, 0);
    strip.show();
    i++;
    delay(10);
  }
  strip.setPixelColor(i - 1, 0, 0, 0);
  strip.show();
}

