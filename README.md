# Nexus
### A behaviour tree based personal assistant

## Requirements:
* For the wake-word functionality to work you must have a valid [PicoVoice](https://picovoice.ai/) account and access token. 
* A working microphone connected to the PC

## Usage:
- The program works in a virtual environment so it must be enabled using the Activate script.
```bash
> Scripts\Activate
> python main.py
```

## Features:
- Interconversion of physical quantities in different systems.
- Automatic detection of dimensional errors
- Basic mathematical evaluations
- You can hardcode custom commands in the return statement of `eval_code.py` to speed up testing
- Logging administrative commands
- Permission checking system

### *Try*:
- "Nexus, what is 2 raised to 10"
- "Nexus, convert 5 nanometers to kilometers"
- "Nexus, convert 15 weeks to years"
