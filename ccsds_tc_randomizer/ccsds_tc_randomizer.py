def ccsds_tc_randomizer_bits(n_bits: int):
    """
    Generate n_bits of the CCSDS TC randomizer (BTG) sequence
    defined by h(x) = x^8 + x^6 + x^4 + x^3 + x^2 + x + 1,
    with 8-bit LFSR initialized to all ones.
    """
    state = 0xFF  # X8..X1 = 1
    bits = []

    for _ in range(n_bits):
        # Output bit (take X1 = LSB)
        out_bit = state & 0x01
        bits.append(out_bit)

        # Feedback = XOR of taps X8, X6, X4, X3, X2, X1
        # which are bits 7,5,3,2,1,0 of 'state'
        fb = (
            ((state >> 6) & 1) ^
            ((state >> 4) & 1) ^
            ((state >> 3) & 1) ^
            ((state >> 2) & 1) ^
            ((state >> 1) & 1) ^
            ((state >> 0) & 1)
        )

        # Shift right, insert feedback into MSB (X8)
        state = ((state >> 1) & 0x7F) | (fb << 7)
        #state = ((state << 1) & 0xFE) | fb

    return bits, state

# Generate and print a 100-bit sequence
seq, state = ccsds_tc_randomizer_bits(256)

byte_value = 0
reversed_byte_value = 0
for i, bit in enumerate(seq):
    if i > 0 and i % 8 == 0:
        print(f"Right order: {byte_value:0=#4x}\t{byte_value:0=8b}\tReversed: {reversed_byte_value:0=#4x}\t{reversed_byte_value:0=8b}")
        byte_value = 0
        reversed_byte_value = 0
    byte_value |= (bit << (7 - (i % 8)))
    reversed_byte_value |= (bit << (i % 8))


# yee buddy now try to prove it's inverted in the code?