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
seq, state = ccsds_tc_randomizer_bits(255)
seq_str = ''.join(str(b) for b in seq)
print(state, seq_str)

#for i in e