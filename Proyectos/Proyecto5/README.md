<p align="center">  Elaboración Proyecto 5 Computer Architecture</p>

<h4 align="center">  ARQUITECTURA DE COMPUTADORES A2 </h4>


<p align="center">  WEB GRUPO ALPHA:
https://diegotoscano04.github.io/  </p>
<p align="center"> <img src= "https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/4f2cd469-f8a6-482a-8f92-33960615841e"> </p>

------------

# Aprendizaje herramienta The Nand to Tetris

## Software:
###### El paquete de software Nand to Tetris contiene todas las herramientas y archivos necesarios para completar todos los proyectos descritos en este sitio y en el libro "The Elements of Computing Systems".

## Descarga:
###### Se descarga el programa Nand2Tetris de la página web: https://www.nand2tetris.org/software
###### Una vez descargados los archivos quedará una carpeta con el nombre de `nand2tetris` con 2 subcarpetas denominadas `projects` y `tools`.
![image](https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/d058171f-9976-4289-bb46-fc4ff46c9729) ![image](https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/417ef519-6948-40a5-9c36-775b71ab4c82)

## Información sobre los archivos:
###### En la carpeta `projects` estarán los proyectos del 1 al 13 los cuales son archivos que deben modificarse para completar las prácticas mientras se trabaja en varios proyectos de nand2tetris.
###### En la carpeta `tools` estarán las herramientas del software nand2tetris.

## Uso del Hardware Simulator 2.5
<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/ebe3caf7-7622-4420-8b3b-120ec046a87e" width="500" height="300" /></p>
<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/f3fbf4f2-1dcb-483f-a408-c2b43c77ea67" /></p>

<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/55cdd5ce-dbdd-4ba1-a5f3-e75040635ca5" width="500" height="300" /></p>
<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/f3fbf4f2-1dcb-483f-a408-c2b43c77ea67" /></p>

<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/673b1925-adb1-4637-9107-0888487ac3a2" width="500" height="300" /></p>
<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/f3fbf4f2-1dcb-483f-a408-c2b43c77ea67" /></p>

##### En la parte final de cada evaluación para cada una de las compuertas podemos corroborar con un mensaje de :`Comparison ended successfuly` si realizamos la actividad de manera satisfactoria.

### Desarrollo Proyecto 5:

###### En este proyecto se integrarán los dispositivos ALU y RAM construidos en los proyectos 2 y 3 en un sistema informático capaz de ejecutar programas escritos en el lenguaje máquina introducido en el proyecto 4. El propósito es construir una plataforma hardware capaz de ejecutar programas escritos en el lenguaje máquina Hack y a su vez demuostrar el funcionamiento de la plataforma haciendo que el Chip ejecute correctamente los tres programas de prueba.


### Objetivo

##### Construir los siguientes chips:
###### Memory
###### CPU
###### Computer

------------

<h3 align="center">Memory</h3>

###### La memoria en una computadora es un componente crucial que sirve para almacenar datos e instrucciones temporales o permanentes. Los diferentes tipos de memoria, como la RAM, la ROM y la memoria de almacenamiento secundario, desempeñan roles específicos en el funcionamiento de la computadora, asegurando un rendimiento eficiente y la capacidad de almacenar información de manera confiable. Este chip memory, está compuesto esencialmente de una fusión de otros tres chips de niveles inferiores: RAM16K, pantalla, teclado. Aunque estos están ya incorporados por lo que no hay necesidad de construirlos. Además también cuenta con las compuertas: DMux4Way, Mux4Way16 y or.

<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/b77825c7-3bfc-4943-a895-cbd09060322d" /></p>
<p align="center"> Fuente: https://www.nand2tetris.org/_files/ugd/44046b_b2cad2eea33847869b86c541683551a7.pdf/</p>

##### Implementación del código:
-----------------
  
    CHIP Memory {
    IN in[16], load, address[15];
    OUT out[16];

    PARTS:
    DMux4Way(in=true, sel=address[13..14], a=a,b=b,c=c,d=d);
    Or(a=a,b=b,out=ram);
    And(a=load,b=ram, out=loadram);
    RAM16K(in=in, load=loadram, address=address[0..13], out=out1);
    And(a=c,b=load,out=loadscreen);
    Screen(in=in, load=loadscreen, address=address[0..12], out=out2);
    Keyboard(out=keyboard);
    Mux4Way16(a=out1,b=out1,c=out2,d=keyboard,sel=address[13..14], out=out);
    }

--------------

##### Resultados obtenidos:

<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/64a9a6fa-dd92-43dc-8b77-a26cb5ccf503" width="500" height="350"/></p>
<p align="center"> Fuente: https://www.nand2tetris.org/_files/ugd/44046b_b2cad2eea33847869b86c541683551a7.pdf</p>

----------------


<h3 align="center">CPU (Central Processing Unit)</h3>

###### La CPU es el cerebro de una computadora, un componente microelectrónico que realiza una variedad de operaciones aritméticas, lógicas y de control que ejecuta instrucciones escritas en el lenguaje HACK.. Las tareas típicas que realiza una CPU incluyen la carga de datos desde la memoria principal, la realización de cálculos, la toma de decisiones lógicas y la devolución de resultados. La CPU está compuesta por varias unidades y componentes clave:

###### Unidad de Control (CU): La CU es responsable de controlar y coordinar las operaciones de la CPU. Supervisa la secuencia de ejecución de instrucciones y garantiza que se realicen en el orden correcto. También interpreta y decodifica las instrucciones antes de ejecutarlas.

###### Unidad Aritmético Lógica (ALU): La ALU es la parte de la CPU que realiza operaciones aritméticas (como sumas y restas) y operaciones lógicas (como comparaciones). Es fundamental para la realización de cálculos y toma de decisiones.

###### Registros: Los registros son pequeñas unidades de almacenamiento de alta velocidad dentro de la CPU. Se utilizan para almacenar datos temporales y resultados intermedios durante el procesamiento de instrucciones.

<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/898a8287-aeaa-4ed1-a6dd-d084a4571c98" /></p>
<p align="center">Fuente: https://www.nand2tetris.org/_files/ugd/44046b_b2cad2eea33847869b86c541683551a7.pdf </p>

##### Implementación del código:

-----------------------

    CHIP CPU {

    IN  inM[16],         // M value input  (M = contents of RAM[A])
        instruction[16], // Instruction for execution
        reset;           // Signals whether to re-start the current
                         // program (reset==1) or continue executing
                         // the current program (reset==0).

    OUT outM[16],        // M value output
        writeM,          // Write to M? 
        addressM[15],    // Address in data memory (of M)
        pc[15];          // address of next instruction

    PARTS:
    Not(in=instruction[15],out=opbit);
    Mux16(a=instruction,b=OutALU,sel=instruction[15],out=out1);
    Or(a=opbit,b=instruction[5],out=out2);
    ARegister(in=out1,load=out2,out=Aregister);
    And(a=instruction[15],b=instruction[4],out=out3);
    DRegister(in=OutALU,load=out3,out=Dregister);
    And(a=instruction[15],b=instruction[3],out=writeM);    
    And(a=instruction[15],b=instruction[12],out=out4);
    Mux16(a=Aregister,b=inM,sel=out4,out=out5);
    And16(a=Aregister,b=true,out[0..14]=addressM);
    ALU(x=Dregister,y=out5,zx=instruction[11],nx=instruction[10],zy=instruction[9],ny=instruction[8],f=instruction[7],no=instruction[6],out=outM, out=OutALU, zr=zr,ng=ng);
    
    Not(in=zr,out=notzr);
    Not(in=ng,out=notng);
    And(a=zr,b=instruction[1],out=aux);
    And(a=ng,b=instruction[2],out=aux2);
    And(a=notzr,b=notng,out=aux3);
    And(a=aux3,b=instruction[0],out=aux4);
    Or(a=aux,b=aux2,out=aux5);
    Or(a=aux5,b=aux4,out=aux6);
    And(a=instruction[15],b=aux6,out=jump);
    Not(in=jump,out=notjump);
    
    PC(in=Aregister,load=jump,inc=notjump,reset=reset,out[0..14]=pc);
    }

-----------------

##### Resultados obtenidos:


<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/669cc3f0-abfe-408c-9368-61e0e91faabc" width="500" height="350"/></p>
<p align="center">Fuente: https://www.nand2tetris.org/_files/ugd/44046b_b2cad2eea33847869b86c541683551a7.pdf </p>

<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/7439642c-80cd-457e-a5cc-fa2ffb2da639" width="500" height="350"/></p>
<p align="center">Fuente: https://www.nand2tetris.org/_files/ugd/44046b_b2cad2eea33847869b86c541683551a7.pdf </p>


-----------------

<h3 align="center">Computer</h3>

##### Es Una máquina de 16 bits que consta de los siguientes elementos:

<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/89c00b67-c407-4750-8d6d-6d9902fe336d" width="500" height="350"/></p>
<p align="center">Fuente: https://www.nand2tetris.org/_files/ugd/44046b_b2cad2eea33847869b86c541683551a7.pdf </p>

##### Ambos chips de memoria tienen una anchura de 16 bits y un espacio de direcciones de 15 bits.
##### Una vez que la CPU y los chips de memoria se han implementado y probado, la construcción del ordenador en su conjunto es sencilla.

##### Implementación del código:

------------

    CHIP Computer {
    IN reset;
    PARTS:  CPU(inM=outMemory,instruction=outROM32K,reset=reset,writeM=writeM,outM=outM,addressM=addressM,pc=pc);
    ROM32K(address=pc,out=outROM32K);
    Memory(load=writeM,in=outM,address=addressM,out=outMemory);    
    }

----------------

##### Resultados obtenidos:

<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/34761f01-3be7-4666-b8f4-1dd0b480e070" width="500" height="350"/></p>
<p align="center">Fuente: https://www.nand2tetris.org/_files/ugd/44046b_b2cad2eea33847869b86c541683551a7.pdf </p>


  -----------------
