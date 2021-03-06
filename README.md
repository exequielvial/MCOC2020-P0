# Mi computador principal
* Marca/modelo: Hp Envy15-J012la
* Notebook
* Año de adquisición 2015
* Procesador:
	* Intel Core i5-4200M
	* Velocidad base: 2.50 GHz
	* Velocidad máxima: 3.0 GHz 
	* Número de núcleos: 2
	* Número de hilos: 4
	* Arquitectura: x64
* Tamaño de las cachés del procesador:
	* L1: 128 KB
	* L2: 512 KB
	* L3: 3.0 MB
* Memoria:
	* Total 8 GB
	* Tipo de memoria: DDR3
	* Velocidad: 1600 MHz
	* Número de (SO)DIMM: 1 (creo) 
* Tarjeta gráfica:
	* Nvidia GeForce GT 750M
	* Memoria dedicada: 4GB
	* Resolución: 1920 x 1080
* Disco 1:
	* Marca: KingSpec 
	* Tipo: SSD
	* Tamaño: 256 GB
	* Particiones: 1
	* Sistema de archivos: NTFS
* Disco 2:
	* Marca: Samsung
	* Tipo: HDD
	* Tamaño: 750 GB
	* Particiones: 1
	* Sistema de archivos: NTFS
* Proovedor de internet: GTD Manquehue fibra óptica
* Desempeño MATMUL:
* Gráfico: https://github.com/exequielvial/MCOC2020-P0/issues/1#issue-675370055
* 1) El gráfico de la memoria es igual, lógicamente, sin embargo hay unas leves diferencias en el gráfico de rendimiento ya que mis ciclos se tardan más en un inicio.
* 2) Esto es debido principalmente a que mi procesador no es tan potente como el del profesor y eso hace que tarde más en comenzar a leer el ciclo una vez empieza una iteración pero luego alcanzan una velocidad parecida a largo plazo.
* 3) El gráfico de la memoria utilizada es lógico que sea lineal ya que la memoria está definida bajo una fórmula que varía linealmente según N, por otro lado el gráfico del rendimiento no es lineal por un lado porque el computador en que llevé a cabo el programa estaba haciendo más procesos simultáneamente al correr los distintos ciclos por lo que tenía distinta capacidad de RAM a lo largo del ciclo, por otro lado, la multiplicación de las matrices no aumenta linealmente por lo que es esperable que el rendimiento tampoco sea así
* 4) Versión 3.8 de python
* 5) Versión 1.18.5 de numpy
* 6) Gráfico: https://github.com/exequielvial/MCOC2020-P0/issues/2#issue-675389002, como se puede ver en este hay momentos en que supera el 100% por lo que podemos asumir que es en este momento que comienza a utilizar otro procesador para correr el programa, de lo contrario no lo podría hacer.  pd: La imagen del gráfico la saqué al principio de correr el ciclo porque cuano abro esa ventana luego de un rato se reinicia mi computador. 
-----------
* Gráfico matmul multiplicación hecha a mano: https://github.com/exequielvial/MCOC2020-P0/issues/3#issuecomment-671661284
---------
* Gráficos inversas según tipo de datos:
	* Half: https://github.com/exequielvial/MCOC2020-P0/issues/6#issue-678108944
	* Single: https://github.com/exequielvial/MCOC2020-P0/issues/5#issue-678108721
	* Double: https://github.com/exequielvial/MCOC2020-P0/issues/7#issue-678109124
	* Longdouble: https://github.com/exequielvial/MCOC2020-P0/issues/8#issue-678109305
* Se puede ver claramente que el uso de memoria ram aumenta a medida que vamos cambiando los tipos de datos (en el orden entregados), esto se debe a que aumentan los bytes de cada float, en todos los casos se superan los 3 procesadores que posee mi computador.
---------
* Entrega 6:
	* Como es de esperar todos toman tiempos muy parecidos para llevar a cabo el proceso cuando el tamaño de la matriz es pequeño, pero con el aumento de este tamaño se puede observar claramente que a medida que vamos agregando más información a cada inversa, es menor el tiempo que ocupa, esto se puede atribuir a que al ser python un lenguaje de alto nivel si no le decimos específicamente qué vamos a necesitar para llevar a cabo el programa, este va a importar y utilizar más herramientas de las que se necesitan, por esto al usar pos_overwrite=True toma menos tiempo en terminar el ciclo, ya que es una orden muy directa que se le da al computador. 
----------
* Entrega 7:
	* Gráficos:
		* Inversa llena: https://github.com/exequielvial/MCOC2020-P0/issues/9#issue-683907103
		* Inversa dispersa: https://github.com/exequielvial/MCOC2020-P0/issues/10#issue-683907453
		* Matmul llena: https://github.com/exequielvial/MCOC2020-P0/issues/11#issue-683907538
		* Matmul dispersa: https://github.com/exequielvial/MCOC2020-P0/issues/12#issue-683907609
		* Solve llena: https://github.com/exequielvial/MCOC2020-P0/issues/13#issue-683907698
		* Solve dispersa: https://github.com/exequielvial/MCOC2020-P0/issues/14#issue-683907763
	* Código matrices laplacianas: https://github.com/exequielvial/MCOC2020-P0/blob/master/Entrega%207/M_laplacianas.py
	* 1.Se puede observar que en los 3 casos que el tiempo de ensamblado en el caso de la matriz dispersa es menor, lo cual es lógico ya que le estamos diciendo al computador que muchos valores van a ser cero y le ahorramos memoria en el proceso, pero el tiempo de solución en todos los casos es menos en los que se trabaja con matriz llena, esto se puede deber a que se maneja mayor información de la matriz al manera de usarla, en todo caso una vez que el número de datos es muy grande estos tiempos son casi iguales.
	* 2. En todos los casos se puede observar que el comportamiento asintótico para el ensamblado es de una complejidad N^2 ya que se puede observar una tendencia a esta recta, esto es porque ya llega un punto en que el proceso que se demora en computador no es tan elevado con respecto a números menores, pero por otro lado la complejidad asintótica para las soluciones es de N^3, ya que al igual que el anterior tiende a reducir su incremento de tiempo, pero sigue siendo mayor al tiempo de ensamblado por la complejidad del proceso.
	* 3. Mientras mayor es el tamaño de las matrices, más semejante son los tiempos que toma cada corrida, teniendo además un comportamiento más lineal que anteriormente. 
	* 4. Todas las corridas tanto usando matrices llenas como dispersas comienzan con un rango de comportamiento, donde se puede observar una gran variedad de tiempos, dentro de un rango acotado, y luego se forma un comportamiento más parejo, el cual se logra antes en los procesos que se utiliza matrices llenas.
	

	
