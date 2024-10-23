#define MOTOR PD1
#define LIGA_PIN PB1
#define DESLIGA_PIN PB2

uint8_t motor_ligado = 0;
uint8_t contando_tempo = 0;

void iniciar_timer_10s() {
    TCCR1B |= (1 << WGM12); 
    OCR1A = 15624 * 10; // 10 segundos
    TIMSK1 |= (1 << OCIE1A); 
    TCCR1B |= (1 << CS12) | (1 << CS10);
}

void parar_timer() {
    TCCR1B = 0;
    TIMSK1 &= ~(1 << OCIE1A);
    contando_tempo = 0;
}

ISR(INT0_vect) {
    if (!motor_ligado && !contando_tempo) {
        iniciar_timer_10s();
        contando_tempo = 1;
    }
}

ISR(INT1_vect) {
    if (motor_ligado) {
        PORTD &= ~(1 << MOTOR);
        motor_ligado = 0;
    }
    parar_timer();
}

ISR(TIMER1_COMPA_vect) {
    if (contando_tempo) {
        PORTD |= (1 << MOTOR);
        motor_ligado = 1;
        parar_timer();
    }
}

int main(void) {
    DDRD |= (1 << MOTOR);
    PORTD &= ~(1 << MOTOR);

    DDRB &= ~(1 << LIGA_PIN);
    DDRB &= ~(1 << DESLIGA_PIN);

    EICRA |= (1 << ISC11);
    EICRA |= (1 << ISC01);
    EIMSK |= (1 << INT1) | (1 << INT0);

    sei();

    while (1);
}
