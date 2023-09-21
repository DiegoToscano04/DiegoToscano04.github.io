<p align="center">  Elaboración Proyecto 3 Lógica Secuencial</p>

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

### Desarrollo Proyecto 2:

###### La pieza central de la arquitectura del ordenador es la CPU, o Unidad Central de Procesamiento, y la pieza central computacional de la CPU es la ALU, o Unidad Aritmético-Lógica. En este proyecto el propósito es construir gradualmente un conjunto de chips que realizan sumas aritméticas, culminando con la construcción de una ALU: el chip ALU del ordenador Hack. Todos los chips construidos en este proyecto van a ser estandares, excepto la ALU, que varía de una arquitectura de ordenador a otra.


## Objetivo

#### Construir los siguientes chips:
##### DFF (given)
##### Bit
##### Register
##### RAM8
##### RAM64
##### RAM512
##### RAM4K
##### RAM16K
##### PC
------------

<h3 align="center">DFF (given)</h3>

###### El DFF o Data flip-flop e una variante del elemento secuencial más elemental del ordenador, el flip-flop. Un DFF posee una interfaz que tiene dos entradas de datos de un bit y una salida de datos de un bit, también posee una entra da reloj que cambia según la señal del reloj maestro.

###### Es decir que las entradas de datos y las entradas de reloj en conjunto permiten a un DFF implementar el comportamiento llamado: comportamiento out(t)=in(t-1) donde in y out son los valores de entrada y salida de la compuerta y t es el ciclo del reloj actual. En resumen, el DFF emite el valor de entrada de la unidad de tiempo anterior.

<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/e7ea697a-831d-48e9-8150-9931ec89ab2d" /></p>
<p align="center"> Fuente: https://www.nand2tetris.org/_files/ugd/44046b_862828b3a3464a809cda6f44d9ad2ec9.pdf</p>

<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/6074bcc0-8abf-432f-bf34-193e07264d15" /></p>
<p align="center"> Fuente:https://www.nand2tetris.org/_files/ugd/44046b_862828b3a3464a809cda6f44d9ad2ec9.pdf</p>


-----------------

<h3 align="center">Bit</h3>

##### El bit o celda binaria está diseñado para almacenar un solo bit de información, es decir 0 o 1- La interfaz del chip consta de un pin de entrada que transporta un bit de datos. Posee un bit, un pin de carga que habilita la celda para escrituras y un pin de salida que emite el estado actual de la celda. 

<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/4a9073e9-7c6f-4f0f-88af-639db5910a9d"/></p>
<p align="center">Fuente: https://www.nand2tetris.org/_files/ugd/44046b_862828b3a3464a809cda6f44d9ad2ec9.pdf </p>

<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/f5daebbc-329e-4b82-bd18-b33ee2a15f62"/></p>
<p align="center">Fuente: https://www.nand2tetris.org/_files/ugd/44046b_862828b3a3464a809cda6f44d9ad2ec9.pdf</p>


    CHIP Bit {
    IN in, load;
    OUT out;

    PARTS:
    Mux(a=aux,b=in,sel=load,out=out1);
    DFF(in=out1,out=out,out=aux);
    }


-----------------

<h3 align="center">Register</h3>

#####  Un register es un dispositivo de almacenamiento que puede “almacenar” o “recordar” un valor a lo largo del tiempo, implementando el comportamiento clásico del almacenamiento out(t)=out (t-1) a lo largo del tiempo. Sin embargo, un DFF únicamente puede implementar su entrada anterior, es decir, out(t)=in(t-1), lo cual nos indica que un registro puede implementarse a partir de un DFF simplemente retroalimentando la salida de este último a su entrada, permitiendo que en el tiempo t en cualquier momento sea un eco la salida en el tiempo t-1, permitiendo la funcionalidad de una unidad de almacenamiento.

##### La Application Programming Interface (API) del chip register es esencialmente la misma que la del chip-bit, a diferencia que los pines de entrada y salida de este dispositivo están diseñados para manejar valores de varios bits.


<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/0a59bd08-487a-4cd2-9108-9992d54ddaa6"/></p>
<p align="center">fuente:https://www.nand2tetris.org/_files/ugd/44046b_862828b3a3464a809cda6f44d9ad2ec9.pdf</p>

<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/0e539f25-f332-4ba9-a477-6f28618a8444"/></p>
<p align="center">fuente:https://www.nand2tetris.org/_files/ugd/44046b_862828b3a3464a809cda6f44d9ad2ec9.pdf</p>

    CHIP Register {
    IN in[16], load;
    OUT out[16];

    PARTS:
    Bit(in=in[0], load=load, out=out[0]);
    Bit(in=in[1], load=load, out=out[1]);
    Bit(in=in[2], load=load, out=out[2]);
    Bit(in=in[3], load=load, out=out[3]);
    Bit(in=in[4], load=load, out=out[4]);
    Bit(in=in[5], load=load, out=out[5]);
    Bit(in=in[6], load=load, out=out[6]);
    Bit(in=in[7], load=load, out=out[7]);
    Bit(in=in[8], load=load, out=out[8]);
    Bit(in=in[9], load=load, out=out[9]);
    Bit(in=in[10], load=load, out=out[10]);
    Bit(in=in[11], load=load, out=out[11]);
    Bit(in=in[12], load=load, out=out[12]);
    Bit(in=in[13], load=load, out=out[13]);
    Bit(in=in[14], load=load, out=out[14]);
    Bit(in=in[15], load=load, out=out[15]);
    }

    
###### Ambos chips, bit y register tienen el mismo comportamiento de lectura y escritura:

###### Lectura: Para leer el contenido de un registro, simplemente sondeamos su salida.
###### Escritura: Para escribir un nuevo valor de datos d en un registro, ponemos d en la entrada in y  la entrada load. En el siguiente ciclo de reloj el registro se compromete con el valor de datos nuevos y salida empieza a emitir d.

-----------------


<h3 align="center">Compuerta Inc16</h3>

##### El chip inc16 es un tipo especial de sumador el cual se encarga de incrementar una entrada de 16 bits en 1 y utilizando el chip Add16 implementado anteriormente es posible construir el inc16.

<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/4fc8ed2c-eecd-4e03-a44e-56e959f738ad" width="250" height="200"/></p>
<p align="center">Fuente: https://gittest2121.gitbook.io/nand2tetris/combinational-chips/inc16-chip</p>

    CHIP Inc16 {
    IN in[16];
    OUT out[16];

    PARTS:
    Add16(a=in,b[0]=true,out=out);
    }

-----------------
<h3 align="center">RAM8</h3>

##### para implementar una RAM8, se alinean ocho registros. A continuación, se construye una lógica combinacional que, dado un valor de dirección, carga la entrada de la RAM8 en el registro seleccionado. De forma similar, se construye otra lógica combinacional que, dado un valor de dirección, selecciona el registro correcto y envía su valor de salida a la salida de la RAM8.

<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/e4786315-0cf0-45b8-bdf4-ac64525ce8cd" width="250" height="200"/></p>
<p align="center">Fuente: https://gittest2121.gitbook.io/nand2tetris/combinational-chips/inc16-chip</p>

•	Multiplexor de 8 vías: El multiplexor de 8 vías (DMux8Way) se utiliza para seleccionar uno de los ocho registros, en función de las líneas de dirección.
•	Registros: Los ocho registros se implementan utilizando el componente Register.
•	Multiplexor de 8 vías y 16 bits: El multiplexor de 8 vías y 16 bits (Mux8Way16) se utiliza para seleccionar uno de los ocho registros seleccionados por el multiplexor de 8 vías, en función de las líneas de dirección.

    CHIP RAM8 {
    IN in[16], load, address[3];
    OUT out[16];

    PARTS:
    DMux8Way(in=load, sel=address, a=a,b=b,c=c,d=d,e=e,f=f,g=g,h=h);    
    Register(in=in,load=a,out=Register1);
    Register(in=in,load=b,out=Register2);
    Register(in=in,load=c,out=Register3);
    Register(in=in,load=d,out=Register4);
    Register(in=in,load=e,out=Register5);
    Register(in=in,load=f,out=Register6);
    Register(in=in,load=g,out=Register7);
    Register(in=in,load=h,out=Register8);
    
    Mux8Way16(a=Register1,b=Register2,c=Register3,d=Register4,e=Register5,f=Register6,g=Register7,h=Register8, sel=address,out=out);
    
    }

  -----------------
