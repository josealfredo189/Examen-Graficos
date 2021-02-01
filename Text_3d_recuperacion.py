import numpy as np
import matplotlib.pyplot as plt 
from math import sqrt, ceil
import keyboard as kb


#--------Asignar ejes--------
#Se le asigna los ejes X, Y en la vetana
plt.title('Triangle 3D')
plt.xlabel(r'EJE x')
plt.ylabel(r'EJE y')

#Coordenadas de la figura
x = [40, 30, 80, 85]# eje x
y = [60, 10, 60, 40]# eje y 
z = [ 0,  0,  0,  0]# eje z

#Coordenadas generales a los cuales despues
#se les asignaran las coordenadas de la figura
xg = []
yg = []
zg = []

#Plotear el triangulo
def plotTriangle(xg, yg, zg):
    
    #Plotear la base del triangulo, de color negro 
    plt.plot([xg[0],xg[1]], [yg[0],yg[1]], color='k')
    plt.plot([xg[1],xg[2]], [yg[1],yg[2]], color='k')
    plt.plot([xg[2],xg[0]], [yg[2],yg[0]], color='k')
    plt.scatter(xg[3], yg[3], s=20, color='r')    # el hitpoint (red dot)
    #Plotea los otros dos triangulos
    plt.plot([xg[0],xg[3]], [yg[0],yg[3]], linestyle=':', color='orange')   #plotea 1st linea punteada
    plt.plot([xg[1],xg[3]], [yg[1],yg[3]], linestyle=':', color='orange')   #plotea 2st llinea punteada
    plt.plot([xg[2],xg[3]], [yg[2],yg[3]], linestyle=':', color='orange')   #plotea 3st llinea punteada

    #Triangle corners: las esquinas de cada triangulo aunque se muevan
    plt.text(xg[0]+2, yg[0], '0')
    plt.text(xg[1]+2, yg[1], '1')
    plt.text(xg[2]+2, yg[2], '2')
    plt.text(xg[3]+2, yg[3], '3')

def hitpoint(x, y, z):
    #---------------------Calculate area A---------------------
    ##con la formula s=(a+b+c)/2     A=raiz(s(s-a)(s-b)(s-c))
    #Calculate dimensions from triangle base (plane)
    #Calcula el a del triagulo 
    a = abs(x[1]-x[0])
    b = abs(y[1]-y[0])
    c = abs(z[1]-z[0])
    q01=sqrt(a*a+b*b+c*c)
    #Calcula el b del triagulo 
    a = abs(x[2]-x[1])
    b = abs(y[2]-y[1])
    c = abs(z[2]-z[1])
    q12=sqrt(a*a+b*b+c*c)
    #Calcula el c del triagulo 
    a = abs(x[2]-x[0])
    b = abs(y[2]-y[0])
    c = abs(z[2]-z[0])
    q02=sqrt(a*a+b*b+c*c)
    #Caculate el area del triangulo A
    s = (q01+q12+q02)/2
    A = sqrt(s*(s-q01)*(s-q12)*(s-q02))

    #---------------------Calculate area A1---------------------
    #Calcula el a del triagulo 
    a = abs(x[1]-x[3])
    b = abs(y[1]-y[3])
    c = abs(z[1]-z[3])
    q13=sqrt(a*a+b*b+c*c)
    #Calcula el b del triagulo 
    a = abs(x[0]-x[1])
    b = abs(y[0]-y[1])
    c = abs(z[0]-z[1])
    q10=sqrt(a*a+b*b+c*c)
    #Calcula el c del triagulo 
    a = abs(x[0]-x[3])
    b = abs(y[0]-y[3])
    c = abs(z[0]-z[3])
    q30=sqrt(a*a+b*b+c*c)
    #Caculate el area del triangulo A1
    s1=(q13+q10+q30)/2
    A1=sqrt(s1*(s1-q13)*(s1-q10)*(s1-q30))

    #---------------------Calculate area A2---------------------
    #Calcula el a del triagulo 
    a = abs(x[0]-x[3])
    b = abs(y[0]-y[3])
    c = abs(z[0]-z[3])
    q30=sqrt(a*a+b*b+c*c)
    #Calcula el a del triagulo 
    a = abs(x[0]-x[2])
    b = abs(y[0]-y[2])
    c = abs(z[0]-z[2])
    q20=sqrt(a*a+b*b+c*c)
    #Calcula el a del triagulo 
    a = abs(x[2]-x[3])
    b = abs(y[2]-y[3])
    c = abs(z[2]-z[3])
    q32=sqrt(a*a+b*b+c*c)
    #Caculate el area del triangulo A2
    s2=(q30+q20+q32)/2
    A2=sqrt(s2*(s2-q30)*(s2-q20)*(s2-q32))
    #Devuelve las areas
    return A, A1, A2

# Permite pletear todo los mensajes y lo anterior
def Plot(x, y, z, xg, yg, zg):

    #Muestra la ventana de la figura
    plt.axis([100, 220, 30, 120])
    plt.grid()

    #Llama al hitpoint y le asigna las areas a sus respectivas variables 
    [A, A1, A2] = hitpoint(x, y, z)
    
    #Redondeamos los valores de la areas con "ceil" 
    # el cual se importa al principo
    a = ceil(A)
    a1= ceil(A1)
    a2= ceil(A2)
    a3= ceil(A1+A2)
    
    #Mostramos las etiquetas de las areas A, A1, A2 con distintos colores
    plt.text(175,80,'A=',color='b')
    plt.text(185,80,a,color='b')
    plt.text(175,85,'A1=',color='purple')
    plt.text(187,85,a1,color='purple')
    plt.text(175,90,'A2=',color='k')
    plt.text(187,90,a2,color='k')

    #Si el resultado de A1+A2 es mayor a A
    #se muestra el siguiente mensaje y su resultado (indicando que esta fuera dle limite)
    if((A1+A2)>A):
        plt.text(150,60,'El HIT PONT esta Fuera de los limites', color='r')
        plt.text(175,75,'A1+A2=',color='r')
        plt.text(190,75,a3,color='r')
    else:#De lo contrario se muestra el siguiente mensaje y su resultado (indicando que esta dentro del limite)
        plt.text(150,60,'El HIT PONT esta dentro del limite', color='g')
        plt.text(175,75,'A1+A2=',color='g')
        plt.text(190,75,a3,color='g')
    
    #Ejecuta la funcion para mostrar el triangulo 
    plotTriangle(xg, yg, zg)
    plt.gca().set_aspect('equal')   #Muestra la grafica igual sin importa la resolucion de la pantalla
    plt.show()  #Muestra la grafica

#Pide el hitpoint x, y o el numeoro la tecla 'esc'
while True:
    #----Variable que indican el centro de la figura 
    xc = 80
    yc = 40
    zc = 40

    #Le pide al usuario el hitpoin en "x" o que precione "esc" para salir
    """Profe perdon pero no pude hacer que recibiera la tecla esc
    """
    enterx=input('donde esta el hitpoint en "x"? o presiona 18390045 para salir ')
    if enterx=='18390045':# si presiona "18390045" se cierra el programa
        break
    else:
        
        #De lo contrario el valor dado se le asigna a la vairbale "x" en la posicion 3
        x[3]=int(enterx)
 
        #Le pide al usuario el hitpoin en "y" o que precione "esc" para salir
        entery=input('donde esta el hitpoint en "y"? o presiona 18390045 para salir ')
        if entery=='18390045':# si presiona "18390045" se cierra el programa
            break
        else:

            #De lo contrario el valor dado se le asigna a la vairbale "y" en la posicion 3
            y[3]=int(entery)

            #los valores asignados por el usuario y los que ya tienen las variables
            # se le asignan a las variables generales, sumado del sentro
            for i in range(len(x)):
                xg.append(x[i]+xc)
                yg.append(y[i]+yc)
                zg.append(z[i]+zc)

            # Se plotea todo el proceso y se le mandan las respectivas variables a la funcion
            Plot(x, y, z, xg, yg, zg)
            
            #Limpia las variables generales
            #en caso que el usuario quiera volver a indicar otro hitpoint
            j=0
            while j< 4:
                xg.remove(xg[0])
                yg.remove(yg[0])
                zg.remove(zg[0])
                j+=1
