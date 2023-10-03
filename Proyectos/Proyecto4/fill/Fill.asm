// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

(START)
@BLACKID
M=0

(LOOP)
@i
M=0

@KBD
D=M

@BLACK
D;JNE

@WHITE
0;JMP


(BLACK)
@BLACKID
D=M
@LOOP
D;JNE

@i
D=M
@SCREEN
A=A+D
M=-1
@i
M=M+1
D=M

@8192
D=A-D

@BLACK
D;JGT

@BLACKID
M=1

@LOOP
D;JEQ

(WHITE)
@BLACKID
D=M
@LOOP
D;JEQ

@i
D=M
@SCREEN
A=A+D
M=0
@i
M=M+1
D=M

@8192
D=A-D

@WHITE
D;JGT

@BLACKID
M=0

@LOOP
D;JEQ



