#include <stdio.h>

uint8_t horas = 0;
uint8_t minutos = 0;
uint8_t segundos = 0;

ISR(TIMER1_COMPA_vect) {
    segundos++;
    if (segundos >= 60) {
        segundos = 0;
        minutos++;
        if (minutos >= 60) {
            minutos = 0;
            horas++;
            if (horas >= 24) {
                horas = 0;
            }
        }
    }

    char buffer[10];
    sprintf(buffer, "%02d:%02d:%02d", horas, minutos, segundos);
}

int main(void) {
    TCCR1B |= (1 << WGM12); 
    OCR1A = 15624;
    TIMSK1 |= (1 << OCIE1A); 
    TCCR1B |= (1 << CS12) | (1 << CS10);

    sei();

    while (1);
}
