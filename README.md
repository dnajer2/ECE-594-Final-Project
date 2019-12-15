# ECE-594-Final-Project
An attempt to perform an acoustic based side channel attack on keyboards without physically needing to interact with the target keyboard.

Steps:
1. Record target keyboard sounds
2. Using Audacity, isolate every keystroke sound and save as a .wav file.
2.1 Save every audio file as xn.wav where n is the nth keystroke recorded
3. Run the Matlab/Octave script, adjusting the loop to read in your audio diles
4. Review the generated "Character Spikes" text file.
5. Run Frequency Analysis Helper v1 (freq.py) script
6. Use Frequency Analysis Helper v1 to try to decipher the recorded text.
