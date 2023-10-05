<p align="center">  Elaboración Proyecto 2 Aritmética Booleana</p>

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


### Objetivo

##### Construir los siguientes chips:
###### HalfAdder
###### FullAdder
###### Add16
###### Inc16
###### ALU
------------

<h3 align="center">HalfAdder</h3>

###### Esta compuerta es un circuito lógico combinacional diseñado para sumar dos dígitos binarios. Este, proporciona una salida junto con un acarreo(si lo hay). Para su diseño, se  hace uso de una puerta Xor, la cual nos proporciona como salida la suma y una puerta And para la salida del Acarreo.

<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/8460345f-aef7-40e8-9d67-fa8ce555c7d5" /></p>
<p align="center"> Fuente:  https://www.geeksforgeeks.org/half-adder-in-digital-logic/</p>

-----------------

    CHIP HalfAdder {
    IN a, b;    // 1-bit inputs
    OUT sum,    // Right bit of a + b 
        carry;  // Left bit of a + b

    PARTS:
    Xor(a=a,b=b,out=sum);
    And(a=a,b=b,out=carry);
    }
--------------
<h3 align="center">FullAdder</h3>

##### Como en el caso del half-adder, el full-adder produce dos salidas, el bit menos significativo de la suma y el bit de acarreo. La memoria sumadora representa números enteros mediante patrones de n-bits, los cuales pueden ser 16,32 ,64, etc. 

##### El chip que se encarga de sumar dichos números se denomina sumador multibit o únicamente sumador.

<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/d21b5dcf-2dd7-476c-8d59-94302ff6c3f2"/></p>
<p align="center">Fuente: https://www.nand2tetris.org/_files/ugd/44046b_f0eaab042ba042dcb58f3e08b46bb4d7.pdf </p>

<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/c89a55b8-2f79-4984-8607-d772ef76025d"/></p>
<p align="center">Fuente: https://angelmicelti.github.io/4ESO/EDI/sumador_completo.html</p>


    CHIP FullAdder {
    IN a, b, c;  // 1-bit inputs
    OUT sum,     // Right bit of a + b + c
        carry;   // Left bit of a + b + c

    PARTS:
    HalfAdder(a=a,b=b,carry=carry1,sum=out1);
    HalfAdder(a=out1,b=c,carry=carry2,sum=sum);
    Or(a=carry1,b=carry2,out=carry);		
    }

-----------------
<h3 align="center">Add16</h3>

#####  para lograr un sumador de 16 bits, se puede conectar los sumadores en serie, de forma que desde el bit menos significativo hacia el más significativo, el acarreo de entrada del bit esté conectado al acarreo de salida del bit.

##### El primer bit se puede construir con un semisumador mientras que los demás bits requieren un sumador completo, se tiene un semi sumador de N bits. Pero si en el primer bit se utiliza un sumador completo, el circuito dispone además del acarreo de entrada Ci y se tiene un sumador completo de N bits.


<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/e9393d28-4247-4b47-922d-dc64035f7dc7"/></p>
<p align="center">fuente: http://codigoelectronica.com/blog/compuerta-or](https://www.studocu.com/es-mx/document/universidad-panamericana-mexico/sistemas-de-informacion/sumador-16-bits-nota-a/9517248
https://youtu.be/81SrA0qSA98</p>

    CHIP Add16 {
    IN a[16], b[16];
    OUT out[16];

    PARTS:
    HalfAdder(a=a[0],b=b[0],carry=carry1,sum=out[0]);
    FullAdder(a=a[1],b=b[1],c=carry1,carry=carry2,sum=out[1]);
    FullAdder(a=a[2],b=b[2],c=carry2,carry=carry3,sum=out[2]);
    FullAdder(a=a[3],b=b[3],c=carry3,carry=carry4,sum=out[3]);
    FullAdder(a=a[4],b=b[4],c=carry4,carry=carry5,sum=out[4]);
    FullAdder(a=a[5],b=b[5],c=carry5,carry=carry6,sum=out[5]);
    FullAdder(a=a[6],b=b[6],c=carry6,carry=carry7,sum=out[6]);
    FullAdder(a=a[7],b=b[7],c=carry7,carry=carry8,sum=out[7]);
    FullAdder(a=a[8],b=b[8],c=carry8,carry=carry9,sum=out[8]);
    FullAdder(a=a[9],b=b[9],c=carry9,carry=carry10,sum=out[9]);
    FullAdder(a=a[10],b=b[10],c=carry10,carry=carry11,sum=out[10]);
    FullAdder(a=a[11],b=b[11],c=carry11,carry=carry12,sum=out[11]);
    FullAdder(a=a[12],b=b[12],c=carry12,carry=carry13,sum=out[12]);
    FullAdder(a=a[13],b=b[13],c=carry13,carry=carry14,sum=out[13]);
    FullAdder(a=a[14],b=b[14],c=carry14,carry=carry15,sum=out[14]);
    FullAdder(a=a[15],b=b[15],c=carry15,carry=carry16,sum=out[15]);
    }
        
-----------------
<h3 align="center">Inc16</h3>

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
<h3 align="center">ALU (ARITHMETIC LOGIC UNIT)</h3>

##### Es la parte fundamental de la GPU de la computadora, siendo capaz de realizar operaciones lógicas y aritméticas dependiendo de las entradas que se le den, de igual forma, es capaz de realizar operaciones para confirmar si un numero es negativo o igual a cero (zr y ng respectivamente).

<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/ee03edd1-3f17-4013-9cdf-f2a9acc866ad" width="250" height="200"/></p>
<p align="center">Fuente: Fuente: Chapter 2 NandtoTetris</p>

##### Como se puede apreciar en la figura, las entradas a la ALU son 8 en total, sus salidas son 3, de las cuales f(x,y), es la operación realizada a partir de la secuencia ingresada.
##### Ahora bien, es importante señalar que la implementación de nuestra ALU cuenta con la reutilización de compuertas creadas en este y en el proyecto antecesor.
##### De igual manera, es de destacar la tabla de verdad de la ALU, donde la secuencia de entrada, que va de zx…no, son las instrucciones de funcionamiento de la unidad, en donde cada una, tiene un papel especifico, como se ve en el encabezado de cada columna de la tabla, y por consiguiente, la salida, se obtiene una expresión por tal cadena.

<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/e0fcf1a7-f657-4391-b99a-62f7d3314ad2" width="250" height="200"/></p>
<p align="center">Fuente: Chapter 2 NandtoTetris</p>

     CHIP ALU {
     IN  
     x[16], y[16],  // 16-bit inputs        
     zx, // zero the x input?
     nx, // negate the x input?
     zy, // zero the y input?
     ny, // negate the y input?
     f,  // compute out = x + y (if 1) or x & y (if 0)
     no; // negate the out output?
     
     OUT 
     out[16], // 16-bit output
     zr, // 1 if (out == 0), 0 otherwise
     ng; // 1 if (out < 0),  0 otherwise

    PARTS:    
    Mux16(a=x,b[0..15]=false,sel=zx,out=aux);    
    Not16(in=aux,out=notx);
    Mux16(a=aux,b=notx,sel=nx,out=newx);
    Mux16(a=y,b[0..15]=false,sel=zy,out=aux1);    
    Not16(in=aux1,out=noty);
    Mux16(a=aux1,b=noty,sel=ny,out=newy);
    Add16(a=newx,b=newy,out=aux2);
    And16(a=newx,b=newy,out=aux3);
    Mux16(a=aux3,b=aux2,sel=f,out=out1);
    Not16(in=out1,out=out2);
    Mux16(a=out1,b=out2,sel=no,out=out3,out[0..7]=out4,out[8..15]=out5);

    Or8Way(in=out4,out=out6);
    Or8Way(in=out5,out=out7);
    Or(a=out6,b=out7,out=out8);
    Not(in=out8,out=zr);

    And16(a=out3,b[0..15]=true,out[15]=ng);
    And16(a=out3,b[0..15]=true,out=out);    	
    }

   ##### Aquí tenemos un ejemplo del funcionamiento de nuestra ALU, en la parte izquierda, contamos con la secuencia de variables necesarias para la operación que se desea realizar y en la parte derecha nuestras salidas, de tal manera, queda comprobada la tabla de verdad, y los indicadores de salida de nuestro chip.

<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/f1be1d74-2eb4-4fa7-8c9a-28af6230b38b" width="250" height="200"/></p>
<p align="center">Fuente: Fuente: Propiedad de los autores</p>

### Principales diferencias entre la lógica aritmética y la lógica secuencial.

##### Las principales diferencias, se encuentran en la naturaleza de cada ítem, por ejemplo, la lógica aritmética está más encargada de realizar alguna operación sin determinar la secuencialidad de la misma, solo depende de las entradas que tome para funcionar, por otro lado, la lógica secuencial, sí se ve afectada por el orden de los datos, realizando operaciones de almacenamiento y de flujo de operaciones, por otro lado, los datos usados por la lógica secuencial, son una combinatoria de datos numéricos, datos lógicos y señales de control. Por otro lado, la función de retroalimentación de la salida de cada lógica es exclusiva en este caso de la lógica secuencial dado que su arquitectura tiene la capacidad de almacenar estados anteriores que influyen en las entradas futuras. Dicho esto, se debe tener en cuenta el fin que tiene cada lógica, haciendo a la aritmética más enfocada en los sistemas que requieran cálculos de tipo numérico y en contraste, a la secuencial en sistemas de control, maquinas o en general cosas que requieran almacenar y retener estados anteriores.
  -----------------
