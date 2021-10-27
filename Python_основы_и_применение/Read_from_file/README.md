## [Interesting_number.py](https://github.com/vasoltu/Stepik/blob/main/Python_основы_и_применение/Read_from_file/Interesting_number.py)
Используется API сайта numbersapi.com

Дан набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический факт об этом числе.

Для каждого числа вывести Interesting, если для числа существует интересный факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.

**Пример запроса к интересному числу:**
```
http://numbersapi.com/31/math?json=true
```
**Пример запроса к скучному числу:**
```
http://numbersapi.com/999/math?json=true
```
**Пример входного файла:**
```
31
999
1024
502
```

**Пример выходного файла:**
```
Interesting
Boring
Interesting
Boring
```
