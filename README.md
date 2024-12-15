# CNC GCODE Compiler  

**Author:** Oscar Lopez  
**Repository:** [CNC_GCODE_COMPILER](https://github.com/oscar-dev19/CNC_GCODE_COMPILER)  

## Overview  
The **CNC GCODE Compiler** is a Python-based tool designed to simplify the process of generating G-code for CNC machines. This project focuses on converting user-defined inputs into machine-readable G-code, offering a streamlined solution for CNC programming and automation.  

## Features  
- **User-Friendly Input Format:** Easily define machining operations with intuitive configuration.  
- **Customizable Outputs:** Generate G-code tailored to specific CNC machines and controllers.  
- **Error Checking:** Identify and handle common programming mistakes to ensure safe and precise machining.  
- **Extensible Design:** Modify or expand the functionality to meet diverse manufacturing needs.  

## Requirements  
- Python 3.8 or higher
- Java jdk: for antlr framework to work.
- Required dependencies are listed in `requirements.txt`  

## Installation  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/oscar-dev19/CNC_GCODE_COMPILER.git  
2. Navigate to the project Directory
   ```bash
   cd CNC_GCODE_COMPILER  
3. Install dependencies:
   ```bash
   pip install -r requirements.txt  

## Usage
  1.Define the input parameters a .g4 file

  2. run the compiler
     ```bash
     python copile.py

## Project Structure
  - compile.py: The python compiler that interprets the commands in the g4 file.
  - gCode.g4: The file with all cnc instructions.




