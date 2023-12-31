# This was created with Google Bard given the Professor Messer CompTIA A+ 220-1101 1.1 Laptop Hardware Youtube Video url: https://www.youtube.com/watch?v=y7oHZ1mi7e4

import random

# Create a word bank

word_bank = [
    # General nouns
   "keyboard", "display", "battery", "lithium-ion battery", "lithium-ion polymer battery", "memory", "sodimm", 
   "solid state drive (SSD)", "hard drive", "SATA", "m.2 interface", "chassis", "touchpad", "trackpad", "webcam",
   "microphone", "speakers", "headphone jack", "USB ports", "Thunderbolt ports", "HDMI port", "Ethernet port", 
   "SD card reader", "optical drive", "stylus",

   # Display nouns
   "resolution", "aspect ratio", "refresh rate", "touch screen", "brightness", "contrast", "color gamut", 
   "viewing angles",

   # Battery nouns
   "capacity", "lifespan", "charging time", "quick charging", "battery health",

   # Memory nouns
   "RAM", "DDR4", "DDR5", "capacity", "speed", "channels",

   # Storage nouns
   "hard drive capacity", "SSD capacity", "NVMe", "SATA", "read speed", "write speed",

   # Operating system nouns
   "Windows", "macOS", "ChromeOS", "Linux", "updates", "security patches",

   # Software nouns
   "pre-installed software", "bloatware", "drivers", "firmware", "updates"
   
   ]

# Randomly choose a word from word_bank

random_word = random.choice(word_bank)

print (random_word)
