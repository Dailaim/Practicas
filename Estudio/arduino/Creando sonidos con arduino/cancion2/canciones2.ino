#include <piezo-music.h>
#include <example-music.h>
/*-----------------------------------------------------------------------------------------------

C = DO
D = RE
E = MI
F = FA
G = SOL
A = LA
B = SI
S = Sostenido Ejemplo: NOTE_AS5   --> Corresponde a la nota LA sostenido en la octaba numero 5

-----------------------------------------------------------------------------------------------*/

const int pin = 8; 


int cantidad = sizeof(zelda_main_theme_melody)/sizeof(zelda_main_theme_melody[0]);
void setup()
{
  Serial.begin(9600);
 //playSong(pin, mario_underworld_melody, mario_underworld_rythm, cantidad, 40);
}
 
void loop()
{
  delay(1000);
playSong(pin, zelda_main_theme_melody, zelda_main_theme_rythm, cantidad, 40);
  delay(1000);
}
