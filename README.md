# Programming Code Project - Lexical & Syntax Analysis

## Project Overview
This project is designed for Programming Code exercises focusing on Lexical Analysis and Syntax Analysis.

## Usage Instructions

### 1. Modify Source Code
Students need to modify the source code in the `HLang.g4` file according to the requirements of each specific exercise.

### 2. Generate Build Files
Use the following command to generate the build files:
```bash
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -no-listener -o build HLang.g4
```

### 3. Submit Assignment
After running the build command, students should:
- Copy all files from the `build/` directory
- Upload these files to the LMS assignment submission section

## Project Structure
- `HLang.g4` - Main grammar file to be modified for exercises
- `antlr-4.13.2-complete.jar` - ANTLR tool for generating lexer and parser
- `build/` - Generated files directory (created after running build command)

## Dependencies
- Java Runtime Environment (JRE) for running ANTLR
- ANTLR 4.13.2 complete package
# Exercise-PPL
