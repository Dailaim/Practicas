#include <piezo-music.h>

/*

C = DO
D = RE
E = MI
F = FA
G = SOL
A = LA
B = SI
S = Sostenido Ejemplo: NOTE_AS5   --> Corresponde a la nota LA sostenido en la octaba numero 5

*/



int melodia[] = {
  NOTE_E6, NOTE_DS6, NOTE_E6, NOTE_DS6,
  NOTE_E6, NOTE_B5 ,NOTE_D6, NOTE_C6,
  NOTE_A5,PAUSE,NOTE_C5,NOTE_E5,
  NOTE_A5,NOTE_B5,PAUSE, NOTE_E5, 
  NOTE_GS5,NOTE_B5,NOTE_C6,PAUSE,
  NOTE_E5,NOTE_E6,NOTE_DS6,NOTE_E6,
  NOTE_DS6,NOTE_E6,NOTE_B5,NOTE_D6,
  NOTE_C6, NOTE_A5,PAUSE,NOTE_C5,
  NOTE_E5, NOTE_A5, NOTE_B5,PAUSE,
  NOTE_E5,NOTE_C6,NOTE_B5,NOTE_A5,
  PAUSE,NOTE_B5,NOTE_C6, NOTE_D6,
  NOTE_E6, NOTE_G5, NOTE_F6,NOTE_E6,
  NOTE_D6, NOTE_F5, NOTE_E6, NOTE_D6,
  NOTE_C6, NOTE_E5, NOTE_D6,NOTE_C6,
  NOTE_B5, PAUSE, NOTE_E5,NOTE_E6,
  PAUSE,PAUSE,NOTE_E6,NOTE_E7,
  PAUSE,NOTE_DS6, NOTE_E6, PAUSE,
  NOTE_DS6, NOTE_E6, NOTE_DS6,NOTE_E6,
  NOTE_DS6, NOTE_E6, NOTE_B5, NOTE_D6,
  NOTE_C6, NOTE_A5, PAUSE,NOTE_C5,
  NOTE_E5,NOTE_A5, NOTE_B5,PAUSE,
  NOTE_E5,NOTE_GS5,NOTE_B5,NOTE_C6,
  PAUSE, NOTE_E5,NOTE_E6,NOTE_DS6,
  NOTE_E6,NOTE_DS6,NOTE_E6,NOTE_B5,
  NOTE_D6,NOTE_C6,NOTE_A5,PAUSE,
  NOTE_C5,NOTE_E5,NOTE_A5,NOTE_B5,
  PAUSE,NOTE_E5,NOTE_C6,NOTE_B5,
  NOTE_A5,PAUSE
};

int ritmo[] = {
  6,6,6,6,
  6,6,6,6,
  4,6,6,6,
  6,4,6,6,
  6,6,4,6,
  6,6,6,6, 
  6,6,6,6,
  6,4,6,6,
  6,6,4,6,
  6,6,6,4,
  6,6,6,6,
  3,6,6,6,
  3,6,6,6,
  3,6,6,6,
  4,6,6,6,
  6,6,6,6,
  6,6,6,6,
  6,6,6,6,
  6,6,6,6,
  6,4,6,6,
  6,6,4,6,
  6,6,6,4,
  6,6,6,6,
  6,6,6,6,
  6,6,4,6,
  6,6,6,4,
  6,6,6,6,
  2,4
};

const int pin = 5; 

int cantidad = sizeof(melodia)/sizeof(melodia[0]);

void setup()
{

}
 
void loop()
{
  delay(1000);
  playSong(pin, melodia, ritmo, cantidad, 50);

}
