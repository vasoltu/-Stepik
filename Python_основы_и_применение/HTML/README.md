## [Html(A,B).py](https://github.com/vasoltu/Stepik/blob/main/Python_основы_и_применение/HTML/Html(A%2CB).py)
Рассмотрим два HTML-документа A и B.
Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">, возможно с дополнительными параметрами внутри тега.
Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за один переход и из C в B можно перейти за один переход.

Программе на вход подаются две строки, содержащие url двух документов A и B.
Вывести Yes, если из A в B можно перейти за два перехода, иначе выведите No.

Обратить внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.

**Sample Input 1:**
```
https://stepic.org/media/attachments/lesson/24472/sample0.html
https://stepic.org/media/attachments/lesson/24472/sample2.html
```
  
**Sample Output 1:**
  
```
Yes
```

**Sample Input 2:**
```
https://stepic.org/media/attachments/lesson/24472/sample0.html
https://stepic.org/media/attachments/lesson/24472/sample1.html
```
**Sample Output 2:**
```
No
```
  
**Sample Input 3:**
```
https://stepic.org/media/attachments/lesson/24472/sample1.html
https://stepic.org/media/attachments/lesson/24472/sample2.html
```
**Sample Output 3:**
```
Yes
```
  
  
## [Html(parser).py](https://github.com/vasoltu/Stepik/blob/main/Python_основы_и_применение/HTML/Html(parser).py)
Программе на вход подается ссылка на HTML файл.
Необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... > и вывести список сайтов, на которые есть ссылка.

Сайтом будем называть имя домена вместе с именами поддоменов. То есть, это последовательность символов, которая следует сразу после символов протокола, если он есть, до символов порта или пути, если они есть, за исключением случаев с относительными ссылками вида
<a href="../some_path/index.html">.

Сайты следует выводить в алфавитном порядке.

**Пример HTML файла:**
```
<a href="http://stepic.org/courses">
<a href='https://stepic.org'>
<a href='http://neerc.ifmo.ru:1345'>
<a href="ftp://mail.ru/distib" >
<a href="ya.ru">
<a href="www.ya.ru">
<a href="../skip_relative_links">
```
**Пример ответа:**

```
mail.ru
neerc.ifmo.ru
stepic.org
www.ya.ru
ya.ru
```
  
