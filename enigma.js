class Rotors {
    constructor(positions) {
        this.rotor1 = 'DMTWSILRUYQNKFEJCAZBPGXOHV';
        this.rotor2 = 'HQZGPJTMOBLNCIFDYAWVEUSRKX';
        this.rotor3 = 'UQNTLSZFMREHDPXKIBVYGJCWOA';
        this.positions = positions;
        this.init_position();
    }

    init_position() {
        this.rotor1 = this.rotor1.slice(this.positions[0]) + this.rotor1.slice(0, this.positions[0]);
        this.rotor2 = this.rotor2.slice(this.positions[1] % 26) + this.rotor2.slice(0, this.positions[1] % 26);
        this.rotor3 = this.rotor3.slice(this.positions[2] % 676) + this.rotor3.slice(0, this.positions[2] % 676);
    }

    rotor_rotation() {
        this.rotor1 = this.rotor1.slice(1) + this.rotor1.charAt(0);
        this.positions[0] += 1;
        if (this.positions[0] > 26) {
            this.positions[0] = 1;
            this.rotor2 = this.rotor2.slice(1) + this.rotor2.charAt(0);
            this.positions[1] += 1;
            if (this.positions[1] > 26) {
                this.positions[1] = 1;
                this.rotor3 = this.rotor3.slice(1) + this.rotor3.charAt(0);
                this.positions[2] += 1;
                if (this.positions[2] > 26) {
                    this.positions[2] = 1;
                }
            }
        }
    }

    get_value(letter) {
        let index = this.rotor1.indexOf(letter);
        let value = this.rotor2.charAt(index);
        value = this.rotor3.charAt(this.rotor2.indexOf(value));
        return value;
    }

    get_value_reverse(letter) {
        let index = this.rotor3.indexOf(letter);
        let value = this.rotor2.charAt(index);
        value = this.rotor1.charAt(this.rotor2.indexOf(value));
        return value;
    }
}

function reflector(letter) {
    const wiring = 'EJMZALYXVBWFCRQUONTSPIKHGD';
    return wiring[letter.charCodeAt(0) - 65];
}

function plugboard(letter, wiring) {
    return wiring[letter];
}

function enigma_machine(message, position) {
    const plugboard_wiring = { 'A': 'B', 'B': 'A', 'C': 'D', 'D': 'C', 'E': 'F', 'F': 'E', 'G': 'H', 'H': 'G', 'I': 'J', 'J': 'I' };
    const rotors = new Rotors(position);
    let output = '';

    for (let i = 0; i < message.length; i++) {
        let letter = message[i].toUpperCase();
        if (!/[A-Z]/.test(letter)) {
            output += letter;
            continue;
        }
        rotors.rotor_rotation();
        if (letter in plugboard_wiring) {
            letter = plugboard(letter, plugboard_wiring);
        }
        letter = rotors.get_value(letter);
        letter = reflector(letter);
        letter = rotors.get_value_reverse(letter);
        if (letter in plugboard_wiring) {
            letter = plugboard(letter, plugboard_wiring);
        }
        output += letter;
    }
    return output;
}
