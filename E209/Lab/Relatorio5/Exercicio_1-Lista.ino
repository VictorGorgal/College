#define Led1 (0b00000010)
#define Led2 (0b00000001)
#define LIGA_PIN (1 << PD7)
#define DESLIGA_PIN (1 << PD6)
#define S1_PIN (1 << PD5)

int main(void) {
  DDRD = DDRD | Led1;
  DDRD = DDRD | Led2;

  DDRD &= ~(LIGA_PIN);
  DDRD &= ~(DESLIGA_PIN);
  DDRD &= ~(S1_PIN);

  PORTD = PORTD & ~(Led1);
  PORTD = PORTD & ~(Led2);

  for (;;) {
    int liga = PIND & LIGA_PIN;
    int desliga = PIND & DESLIGA_PIN;
    int s1 = PIND & S1_PIN;

    if (liga && !s1) {
      PORTD = PORTD | Led2;
    }

    if (desliga || s1) {
      PORTD = PORTD & ~(Led2);
    }

    if (s1) {
      PORTD = PORTD | Led1;
    }

    if (!s1 && liga) {
      PORTD = PORTD & ~(Led1);
    }

    _delay_ms(100);
  }
}
