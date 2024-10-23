#define MOTOR_PIN PD7
#define LIGA_PIN PC0
#define DESLIGA_PIN PC1
#define S1_PIN PB0
#define S2_PIN PB1

uint8_t motor_ligado = 0;
uint8_t sentido_horario = 1;

ISR(PCINT0_vect) {
    if (PINB & (1 << S1_PIN)) {
        PORTD &= ~(1 << MOTOR_PIN);
        _delay_ms(5500);
        sentido_horario = 0;
    }

    if (PINB & (1 << S2_PIN)) {
        PORTD &= ~(1 << MOTOR_PIN);
        _delay_ms(7500);
        sentido_horario = 1;
    }
}

ISR(PCINT1_vect) {
    if (PINC & (1 << DESLIGA_PIN)) {
        PORTD &= ~(1 << MOTOR_PIN);
        motor_ligado = 0;
    }
}

int main(void) {
    DDRD |= (1 << MOTOR_PIN);
    DDRC &= ~((1 << LIGA_PIN) | (1 << DESLIGA_PIN));
    DDRB &= ~((1 << S1_PIN) | (1 << S2_PIN));

    PCICR |= (1 << PCIE0) | (1 << PCIE1);
    PCMSK0 |= (1 << PCINT0) | (1 << PCINT1);
    PCMSK1 |= (1 << PCINT8) | (1 << PCINT9);

    sei();

    while (1) {
        if (PINC & (1 << LIGA_PIN)) {
            if (!motor_ligado) {
                motor_ligado = 1;
                if (sentido_horario) {
                    PORTD |= (1 << MOTOR_PIN);
                } else {
                    PORTD &= ~(1 << MOTOR_PIN);
                }
            }
        }
    }
}
