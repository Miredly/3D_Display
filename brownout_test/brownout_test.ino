#include <Adafruit_NeoPixel.h>
#include <math.h>

//set up the pin that controls the LEDs, the type of LEDs (WS2812B) and the number of LEDs in the cube (8*8*8=512)
#define PIXEL_PIN 2
// How many NeoPixels are attached to the Arduino?
#define PIXEL_COUNT 512
// When we setup the NeoPixel library, we tell it how many pixels, and which pin to use to send signals.
// Note that for older NeoPixel strips you might need to change the third parameter--see the strandtest
// example for more information on possible values.
#define PIXEL_TYPE NEO_GRB + NEO_KHZ800
Adafruit_NeoPixel strip = Adafruit_NeoPixel(PIXEL_COUNT, PIXEL_PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  strip.begin();
  strip.show();
}

void loop() {
  int red = 255;
  int green = 0;
  int blue = 255;
  int i = 0;
  while (i < PIXEL_COUNT) {
//    strip.setPixelColor(i - 1, 0, 0, 0);
    strip.setPixelColor(i, red, green, blue);
    strip.show();
    i++;
    delay(10);
  }

    strip.setPixelColor(i-1, 0, 0, 0);

    strip.show();
}

