# CNC GCode Compiler (Concept - Beta)

[![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)  
[![Status](https://img.shields.io/badge/status-Beta-orange)](#)  
[![Issues](https://img.shields.io/github/issues/oscar-dev19/cnc_gcode_compiler)](https://github.com/oscar-dev19/cnc_gcode_compiler/issues)  

## Overview  

**CNC GCode Compiler** is a **conceptual compiler** that simulates the behavior of a CNC machine using Python's `turtle` package. The project is designed to help visualize the execution of GCode commands in a virtual environment, making it an excellent tool for educational purposes, prototyping, and debugging.  

⚠️ **Note**: This project is a proof of concept and currently in **beta**. Future iterations may expand its functionality to support direct integration with CNC hardware.  

---

## Features  

- **GCode Simulation**: Executes GCode commands in a 2D simulation using Python's `turtle` module.  
- **Syntax Validation**: Ensures compatibility with standard GCode formats.  
- **Environment Visualization**: Provides a clear visual representation of toolpaths.  
- **Prebuilt Environment**: A ready-to-use Conda environment is included for seamless setup.  

---

## Installation  

### Prerequisites  
- Conda (Anaconda or Miniconda)  

### Steps  

1. Clone the repository:  
   ```bash
   git clone https://github.com/oscar-dev19/cnc_gcode_compiler.git
   cd cnc_gcode_comp

2. Load prebuilt conda environment:
   ```bash
   conda env create -f env/environment.yml
   conda activate cnc_gcode_compiler

3. 

