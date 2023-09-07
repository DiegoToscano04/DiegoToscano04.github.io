<p align="center">  Elaboración Proyecto 1 
Lógica Booleana</p>

------------

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

### Desarrollo de las compuertas: 
------------

<h3 align="center">Compuerta Not</h3>

###### Para generar la compuerta NOT a partir de la compuerta NAND es necesario aplicar una propiedad del algebra booleana a AND a = a, haciendo uso de lo anterior solo hace falta asignarle a la compuerta NAND el valor de a para sus dos entradas y así obtener la negación de a.

<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/36a12e02-c481-472c-8c9b-4f95b792b4e5" /></p>
<p align="center"> fuente: http://codigoelectronica.com/blog/compuerta-nand </p>

<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/297c25b3-5732-4caf-8813-b5d566552ce3" /></p>
<p align="center"> fuente: https://mielectronicafacil.com/sistemas-digtales/compuerta-logica-not/ </p>

-----------------

    CHIP Not {
    IN in;
    OUT out;

    PARTS:
    Nand(a=in,b=in,out=out);
    }
--------------
<h3 align="center">Compuerta AND</h3>
<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/a84e08d2-fcc5-4631-a2be-74c00ab3fb0f" /></p>
<p align="center"> fuente:http://codigoelectronica.com/blog/compuerta-and </p>


##### Para generar la compuerta AND solo es necesario negar la salida de la compuerta NAND, es decir asignar la salida de una compuerta NAND a la entrada de una NOT. 

    CHIP And {
    IN a, b;
    OUT out;

    PARTS:
    Nand(a=a,b=b,out=nand1);
    Nand(a=nand1, b=nand1, out=out);
    }

-----------------
<h3 align="center">Compuerta OR</h3>
<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/4d967b32-8721-4232-8da4-eea06ae46d45" /></p>
<p align="center">fuente: http://codigoelectronica.com/blog/compuerta-or</p>

##### Para realizar la compuerta OR es necesario recordar una de las leyes de De Morgan, es decir que la compuerta OR es equivalente a negar la salida de una compuerta AND que recibe las dos entradas previamente negadas.

    CHIP Or {
    IN a, b;
    OUT out;

    PARTS:
    Not(in=a,out=nota);
    Not(in=b,out=notb);
    Nand(a=nota,b=notb,out=out);	
    }
    
-----------------
<h3 align="center">Compuerta XOR</h3>
<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/18f5b511-8091-494b-9dcb-e54719fcd1ef"/></p>
<p align="center">fuente: http://codigoelectronica.com/blog/compuerta-xor</p>

##### Para realizar la compuerta XOR es necesario basarse en su tabla de verdad, en la que se logra ver que la compuerta XOR es equivalente a usar una compuerta AND cuyas entradas serán a y b negado, luego otra compuerta AND cuyas entradas serian a negado y b, para luego usar una compuerta OR cuyas entradas serán las salidas de las previas compuertas AND.

    CHIP Xor {
    IN a, b;
    OUT out;

    PARTS:
    Not(in=a,out=nota);
    Not(in=b,out=notb);	
    And(a=nota,b=b,out=out1);
    And(a=a,b=notb,out=out2);
    Or(a=out1,b=out2,out=out);	
    }

-----------------
<h3 align="center">Compuerta MUX</h3>
<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/87047d54-1708-4988-9692-235a2fdb6659" width="350" height="450"/></p>
<p align="center">fuente: https://areatecnologia.com/electronica/multiplexor.html</p>

##### Para realizar la compuerta MUX es necesario basarse en su tabla de verdad, la función de la compuerta MUX es escoger los valores de a ó b dependiendo del selector.  La compuerta MUX es equivalente a negar el selector, luego usar una compuerta AND cuyas entradas serán el valor de b y del selector, luego usar una compuerta AND cuyas entradas serán el valor de a y el valor del selector negado, para luego usar una compuerta OR cuyas entradas serán las salidas de las compuertas AND anteriores.

    CHIP Mux {
    IN a, b, sel;
    OUT out;

    PARTS:
    Not(in=sel,out=notsel);
    And(a=b,b=sel,out=out1);
    And(a=a,b=notsel,out=out2);
    Or(a=out1,b=out2,out=out);
    }

  -----------------
<h3 align="center">Compuerta DMUX</h3>
<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/ea9c2347-0187-42a1-b54b-b62d39177410"  width="350" height="250"/></p>
<p align="center">fuente: https://www.youtube.com/watch?v=fx8_DuTs1sU&ab_channel=UniversitatPolit%C3%A8cnicadeVal%C3%A8ncia-UPV</p>

##### Para realizar la compuerta DMUX es necesario basarse en su tabla de verdad, la función de la compuerta DMUX se encarga de ordenar el valor de la entrada, en alguno de sus dos valores de salida basado en su selector. La compuerta DMUX es equivalente a negar el selector, luego usar una compuerta AND cuyas entradas serían el valor de entrada para asignar el primer valor de salida, para el segundo valor de salida es necesario usar una compuerta AND cuyas entradas serían el valor de entrada y el selector.

    CHIP DMux {
    IN in, sel;
    OUT a, b;

    PARTS:
    Not(in=sel,out=notsel);
    And(a=in,b=notsel,out=a);
    And(a=in,b=sel,out=b);		
    }

  -----------------
<h3 align="center">Compuertas NOT16, AND16, OR16, MUX16 </h3>
<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/fa143957-75b3-46de-9648-813536108cdd"  width="450" height="300"/><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/2730c24c-5b5f-4a28-b2e0-431caefa9aa8"  width="450" height="300"/></p>
<p align="center">fuente: Chapter 1 Lecture - pages: 72,74</p>
<p align="center"><img src="https://github.com/DiegoToscano04/DiegoToscano04.github.io/assets/129452906/62ad4b93-6a93-4216-a882-91476c3816f5"  width="450" height="300"/></p>
<p align="center">fuente: Chapter 1 Lecture - page: 79</p>

 ##### Para NOT16, AND16, OR16, MUX16 hay que realizar 16 veces la función básica para cada compuerta, esto quiere decir, que para compuerta se deberá realizar la operación designada en pares, por ejemplo: And(a=a[i], b=b[i],out=out[i]) . Esto quiere decir que ahora ser recibirán arreglos como valores de entrada, excepto para la MUX16, la cual recibe arreglos y una constante la cual es el selector. Cada una de estas compuertas retornara un arreglo de 16 miembros.

#### NOT16
    CHIP Not16 {
    IN in[16];
    OUT out[16];

    PARTS:
    Not(in=in[0],out=out[0]);
    Not(in=in[1],out=out[1]);
    Not(in=in[2],out=out[2]);
    Not(in=in[3],out=out[3]);
    Not(in=in[4],out=out[4]);
    Not(in=in[5],out=out[5]);
    Not(in=in[6],out=out[6]);
    Not(in=in[7],out=out[7]);
    Not(in=in[8],out=out[8]);
    Not(in=in[9],out=out[9]);
    Not(in=in[10],out=out[10]);
    Not(in=in[11],out=out[11]);
    Not(in=in[12],out=out[12]);
    Not(in=in[13],out=out[13]);
    Not(in=in[14],out=out[14]);
    Not(in=in[15],out=out[15]);
    }

 #### AND16

    CHIP And16 {
    IN a[16], b[16];
    OUT out[16];

    PARTS:
    And(a=a[0],b=b[0],out=out[0]);
    And(a=a[1],b=b[1],out=out[1]);
    And(a=a[2],b=b[2],out=out[2]);
    And(a=a[3],b=b[3],out=out[3]);
    And(a=a[4],b=b[4],out=out[4]);
    And(a=a[5],b=b[5],out=out[5]);
    And(a=a[6],b=b[6],out=out[6]);
    And(a=a[7],b=b[7],out=out[7]);
    And(a=a[8],b=b[8],out=out[8]);
    And(a=a[9],b=b[9],out=out[9]);
    And(a=a[10],b=b[10],out=out[10]);
    And(a=a[11],b=b[11],out=out[11]);
    And(a=a[12],b=b[12],out=out[12]);
    And(a=a[13],b=b[13],out=out[13]);
    And(a=a[14],b=b[14],out=out[14]);
    And(a=a[15],b=b[15],out=out[15]);
    }
    
 #### OR16

    CHIP Or16 {
    IN a[16], b[16];
    OUT out[16];

    PARTS:
    Or(a=a[0],b=b[0],out=out[0]);
    Or(a=a[1],b=b[1],out=out[1]);
    Or(a=a[2],b=b[2],out=out[2]);
    Or(a=a[3],b=b[3],out=out[3]);
    Or(a=a[4],b=b[4],out=out[4]);
    Or(a=a[5],b=b[5],out=out[5]);
    Or(a=a[6],b=b[6],out=out[6]);
    Or(a=a[7],b=b[7],out=out[7]);
    Or(a=a[8],b=b[8],out=out[8]);
    Or(a=a[9],b=b[9],out=out[9]);
    Or(a=a[10],b=b[10],out=out[10]);
    Or(a=a[11],b=b[11],out=out[11]);
    Or(a=a[12],b=b[12],out=out[12]);
    Or(a=a[13],b=b[13],out=out[13]);
    Or(a=a[14],b=b[14],out=out[14]);
    Or(a=a[15],b=b[15],out=out[15]);
    }
    
 #### MUX16

    CHIP Mux16 {
    IN a[16], b[16], sel;
    OUT out[16];

    PARTS:
    Mux(a=a[0],b=b[0],sel=sel,out=out[0]);
    Mux(a=a[1],b=b[1],sel=sel,out=out[1]);
    Mux(a=a[2],b=b[2],sel=sel,out=out[2]);
    Mux(a=a[3],b=b[3],sel=sel,out=out[3]);
    Mux(a=a[4],b=b[4],sel=sel,out=out[4]);
    Mux(a=a[5],b=b[5],sel=sel,out=out[5]);
    Mux(a=a[6],b=b[6],sel=sel,out=out[6]);
    Mux(a=a[7],b=b[7],sel=sel,out=out[7]);
    Mux(a=a[8],b=b[8],sel=sel,out=out[8]);
    Mux(a=a[9],b=b[9],sel=sel,out=out[9]);
    Mux(a=a[10],b=b[10],sel=sel,out=out[10]);
    Mux(a=a[11],b=b[11],sel=sel,out=out[11]);
    Mux(a=a[12],b=b[12],sel=sel,out=out[12]);
    Mux(a=a[13],b=b[13],sel=sel,out=out[13]);
    Mux(a=a[14],b=b[14],sel=sel,out=out[14]);
    Mux(a=a[15],b=b[15],sel=sel,out=out[15]);
    }
    
  -----------------
<h3 align="center">Compuerta OR8WAY</h3>

###### Para realizar la compuerta OR8WAY solamente hay que anidar compuertas OR, es decir, conectar la salida de una OR a la entrada de otra OR. En esta función se procesan arreglos de 8 miembros, lo que quiere decir que se usan 7 compuertas OR.

    CHIP Or8Way {
    IN in[8];
    OUT out;

    PARTS:
    Or(a=in[0],b=in[1],out=out1);
    Or(a=in[2],b=out1,out=out2);
    Or(a=in[3],b=out2,out=out3);
    Or(a=in[4],b=out3,out=out4);
    Or(a=in[5],b=out4,out=out5);
    Or(a=in[6],b=out5,out=out6);
    Or(a=in[7],b=out6,out=out);
    }

-----------------
<h3 align="center">Compuerta MUX4WAY16</h3>

###### Para realizar la compuerta MUX4WAY16 debemos primero usar una compuerta MUX16 y comparar los valores de la primera entrada con los de la segunda usando como selector el bit menos significativo del selector original. Luego, se hace lo mismo pero esta vez con la tercera y cuarta entrada. Para finalizar se usa otra compuerta MUX16 con las salidas de las compuertas anteriores como entrada y como selector el bit más significativo el selector original.

    CHIP Mux4Way16 {
    IN a[16], b[16], c[16], d[16], sel[2];
    OUT out[16];

    PARTS:
    Mux16(a=a,b=b,sel=sel[0],out=out1);
    Mux16(a=c,b=d,sel=sel[0],out=out2);
    Mux16(a=out1, b=out2,sel=sel[1],out=out);    
    }

-----------------
<h3 align="center">Compuerta MUX8WAY16</h3>

##### Para realizar la compuerta MUX8WAY16 se realiza un proceso similar al proceso de realización de la compuerta MUX4WAY16, solo que en este caso se usara la compuerta MUX4WAY16 en vez de la MUX16, se usara como selector los bits distintos al más significativo del selector original, y en el final se seguía usando una compuerta MUX16 cuyas entradas serán las salidas de las compuertas MUX4WAY16 y su selector será el bit más significativo del selector original. 
##### Tenga en cuenta que la compuerta MUX selecciona, por lo tanto, para realizar la compuerta MUX4WAY16, lo que se hace es primero seleccionar entre dos pares de entradas, para luego seleccionar los valores finales. Pasa algo análogo para la compuerta MUX8WAY16.

    CHIP Mux8Way16 {
    IN a[16], b[16], c[16], d[16],
       e[16], f[16], g[16], h[16],
       sel[3];
    OUT out[16];

    PARTS:
    Mux4Way16(a=a,b=b,c=c,d=d,sel=sel[0..1], out=out1);
    Mux4Way16(a=e,b=f,c=g,d=h,sel=sel[0..1], out=out2);
    Mux16(a=out1,b=out2,sel=sel[2],out=out);
    }

  -----------------
<h3 align="center">Compuerta DMUX4WAY</h3>

##### Para realizar la compuerta DMUX4WAY se usan las compuertas DMUX, las compuertas DMUX se encargan de ordenar un valor dependiendo del selector, por lo tanto, primero se usa el bit más significativo del selector para determinar en qué par de grupos está la entrada si (a,b) o (c,d), luego de ello se usa un DMUX para cada grupo cuyo selector es el bit menos significativo del selector original. 

    CHIP DMux4Way {
    IN in, sel[2];
    OUT a, b, c, d;

    PARTS:   
    DMux(in=in,sel=sel[1],a=out1,b=out2);
    DMux(in=out1,sel=sel[0],a=a,b=b);
    DMux(in=out2,sel=sel[0],a=c,b=d);    
    }

  -----------------
<h3 align="center">Compuerta DMUX8WAY</h3>

##### Para realizar la compuerta DMUX8WAY se realiza un proceso análogo a la DMUX4WAY solo que aquí se usar las compuertas DMUX4WAY en vez de las DMUX, salvo la primera compuerta DMUX la cual se mantiene. Para este caso el selector de la compuerta DMUX sigue siendo el bit más significativo del selector original, pero para las DMUX4WAY el selector será todos los bits del selector original excepto el significativo.

    CHIP DMux8Way {
    IN in, sel[3];
    OUT a, b, c, d, e, f, g, h;

    PARTS:
    DMux(in=in,sel=sel[2],a=out1,b=out2);
    DMux4Way(in=out1,sel=sel[0..1],a=a,b=b,c=c,d=d);
    DMux4Way(in=out2,sel=sel[0..1],a=e,b=f,c=g,d=h);
    }

  -----------------
<h3 align="center">Compuerta DMUX</h3>

##### Tenga en cuenta que la compuerta DMUX ordena, por lo tanto, para realizar la compuerta DMUX4WAY, lo que se hace es primero determinar en qué par irá el valor de entrada, si en el par (a,b) o (c,d), para luego ordenar en el par correspondiente. El caso del DMUX8WAY ocurre lo mismo solo que primero hay que decidir en qué grupo de 4 miembros estará el valor a ordenar.

    CHIP DMux {
    IN in, sel;
    OUT a, b;

    PARTS:
    Not(in=sel,out=notsel);
    And(a=in,b=notsel,out=a);
    And(a=in,b=sel,out=b);		
    }
