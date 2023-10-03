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

### Desarrollo Proyecto 3:

##### La memoria principal del ordenador, también llamada memoria de acceso aleatorio, o RAM, es una secuencia direccionable de registros, cada uno diseñado para contener un valor de n bits. En este proyecto se construirá gradualmente una unidad RAM. Esto implica dos cuestiones principales: (i) utilizar la lógica de compuertas para almacenar bits de forma persistente, a lo largo del tiempo, y (ii) utilizar la lógica de compuertas para localizar ("direccionar") el registro de memoria sobre el que deseamos operar.


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

##### El DFF o Data flip-flop e una variante del elemento secuencial más elemental del ordenador, el flip-flop. Un DFF posee una interfaz que tiene dos entradas de datos de un bit y una salida de datos de un bit, también posee una entra da reloj que cambia según la señal del reloj maestro.

##### Es decir que las entradas de datos y las entradas de reloj en conjunto permiten a un DFF implementar el comportamiento llamado: comportamiento out(t)=in(t-1) donde in y out son los valores de entrada y salida de la compuerta y t es el ciclo del reloj actual. En resumen, el DFF emite el valor de entrada de la unidad de tiempo anterior.

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


<h3 align="center">RAM8</h3>

##### Para implementar una RAM8, se alinean ocho registros. A continuación, se construye una lógica combinacional que, dado un valor de dirección, carga la entrada de la RAM8 en el registro seleccionado. De forma similar, se construye otra lógica combinacional que, dado un valor de dirección, selecciona el registro correcto y envía su valor de salida a la salida de la RAM8.

<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/e4786315-0cf0-45b8-bdf4-ac64525ce8cd"/></p>
<p align="center">Fuente: https://gittest2121.gitbook.io/nand2tetris/combinational-chips/inc16-chip</p>

-	##### Multiplexor de 8 vías: El multiplexor de 8 vías (DMux8Way) se utiliza para seleccionar uno de los ocho registros, en función de las líneas de dirección.
-	##### Registros: Los ocho registros se implementan utilizando el componente Register.
-	##### Multiplexor de 8 vías y 16 bits: El multiplexor de 8 vías y 16 bits (Mux8Way16) se utiliza para seleccionar uno de los ocho registros seleccionados por el multiplexor de 8 vías, en función de las líneas de dirección.


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
<h3 align="center">RAM64</h3>

##### Es una memoria que puede almacenar 64 registros de 16 bits cada uno. Cada registro se identifica por un número de registro de 6 bits, de 0 a 63. Entonces, 64reg/8reg = 8. Por lo tanto, se necesitan 8 RAMs de 8 registros para hacer una RAM de 64 registros.

<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/8bed3125-004b-4af9-9f83-85d6abf556be"/></p>
<p align="center">Fuente: https://gittest2121.gitbook.io/nand2tetris/combinational-chips/inc16-chip</p>

-	##### El multiplexor de 8 vías (DMux8Way) se utiliza para seleccionar uno de los ocho registros, en función de las líneas de dirección [3 a 5].
-	##### Los ocho registros se implementan utilizando el componente RAM8.
-	##### El multiplexor de 8 vías y 16 bits (Mux8Way16) se utiliza para seleccionar uno de los ocho registros seleccionados por el multiplexor de 8 vías, en función de las líneas de dirección [3 a 5].

   CHIP RAM64 {
    IN in[16], load, address[6];
    OUT out[16];

    PARTS:
    DMux8Way(in=load,sel=address[3..5],a=a,b=b,c=c,d=d,e=e,f=f,g=g,h=h);
    RAM8(in=in,load=a,address=address[0..2],out=RAM81);
    RAM8(in=in,load=b,address=address[0..2],out=RAM82);
    RAM8(in=in,load=c,address=address[0..2],out=RAM83);
    RAM8(in=in,load=d,address=address[0..2],out=RAM84);
    RAM8(in=in,load=e,address=address[0..2],out=RAM85);
    RAM8(in=in,load=f,address=address[0..2],out=RAM86);
    RAM8(in=in,load=g,address=address[0..2],out=RAM87);
    RAM8(in=in,load=h,address=address[0..2],out=RAM88);
    Mux8Way16(a=RAM81,b=RAM82,c=RAM83,d=RAM84,e=RAM85,f=RAM86,g=RAM87,h=RAM88,sel=address[3..5],out=out);
}

  -----------------

  <h3 align="center">RAM512</h3>

##### Es una memoria que puede almacenar 512 registros de 16 bits cada uno. Cada registro se identifica por un número de registro de 9 bits, de 0 a 511. Entonces, 512reg/64reg = 8. Por lo tanto, se necesitan 8 RAMs de 64 registros para hacer una RAM de 512 registros.

-	##### El multiplexor de 16 vías (DMux16Way) se utiliza para seleccionar uno de los 16 registros, en función de las líneas de dirección [6 a 8].
-	##### Los 16 registros se implementan utilizando el componente RAM64.
-	##### El multiplexor de 8 vías y 16 bits (Mux8Way16) se utiliza para seleccionar uno de los 16 registros seleccionados por el multiplexor de 16 vías, en función de las líneas de dirección [6 a 8].


     	CHIP RAM512 {
        IN in[16], load, address[9];
        OUT out[16];

        PARTS:
        DMux8Way(in=load,sel=address[6..8],a=a,b=b,c=c,d=d,e=e,f=f,g=g,h=h);
        RAM64(in=in,load=a,address=address[0..5],out=RAM641);
        RAM64(in=in,load=b,address=address[0..5],out=RAM642);
        RAM64(in=in,load=c,address=address[0..5],out=RAM643);
        RAM64(in=in,load=d,address=address[0..5],out=RAM644);
        RAM64(in=in,load=e,address=address[0..5],out=RAM645);
        RAM64(in=in,load=f,address=address[0..5],out=RAM646);
        RAM64(in=in,load=g,address=address[0..5],out=RAM647);
        RAM64(in=in,load=h,address=address[0..5],out=RAM648);
        Mux8Way16(a=RAM641,b=RAM642,c=RAM643,d=RAM644,e=RAM645,f=RAM646,g=RAM647,h=RAM648,sel=address[6..8],out=out);
        }

  
------------------

  <h3 align="center">RAM4K</h3>

##### La RAM 4K se construye con una estructura semejante a la del chip anterior a diferencia que esta vez se aumenta la RAM de forma escalar. Ahora emplea una dirección de 12 bits para acceder en cada registro. Como se puede apreciar en la siguiente tabla. Entonces, 4096/512= 8, por lo que se necesitan 8 RAM de 512 registros para conseguir una RAM de 4k.

<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/247fed9f-806e-440e-91e8-48503706efe9""/></p>
<p align="center">Fuente: https://gittest2121.gitbook.io/nand2tetris/combinational-chips/inc16-chip</p>


    CHIP RAM4K {
    IN in[16], load, address[12];
    OUT out[16];

    PARTS:
    DMux8Way(in=load,sel=address[9..11],a=a,b=b,c=c,d=d,e=e,f=f,g=g,h=h);
    RAM512(in=in,load=a,address=address[0..8],out=RAM5121);
    RAM512(in=in,load=b,address=address[0..8],out=RAM5122);
    RAM512(in=in,load=c,address=address[0..8],out=RAM5123);
    RAM512(in=in,load=d,address=address[0..8],out=RAM5124);
    RAM512(in=in,load=e,address=address[0..8],out=RAM5125);
    RAM512(in=in,load=f,address=address[0..8],out=RAM5126);
    RAM512(in=in,load=g,address=address[0..8],out=RAM5127);
    RAM512(in=in,load=h,address=address[0..8],out=RAM5128);
    Mux8Way16(a=RAM5121,b=RAM5122,c=RAM5123,d=RAM5124,e=RAM5125,f=RAM5126,g=RAM5127,h=RAM5128,sel=address[9..11],out=out);
    }

-----------------

  <h3 align="center">RAM16K</h3>

##### La RAM 16K es una memoria con 16384 registros, cada uno de ellos de 16 bits cuenta con bus de direcciones de 14 bits. Para implementar el chip se utiliza un DMux4Way, 4 ram4k y un Mux4Way16. Entonces, 16384/4096=4, por lo que se necesitan 4 RAM de 4096 registros para conseguir la RAM 16k.

<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/878f56b7-bfd0-467c-a348-22872a21bbe5" /></p>
<p align="center">Fuente: https://gittest2121.gitbook.io/nand2tetris/combinational-chips/inc16-chip</p>


    CHIP RAM16K {
    IN in[16], load, address[14];
    OUT out[16];

    PARTS:
    DMux4Way(in=load,sel=address[12..13],a=a,b=b,c=c,d=d);
    RAM4K(in=in,load=a,address=address[0..11],out=RAM4K1);
    RAM4K(in=in,load=b,address=address[0..11],out=RAM4K2);
    RAM4K(in=in,load=c,address=address[0..11],out=RAM4K3);
    RAM4K(in=in,load=d,address=address[0..11],out=RAM4K4);    
    Mux4Way16(a=RAM4K1,b=RAM4K2,c=RAM4K3,d=RAM4K4,sel=address[12..13],out=out);
    }

--------------------

  <h3 align="center">PC: (Program Counter) </h3>

##### Es una de las unidades más importantes de la GPU, ya que ayuda a llevar una secuencia en las instrucciones que se deben tomar, indicando cual es la siguiente instrucción y en donde se encuentra. Ahora bien, la unidad consta de 16 bits, en este contador se utilizan buses de 16 bits, posee 2 bits de control, uno de ellos se encarga de definir la lectura de datos, y por su parte, el otro es uno de reinicio

<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/02981cb8-bca4-4bce-b5af-827326f450d2" /></p>
<p align="center">Fuente: https://gittest2121.gitbook.io/nand2tetris/combinational-chips/inc16-chip</p>


    CHIP PC {
    IN in[16],load,inc,reset;
    OUT out[16];

    PARTS:    
    Inc16(in=aux,out=out1);
    Mux16(a=aux,b=out1,sel=inc,out=out2);
    Mux16(a=out2,b=in,sel=load,out=out3);
    Mux16(a=out3,b[0..15]=false,sel=reset,out=out4);
    
    Register(in=out4,load=true,out=out,out=aux);
    }
    
------------------------
