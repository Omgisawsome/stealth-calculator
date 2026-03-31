import machine
import time

ROWS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
COLS = [12, 13, 14, 15, 16, 17]

# UART moved to GP20/GP21 to avoid conflict with the Matrix scanning pins
uart = machine.UART(1, baudrate=9600, tx=machine.Pin(20), rx=machine.Pin(21))

KEY_MAP = {
    "R1C1": "SHIFT", "R1C2": "ALPHA", "R1C3": "UP", "R1C5": "MODE", "R1C6": "ON",
    "R2C1": "LEFT", "R3C1": "RIGHT", "R4C1": "DOWN",
    "R5C1": "CALC", "R5C2": "INTEGRAL", "R5C3": "X_INV", "R5C4": "LOG_B",
    "R6C1": "FRAC", "R6C2": "SQRT", "R6C3": "X_SQR", "R6C4": "X_POW", "R6C5": "LOG", "R6C6": "LN",
    "R7C1": "NEG", "R7C2": "TIME", "R7C3": "HYP", "R7C4": "SIN", "R7C5": "COS", "R7C6": "TAN",
    "R8C1": "RCL", "R8C2": "ENG", "R8C3": "L_BRACKET", "R8C4": "R_BRACKET", "R8C5": "SD", "R8C6": "M_PLUS",
    "R9C1": "7", "R9C2": "8", "R9C3": "9", "R9C4": "DEL", "R9C5": "AC",
    "R10C1": "4", "R10C2": "5", "R10C3": "6", "R10C4": "MULT", "R10C5": "DIV",
    "R11C1": "1", "R11C2": "2", "R11C3": "3", "R11C4": "PLUS", "R11C5": "MINUS",
    "R12C1": "0", "R12C2": "DOT", "R12C3": "EXP", "R12C4": "ANS", "R12C5": "EQUAL"
}

row_pins = [machine.Pin(p, machine.Pin.OUT) for p in ROWS]
col_pins = [machine.Pin(p, machine.Pin.IN, machine.Pin.PULL_DOWN) for p in COLS]

def scan_matrix():
    for r_idx, r_pin in enumerate(row_pins):
        r_pin.value(1)
        for c_idx, c_pin in enumerate(col_pins):
            if c_pin.value() == 1:
                code = f"R{r_idx+1}C{c_idx+1}"
                label = KEY_MAP.get(code, "UNUSED")
                
                uart.write(label + "\n")
                print(f"Sent to Pi: {label}")

                while c_pin.value() == 1:
                    time.sleep(0.05)
        r_pin.value(0)

print("Stealth Calc Matrix Scanner Active...")
while True:
    scan_matrix()
    time.sleep(0.01)