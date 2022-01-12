# Xpath

[XPath Tutorial from W3School](https://www.w3schools.com/xml/xpath_intro.asp)

[Xpather.com](http://xpather.com/)

[Xpath cheatsheet](https://devhints.io/xpath)

[Extension de Chrome para xPath](https://chrome.google.com/webstore/detail/xpath-finder/ihnknokegkbpmofmafnkoadfjkhlogph)

[SelectorGadget. Extension de Chrome](https://chrome.google.com/webstore/detail/selectorgadget/mhjhnkcfbdhnjickkkdbjoemdmbfginb?hl=en)

[HTML tree generator Chrome extension](https://chrome.google.com/webstore/detail/html-tree-generator/dlbbmhhaadfnbbdnjalilhdakfmiffeg)

[Tutorial de Youtube](https://www.youtube.com/watch?v=0O1SyTh8Zxo&ab_channel=LeonardoKuffo)

XML Path Language es una técnica para extraer información del lenguaje XML.

`XPath` es a `HTML` lo que `Regex` es a `texto`, ambas buscan patrones.

Los tipos de nodos que se reconocen en una consulta XPath no son los tipos de nodos que se encuentran en el DOM.


Tipos de nodos:

* **Root (Document)**: Nodo raiz del documento.
* **Element**: Un elemento, como ``<element>``.
* **Attribute**: Un atributo, como ``id='123``.
* **Namespace**: Un espacio de nombres, como ``xmlns="namespace"``.
* **Text**: Contenido de texto de un nodo. Equivalente al texto del DOM. Contiene por lo menos un carácter.
* **SignificantWhitespace**: Un nodo con caracteres de espacio en blanco y ``xml:space`` establecido en ``preserve``.
* **Whitespace**: Nodo sólo con caracteres de espacio en blanco y sin espacio en blanco significativo. Los caracteres de espacio en blanco son ``#x20``, ``#x9``, ``#xD`` o ``#xA``.
* **ProcessingInstruction**: Una instrucción de procesamiento, como ``<?pi test?>``. 
* **Comment**: Un comentario, como ``<!-- my comment -->``.

En el navegador se puede interactuar con las consultas xpath al presionar F12 -> Elements y presionar ctrl+f

## Expresiones

para probar las expresiones en el navegador

```xpath
$x('')
```
Expresion | ejemplo | descripción
--------- | ------- | -----------
/ | `/html/body/div` | root
// | `//div//h1` | Anywhere
.. | `//span/..` | nodos padre
\| | `//book/title \| //book/price` |  select several paths.
@ | `//span/@class` | extraer el valor del atributo
text() | `//h1/a/text()` | extraer el texto

## Predicados

Se usan dentro de corchetes `[ ]`. Se pueden usar operadores típicos de programación.

Predicado | ejemplo | descripción
--------- | ------- | -----------
n | `/html/body/div/div[1]` | el div número uno
last() | `/html/body/div/div[last()-1]` | el penúltimo div
position() | `/html/body/div/div[position()>4]` | algunos div
element | `//book[price<30]` | filtrado por **element** (node hijo)
@class | `//span[@class]` | filtrado por atributo
@class=" " | `//span[@class="text" or @class="tag-item]` | filtrado más específico
not | `//span[not(@class)]` | negación


para ver los valores o el texto en la consola del navegador chrome

```xpath
$x('//article[@class="product_pod"]/h3/a/@title').map(x => x.value)
```

```xpath
$x('//span[@class="text"]/text()').map(x => x.wholeText.trim())
```

para filtrar una consulta ya filtrada
```xpath
$x(' (//span[@class="text"]) [4]')
```

## Wildcards

Comodín | ejemplo | Salida
------- | ------- | ------
\* | `/html/*` | (2) [head, body]
\* | `//*` | (151) [html, head, meta, ...]
\* | `//span[@class="text"]/@*` | (20) [class, itemprop, class, ...]
\* | `/html/body//div/@*` | (48) [class, class, class, ...]
node() | `//span[@class="text"]/node()` | Matches any node of any kind

## In-text search

Algunos solo funcionan a partir de Xpath 2.0

Comando | ejemplo | Explicación ejemplo
------- | ------- | -----------
starts-with() | `//small[starts-with(., "Albert")]` | Busca en el texto
ends-with() | `//small[starts-with(text(), "Albert")]` | Busca en el texto
contains() | `//small[contains(@class, "author")]` | Busca en los atributos
matches() | `//small[matches(., "A.*n")]` | Regex

# Axes

Parent, children, siblings, ancestors and descendants

Comando | ejemplo | Explicación
------- | ------- | -----------
self::div | `/html/body/div/self::div` | sintax sugar "."
child::* | `/html/body/div/child::*` | nodos hijos de todo tipo
descendant::text() | `/html/body/div/descendant::text()` | texto de nodos descendentes
descendant-or-self::div | `/html/body/div/descendant-or-self::div` | 

[XPath Axes W3Schools](https://www.w3schools.com/xml/xpath_axes.asp)

![](https://gyires.inf.unideb.hu/GyBITT/03/images/xpath-tengelyek.png)