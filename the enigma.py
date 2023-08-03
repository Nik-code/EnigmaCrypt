class Rotors:
    rotor1 = 'DMTWSILRUYQNKFEJCAZBPGXOHV'
    rotor2 = 'HQZGPJTMOBLNCIFDYAWVEUSRKX'
    rotor3 = 'UQNTLSZFMREHDPXKIBVYGJCWOA'

    def __init__(self, positions):
        self.positions = positions
        self.init_position()

    def init_position(self):
        self.rotor1 = self.rotor1[self.positions[0]:] + self.rotor1[:self.positions[0]]
        self.rotor2 = self.rotor2[self.positions[1] % 26:] + self.rotor2[:self.positions[1] % 26]
        self.rotor3 = self.rotor3[self.positions[2] % 676:] + self.rotor3[:self.positions[2] % 676]

    def rotor_rotation(self):
        self.rotor1 = self.rotor1[1:] + self.rotor1[0]
        self.positions[0] += 1
        if self.positions[0] > 26:
            self.positions[0] = 1
            self.rotor2 = self.rotor2[1:] + self.rotor2[0]
            self.positions[1] += 1
            if self.positions[1] > 26:
                self.positions[1] = 1
                self.rotor3 = self.rotor3[1:] + self.rotor3[0]
                self.positions[2] += 1
                if self.positions[2] > 26:
                    self.positions[2] = 1

    def get_value(self, letter):
        # Value from rotor1
        value = self.rotor1[ord(letter) - 65]
        # Value from rotor2 using the value from rotor1
        value = self.rotor2[ord(value) - 65]
        # Value from rotor3 using the value from rotor2
        value = self.rotor3[ord(value) - 65]
        return value

    def get_value_reverse(self, letter):
        # Value from rotor3
        value = chr(self.rotor3.index(letter) + 65)
        # Value from rotor2 using the value from rotor3
        value = chr(self.rotor2.index(value) + 65)
        # Value from rotor1 using the value from rotor2
        value = chr(self.rotor1.index(value) + 65)
        return value


def reflector(letter):
    wiring = 'EJMZALYXVBWFCRQUONTSPIKHGD'
    return wiring[ord(letter) - 65]


def plugboard(letter, wiring):
    return wiring[letter]


def enigma_machine(message, position):
    plugboard_wiring = {'A': 'B', 'B': 'A', 'C': 'D', 'D': 'C', 'E': 'F', 'F': 'E', 'G': 'H', 'H': 'G', 'I': 'J', 'J': 'I'}
    # Initialize the rotors
    rotors = Rotors(position)
    # Initialize the output
    output = ''

    for letter in message:
        # Make sure the letter is uppercase
        letter = letter.upper()
        # If the letter is not a letter, skip it
        if letter not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            output += letter
            continue
        # Rotate the rotors
        rotors.rotor_rotation()
        # Pass the letter through the plugboard
        if letter in plugboard_wiring:
            letter = plugboard_wiring[letter]

        # Pass the letter through the rotors
        letter = rotors.get_value(letter)
        # Pass the letter through the reflector
        letter = reflector(letter)
        # Pass the letter through the rotors in reverse
        letter = rotors.get_value_reverse(letter)
        # Pass the letter through the plugboard
        if letter in plugboard_wiring:
            letter = plugboard_wiring[letter]
        # Add the letter to the output
        output += letter
    return output

