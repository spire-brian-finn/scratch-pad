def ccsds_tc_randomizer_bits(n_bits: int):
    """
    Generate n_bits of the CCSDS TC randomizer sequence
    following section 6.2 of https://ccsds.org/Pubs/231x0b4e1.pdf
    The spec claims the polynomial is
    h(x) = x^8 + x^6 + x^4 + x^3 + x^2 + x + 1,
    but the diagram just below it seems to suggest
    x^7 + x^5 + x^4 + x^3 + x^2 + x
    and that one matches the 40 bits of the sequence given in the spec,
    1111 1111 0011 1001 1001 1110 0101 1010 0110 1000
    """
    state = 0xFF  # Initialize to all 1
    bits = []

    for _ in range(n_bits):
        out_bit = state & 0x01
        bits.append(out_bit)

        fb = (
            ((state >> 6) & 1) ^
            ((state >> 4) & 1) ^
            ((state >> 3) & 1) ^
            ((state >> 2) & 1) ^
            ((state >> 1) & 1) ^
            ((state >> 0) & 1)
        )

        # Shift right, insert feedback into MSB
        state = ((state >> 1) & 0x7F) | (fb << 7)

    return bits, state

# Generate and print a 100-bit sequence
seq, state = ccsds_tc_randomizer_bits(256)

byte_value = 0
reversed_byte_value = 0
print("Right order:\t\tReversed:")
for i, bit in enumerate(seq):
    if i > 0 and i % 8 == 0:
        print(f"{byte_value:0=#4x}\t{byte_value:0=8b}\t{reversed_byte_value:0=#4x}\t{reversed_byte_value:0=8b}")
        byte_value = 0
        reversed_byte_value = 0
    byte_value |= (bit << (7 - (i % 8)))  # Shift bits into byte MSB-first, per spec
    reversed_byte_value |= (bit << (i % 8))  # Shift bits into byte LSB-first
