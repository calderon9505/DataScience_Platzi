# Xpath

Los tipos de nodos que se reconocen en una consulta XPath no son los tipos de nodos que se encuentran en el DOM.

[Extension de Chrome para xPath](https://chrome.google.com/webstore/detail/xpath-finder/ihnknokegkbpmofmafnkoadfjkhlogph)

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

## Expresiones

```xpath
$x('')
```
Expresion | ejemplo | descripción
--------- | ------- | -----------
/ | /html/body/div | root
// | //h1 | Anywhere
text() | //h1/a/text() | Texto de la etiqueta
.. | //span/.. | nodos padre
@ | //span/@class | atributo

## Predicados

Se usan dentro de corchetes `[ ]`. Se pueden usar operadores típicos de programación.

Predicado | ejemplo | descripción
--------- | ------- | -----------
1 | /html/body/div/div[1] | el div número uno
last() | /html/body/div/div[last()] | el último div
position() | /html/body/div/div[position()>4] | algunos div
@class | //span[@class] | filtrado por atributo `class`
@class=" " | //span[@class="text" or @class="tag-item] | filtrado más específico
not | //span[not(@class)] | negación


para ver el texto en la consola del navegador chrome
```xpath
$x('//span[@class="text"]/text()').map(x => x.wholeText)
```
para filtrar una consulta ya filtrada
```xpath
$x(' (//span[@class="text"]) [4]')
```

## Wildcards

Comodín | ejemplo | Salida
------- | ------- | ------
\* | /html/* | (2) [head, body]
\* | //* | (151) [html, head, meta, ...]
\* | //span[@class="text"]/@* | (20) [class, itemprop, class, ...]
\* | /html/body//div/@* | (48) [class, class, class, ...]
node() | //span[@class="text" and @itemprop="text"]/node() | (10) [text, text, ...]

## In-text search

Comando | ejemplo | Explicación
------- | ------- | -----------
starts-with() | //small[@class="author" and starts-with(., "A")]/text() | 
contains() | //small[@class="author" and contains(., "Ro")]/text() | 
ends-with() | //small[@class="author" and ends-with(., "A")]/text() | A partir de Xpath 2.0
matches() | //small[@class="author" and matches(., "A.*n")]/text() | Regex

# Axes

