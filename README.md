# Mini CTF Challenges

Welcome to the Mini CTF Challenges! This repository contains a series of fun and educational Capture The Flag (CTF) challenges designed to test your cybersecurity skills.

## Challenges

1. **Source Code Secrets** (Easy)
   - Find the hidden flag in the page source
   - [Start Challenge](challenge1.html)

2. **Password Cracker** (Medium)
   - Bypass the login form to find the secret flag
   - [Start Challenge](challenge2.html)

3. **Hidden in Plain Sight** (Hard)
   - Uncover a hidden message in an image using steganography
   - [Start Challenge](challenge3.html)

## Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/mini-ctf-challenges.git
   cd mini-ctf-challenges
   ```

2. Install the required Python packages (for generating the steganography image):
   ```bash
   pip install pillow numpy
   ```

3. Generate the steganography image for Challenge 3:
   ```bash
   python generate_image.py
   ```

4. Open `index.html` in your web browser to start the challenges.

## Flag Format

All flags follow this format: `CTF{example_flag_here}`

## Solutions

If you get stuck, you can find hints within each challenge. The solutions are also available in the source code of each challenge page.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Created for educational purposes
- Inspired by various CTF challenges
- Uses standard web technologies (HTML, CSS, JavaScript)