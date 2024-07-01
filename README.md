# CNC G-Code Compiler Documentation
---
[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)

Author(s):
  * Oscar Lopez
  
Contributor(s):
  * Oscar Lopez

## Table of Contents
- [Overview](#overview)
- [Grammar Definition (`gcode.g4`)](#grammar-definition-gcodeg4)
  - [Rules](#rules)
  - [Tokens](#tokens)
- [Visitor Implementation (`gcodeVisitor.py`)](#visitor-implementation-gcodevisitorpy)
  - [Classes and Methods](#classes-and-methods)
  - [Example Implementations](#example-implementations)
    - [visitDrawlineExpr](#visitdrawlineexpr)
    - [visitLinInterpolateExpr](#visitlininterpolateexpr)
- [Installation](#installation)
- [Contributing](#contributing)
- [Issues](#issues)

## Overview

This CNC G-Code Compiler project uses ANTLR and Python to parse and execute standard CNC G-codes. It supports commands for drawing lines, linear interpolation, circular interpolation, drawing arcs, and dwelling. The lexer and parser are defined in `gcode.g4`, and the visitor implementation is provided in `gcodeVisitor.py`.

## Grammar Definition (`gcode.g4`)

The G-code grammar is defined in `gcode.g4` and includes the following rules:

### Rules

- **start**: Entry point for parsing.
- **expr**: Expressions that represent different G-code commands.
  - **drawlineExpr**: Command `G00` for drawing a line with optional speed and color.
  - **linInterpolateExpr**: Command `G01` for linear interpolation.
  - **circularInterpolateExpr**: Command `G02` for circular interpolation.
  - **drawarcExpr**: Command `G03` for drawing arcs with optional speed and color.
  - **dwellExpr**: Command `G04` for dwelling (pausing).

### Tokens

- **NUMBER**: Numeric values, optionally with a decimal point.
- **COLORS**: Predefined colors: `blue`, `red`, `green`, `pink`, `yellow`, `purple`.
- **WS**: Whitespace (ignored).

## Visitor Implementation (`gcodeVisitor.py`)

The `gcodeVisitor.py` file defines the visitor that executes the parsed G-code commands using the `turtle` module.

### Classes and Methods

- **gcodeVisitor**: Inherits from `ParseTreeVisitor` and provides methods to visit each type of expression.
  - **visitStart**: Entry point for visiting nodes.
  - **visitDrawlineExpr**: Handles `G00` command to draw a line at maximum speed with optional color.
  - **visitLinInterpolateExpr**: Handles `G01` command for linear interpolation with optional speed.
  - **visitCircularInterpolateExpr**: Handles `G02` command for circular interpolation.
  - **visitDrawarcExpr**: Handles `G03` command for drawing arcs with optional speed and color.
  - **visitDwellExpr**: Handles `G04` command for dwelling.

### Example Implementations

#### visitDrawlineExpr
```python
def visitDrawlineExpr(self, ctx:gcodeParser.DrawlineExprContext):
    x_cord = int(ctx.x_cord.text)
    y_cord = int(ctx.y_cord.text)
    machinePointer.speed(10)  # G00 goes at max speed.

    if ctx.color:
        color = ctx.color.text
        machinePointer.color(color)

    machinePointer.pendown()
    machinePointer.goto(x_cord, y_cord)
    return self.visitChildren(ctx)
```

#### visitLinInterpolateExpr

```python
def visitLinInterpolateExpr(self, ctx:gcodeParser.LinInterpolateExprContext):
    x_cord = int(ctx.x_cord.text)
    y_cord = int(ctx.y_cord.text)

    if ctx.speed:
        speed = int(ctx.speed.text)
        machinePointer.speed(speed)

    machinePointer.penup()
    machinePointer.goto(x_cord, y_cord)
    return self.visitChildren(ctx)
```

### Installation
```python
import gcodeVisitor
from antlr4 import *

# Load your G-code file
input_stream = FileStream('path/to/your/gcode/file')

# Create a lexer and parser
lexer = gcodeLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = gcodeParser(stream)

# Parse the G-code
tree = parser.start()

# Create a visitor and visit the parse tree
visitor = gcodeVisitor()
visitor.visit(tree)
```

### Contributing

Contributions are welcome! To contribute:
  1. Fork the Rerpo
  2. create new branch
     ```bash
     git checkout -b feature-branch
     ```
  3. Commit yopur changes
     ```bash
     git commit -m 'Added new feature'
     ```
  4. Push to the branch
     ```bash
     git push origin feature-branch
     ```
  5. Open a pull request.
  6. Profit!

### Issues
If you encounter any issues, please create a new issue in the [Issue Tracker](https://github.com/oscar-dev19/CNC_GCODE_COMPILER/issues). Provide detailed information to helps me resolve the problem efficiently.

### License
This project is licensed under the MIT [License](https://opensource.org/license/mit). See the  file for details.


