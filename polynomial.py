# polynomial.py

class Polynomial:

    def __init__(self, *coefficients):
        self.caefs = []  #список значений

        if len(coefficients) == 1 and isinstance(coefficients[0], Polynomial):
            for c in coefficients[0].caefs:
                self.caefs.append(c)

        #создали многочлен из многочлена

        elif len(coefficients) == 1 and isinstance(coefficients[0], dict):
            slovar = coefficients[0]
            max_stepen = 0
            for stepen in slovar:
                if stepen > max_stepen:
                    max_stepen = stepen

            for i in range(max_stepen + 1):
                self.caefs.append(0)

            for stepen in slovar:
                self.caefs[stepen]=slovar[stepen]

        #Создали многочлен из словаря

        elif len(coefficients) == 1 and isinstance(coefficients[0], (list, tuple)):
            for c in coefficients[0]:
                self.caefs.append(c)

        #Создали многочлен из списка

        else:
            for c in coefficients:
                self.caefs.append(c)


        #Создали многочлен из цифр аргументов

        while len(self.caefs)>1 and self.caefs[-1]==0:
            self.caefs.pop()

        #Удаляем нулевые значения, оставляем один ноль, если ничего нет

        if len(self.caefs)==0:
            self.caefs.append(0)

        #Если нет аргументов, добавляем просто ноль

        self._index = 0
        #Счётчик для итерации по многочлену

    def __repr__(self):
        return "Polynomial" + str(self.caefs)

    # Выводит троку вида Polynomial <список коэффициентов>

    def to_poly(self, other):
        if isinstance(other, Polynomial):
            return other
        if isinstance(other, (int, float, complex)):
            return Polynomial([other])
        return None
    #Для превращения чисел в многочлен

    def __str__(self):
        s = ''
        for stepen in range(len(self.caefs)- 1, -1, -1):
            k=self.caefs[stepen]
            if k==0:
                continue
            #Пропускаем нулевые члены
            if k>0:
                znak = '+'
            else:
                znak = '-'
            #Запомнили знак
            if abs(k)==1 and stepen>0:
                caef = ''
            else:
                caef = str(abs(k))
            #Если число равно единице, но степень есть, не пишем его
            if stepen==0:
                iks=''
            elif stepen==1:
                iks='x'
            else:
                iks='x^' + str(stepen)
            #Смотрим, что будем выводить
            chlen=caef+iks
            if s=='':
                if znak=='-':
                    s='-'+chlen
                else:
                    s=chlen
            else:
                s=s + " " + znak + " " + chlen
        if s == '':
            s='0'
        return s

    #Вывод и представление многочлена в виде строки

    def __eq__(self, other):
        other = self.to_poly(other)
        if other is None:
            return NotImplemented
        return self.caefs == other.caefs

    #Проверка на равность

    def __add__(self, other):
        other = self.to_poly(other)
        if other is None:
            return NotImplemented
        # Проверка

        n = len(self.caefs)
        if len(other.caefs) > n:
            n = len(other.caefs)
        res = []
        for i in range(n):
            a = 0
            if i < len(self.caefs):
                a = self.caefs[i]
            b = 0
            if i < len(other.caefs):
                b = other.caefs[i]
            # Берём первые коэфициенты у каждого многочлена
            res.append(a + b)
            # Складываем
        return Polynomial(res)

    # Сложение двух многочленов или формата многочлен+что-то, но не наоборот

    def __radd__(self, other):
        return self + other
    #Сложение как угодно

    def __neg__(self):
        res = []
        for c in self.caefs:
            res.append(-c)
        return Polynomial(res)

    #Унарный минус, просто идем по всем коэфициентам и добавляем их с отрицательным знаком
    def __sub__(self, other):
        other = self.to_poly(other)
        if other is None:
            return NotImplemented
        return self + (-other)

    #Вычитание, используем для него сложение и унарный минус вместе, числа справа

    def __rsub__(self, other):
        other = self.to_poly(other)
        if other is None:
            return NotImplemented
        return other + (-self)

    #Вычитание для чисел слева

    def __call__(self, x):
        r = 0
        for i in range(len(self.caefs)):
            r += self.caefs[i] * x ** i
        return r

    #Смотрим на многочлен как на функцию
    def degree(self):
        return len(self.caefs)-1
    #Понижение степени

    def der(self, d):
        if d<0:
            return 0
        res = []
        for i in range(d, len(self.caefs)):
            m=1
            for n in range(d):
                m=m*(i-n)
            res.append(m*self.caefs[i])
        return Polynomial(res)

    #Берем производную от многочлена

    def __mul__(self, other):
        other = self.to_poly(other)
        if other is None:
            return NotImplemented

        dlina = len(self.caefs) + len(other.caefs)-1
        res = []
        for i in range(dlina):
            res.append(0)
        #Заполняем длину нулями
        for i in range(len(self.caefs)):
            for n in range(len(other.caefs)):
                res[i+n]+=self.caefs[i]*other.caefs[n]
        #Перемножение всех пар членов с одинаковыми степенями
        return Polynomial(res)
    #Умножение многочлена на многочлен, или многочлена на число

    def __rmul__(self, other):
        return self * other
    #Умножение числа на многочлен

    def __iter__(self):
        i = Polynomial(self)
        i._index = 0
        return i

    def __next__(self):
        if self._index >= len(self.caefs):
            raise StopIteration
        #Чтоб не сломалось в конце
        para = (self._index, self.caefs[self._index])
        self._index += 1
        return para

    #Для цикла for


poly1=Polynomial(1, 3, 5, 6, 1)
poly2=Polynomial(2, 4, 6, 7) #многочлен из чисел через запятую
print(poly1) #str
print(poly1+poly2)#add
x=4
print(x+poly2) #radd
print((x+poly2)(x)) #call
print(poly1.der(3)) #der
print(poly2*2) #mul
print(2*poly2) #rmul
for i, j in poly1: #iter, next
    print(i, j)
print(Polynomial({0: -3, 5: -11, 5: 67}))  # многочлен из словаря
print(Polynomial([1, 2, 3]))  # Многочлен из списка
print(poly2.degree()) #Понижение степени degree
print(poly2 == poly2) #eq
print(-poly2) #neg
print(poly2 - poly2) #sub
print(poly2 - 5) #sub
print(5 - poly2) #rsub
print(poly2.der(3)) #der
print(poly2.__repr__())