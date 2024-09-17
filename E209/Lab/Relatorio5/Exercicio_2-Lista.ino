#define M1_PIN (1 << PD0)
#define M2_PIN (1 << PD1)
#define M3_PIN (1 << PD2)

#define BUTTON_A (1 << PD3)
#define BUTTON_B (1 << PD4)
#define BUTTON_C (1 << PD5)

#define MOTOR1_POWER 30
#define MOTOR2_POWER 50
#define MOTOR3_POWER 70

int main(void) {
    DDRD |= M1_PIN;
    DDRD |= M2_PIN;
    DDRD |= M3_PIN;

    DDRD &= ~(BUTTON_A | BUTTON_B | BUTTON_C);

    PORTD &= ~(M1_PIN | M2_PIN | M3_PIN);

    for (;;) {
        int motor1_on = PIND & BUTTON_A;
        int motor2_on = PIND & BUTTON_B;
        int motor3_on = PIND & BUTTON_C;

        int total_power = 0;

        if (motor1_on) {
            total_power += MOTOR1_POWER;
            PORTD |= M1_PIN;
        } else {
            PORTD &= ~M1_PIN;
        }

        if (motor2_on) {
            total_power += MOTOR2_POWER;
            PORTD |= M2_PIN;
        } else {
            PORTD &= ~M2_PIN;
        }

        if (motor3_on) {
            total_power += MOTOR3_POWER;
            PORTD |= M3_PIN;
        } else {
            PORTD &= ~M3_PIN;
        }

        if (total_power > 90) {
            if (motor1_on) {
                PORTD &= ~M1_PIN;
                total_power -= MOTOR1_POWER;
            }
        }

        if (total_power > 90) {
            if (motor2_on) {
                PORTD &= ~M2_PIN;
                total_power -= MOTOR2_POWER;
            }
        }

        _delay_ms(100);
    }
}
