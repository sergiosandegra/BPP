class OperacionesMatematicas:
    """
    Operaciones matemáticas. Es una clase que permite realizar una serie de operaciones matemáticas con números enteros.
    Atributos:
        op1: es el primer operando de la operación matemática y debe ser de tipo entero. Si un método solo recibe un parámetro, 
        éste será op1.
        op2: es el segundo operando de la operación matemática y debe ser de tipo entero.
    Métodos:
        suma: 
            suma los enteros op1 y op2
        resta: 
            resta los enteros op1 y op2
        producto: 
            multiplica los enteros op1 y op2
        division: 
            divide el entero op1 entre op2. Si op2 vale 0 , el resultado será 0.
        factorial: 
            calcula el factorial de op1
        es_primo: 
            determina si op1 es o no primo

    >>> import OperacionesMatematicas
    >>> oM = OperacionesMatematicas(4, 5)
    >>> suma = OperacionesMatematicas.suma()
    >>> fact = OperacionesMatematicas.factorial()
    """
    
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2


    def suma(self):
        """
        Metodo suma. Aplica el algoritmo de la suma sobre los operandos op1 y op2.
        Input:
            La entrada son los operandos op1 y op2 que son atributos de la clase.
        Output:
            Resultado: variable de tipo entero que almacena el resultado de sumar op1 y op2
        """
        resultado = self.op1 + self.op2
        return resultado


    def resta(self):
        """
        Metodo resta. Aplica el algoritmo de la resta sobre los operandos op1 y op2.
        Input:
            La entrada son los operandos op1 y op2 que son atributos de la clase.
        Output:
            Resultado: variable de tipo entero que almacena el resultado de restar op1 y op2
        """
        resultado = self.op1 - self.op2
        return resultado


    def producto(self):
        """
        Metodo producto. Aplica el algoritmo de la multiplicacion sobre los operandos op1 y op2.
        Input:
            La entrada son los operandos op1 y op2 que son atributos de la clase.
        Output:
            Resultado: variable de tipo entero que almacena el resultado de multiplicar op1 y op2
        """
        resultado = self.op1 * self.op2
        
        return resultado


    def division(self):
        """
        Metodo division. Aplica el algoritmo de la division sobre los operandos op1 y op2.
        Input:
            La entrada son los operandos op1 y op2 que son atributos de la clase.
        Output:
            Resultado: variable de tipo entero que almacena el resultado de dividir op1 y op2
        """
        resultado = 0
        if(self.op2 != 0):
            resultado = self.op1 / self.op2

        return resultado


    def primo(self):
        """
        Metodo primo. Determina si el operando op1 es un numero primo.
        Inputs:
        -------
            self.op1
        Outputs:
        -------
            True su self.op1 es primo, False en caso contrario
        """
        es_primo = True
        for i in (2, self.op1 - 1):
            if(self.op1%i == 0):
                es_primo = False

        return es_primo


    def factorial(self):
        """
        Metodo para calcular el factorial de un numero.
        """
        assert(n >= 0)

        fct = 1
        for i in range(1, self.op1 + 1):
            fct *= i
        
        return fct