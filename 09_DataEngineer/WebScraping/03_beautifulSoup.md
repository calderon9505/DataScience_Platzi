# BeautifulSoup

[Beautiful Soup Documentation](https://beautiful-soup-4.readthedocs.io/en/latest/)

```py
from bs4 import BeautifulSoup
```

Partiendo de un objeto `str` que contenga el HTML (**html_doc** en este caso) se obtiene el objeto `BeautifulSoup`, el cual representa el documento como una estructura de datos anidada.

```py
soup = BeautifulSoup(html_doc, 'html.parser')
```

Para navegar en la estructura de datos se usan las etiquetas del HTML: 

Command | Objeto | Output or Description
------- | ------ | ------
`soup.tag` | `bs4.element.Tag` | Selecciona el tag especificado
`tag.name` | `str` | Nombre del tag.
`tag.string` | `bs4.element.NavigableString` | Contenido del tag.
------- | ------ | ------
`tag.attrs` | `dict` | Atributos del tag.
`tag['attr']` | `list` | Atributo del tag. `KeyError` si no existe.
`tag.get('attr')` | `str` | Atributo del tag. `None` si no existe.
------- | ------ | ------
`tag.parent` | `bs4.element.Tag` | Tag padre.
`tag.parents` | `generator` | Tags padre.
`tag.contents` | `list` | Tags hijos.
`tag.children` | `list_iterator` | Tags hijos.
`tag.descendants` | `generator` | Tags descendentes.
`tag.strings` | `generator` | Contenido de tags hijos. Usar `repr()`
`tag.stripped_strings` | `generator` | Contenido tags hijos without extra whitespace.
------- | ------ | ------
`tag.next_sibling` | `bs4.element.Tag` or `str` | Tag o string hermanos
`tag.previous_sibling` | `bs4.element.Tag` or `str` | Tag o string hermanos
`tag.next_siblings` | `generator` | Tags hermanos. Usar `repr()`
`tag.previous_siblings` | `generator` | Tags hermanos. Usar `repr()`
`tag.next_element` | `bs4.element.Tag` or `str` | Tag o string siguiente.
`tag.previous_element` | `bs4.element.Tag` or `str` | Tag o string previo.
`tag.next_elements` | `generator` | Tags o strings siguientes.
`tag.previous_elements` | `generator` | Tags o strings previos.
------- | ------ | ------
`soup.find_all()` | `bs4.element.ResultSet` | Se explica más adelante.
`soup.find()` | `bs4.element.Tag` | Igual que `find_all()`
`soup.get_text()` | `str` | Todo el texto de la página


### *Multi-valued attributes*

Un tag puede tener más de un atributo `class` (```<p class="body strikeout"></p>```), pero no más de un atributo `id`.

Puedo crear o modificar atributos on `tag['attr']`.

Puedo usar `multi_valued_attributes=None` como parámetro dentro de `BeautifulSoup()` para deshabilitar el uso de atributos multi-valuados.

Puedo usar `.get_attribute_list` despues de un tag para obtener los atributos como listas, incluso si no es multi-valuado.

Si el documento es XML, no existen atributos multi-valuados. Pero se puede usar `multi_valued_attributes=class_is_multi`

### NavigableString

A `NavigableString` is just like a Python Unicode string, except that it also supports **some** of the features described in `Navigating the tree` and `Searching the tree`.

You can convert a `NavigableString` to a Unicode string with `unicode()`.

You can’t edit a string in place, but you can replace one string with another, using `replace_with()`.

# `Find_all()`

```py
soup.find_all(name, attrs, recursive, string, limit, **kwargs)
```

`mytag.find_all()` examine all the descendants of `mytag`.

`_tag` es cualquier tag. `_attr` es cualquier atributo. `_something` is a string, a regular expression, a list, a function, or the value True.

The value to `name` can be `_something`. You can filter an attribute based on `_something`

Some attributes, like the `data-foo` attributes in HTML 5, have names that can’t be used as the names of keyword arguments. You can use these attributes in searches by putting them into a dictionary `{"data-foo": "value"}`.

You can’t use a keyword argument to search for HTML’s `name` element, because Beautiful Soup uses the name argument to contain the name of the tag itself. Instead, you can give a value to `name` in the attrs argument `{"name": "email"}`.

The name of the CSS attribute, `class`, is a reserved word in Python. You can search by CSS class using the keyword argument `class_` or with a dictionary. Remember that a single tag can have multiple values for its `class` attribute. When you search for a tag that matches a certain CSS class, you’re matching against any of its CSS classes:

With `string` you can search for strings instead of tags. You can pass in `_something`.

If you call `mytag.find_all()`, Beautiful Soup will examine all the descendants of `mytag`: its children, its children’s children, and so on. If you only want Beautiful Soup to consider direct children, you can pass in `recursive=False`.

Command |  Description
------- | ------
`find_all('_tag')` |  Tags with the exact string.
`find_all(['_tag1','_tag2'])` |  Tags with the exact strings.
`find_all(re.compile("regex"))` |  Tags with the regex matches.
`find_all(True)` |  All the tags, but none of the text strings.
`find_all(function)` | function that returns `True` or `False`
------- | ------
`find_all(_attr= _something)` |  
`find_all(_attr1=_something, _attr2=_something)` |  Tags with two attributes matches
`find_all(attrs={"_attr": _something})`|  Tags with the attributes matches.
`find_all(string=_something)`|  Tags with the attributes matches.
`find_all('_tag', limit=_number)`|  Limits the output.
`find_all('_tag', recursive=False)`|  Consider direct children.
------- | ------

Because `find_all()` is the most popular method in the Beautiful Soup search API, you can use a shortcut for it. `soup.find_all("_tag")` is equivalent to `soup("_tag")`.

### Regex

```py
import re
soup.find_all(href=re.compile("elsie"))
```

### Function

```py
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

soup.find_all(has_class_but_no_id)
```

The function can be as complicated as you need it to be

# `Find()`

If you know a document only has one `_tag`, it’s a waste of time to scan the entire document looking for more. Rather than passing in limit=1 every time you call find_all, you can use the find() method.

`soup.find_all('title', limit=1)` is equivalent to `soup.find('title')`

The only difference is that `find_all()` returns a list containing the single result, and `find()` just returns the result.

If `find_all()` can’t find anything, it returns an empty list. If `find()` can’t find anything, it returns None.

Navigating using tag names is equivalent to use `find()` repeatedly. `soup.head.title` is equivalent to `soup.find("head").find("title")`

# Other functions

I spent a lot of time above covering `find_all()` and `find()`. The Beautiful Soup API defines ten other methods for searching the tree, but don’t be afraid. Five of these methods are basically the same as `find_all()`, and the other five are basically the same as `find()`. The only differences are in what parts of the tree they search.

* `find_parents()`
* `find_parent()`
* `find_next_siblings()`
* `find_next_sibling()`
* `find_previous_siblings()`
* `find_previous_sibling()`
* `find_all_next()`
* `find_next()`
* `find_all_previous()`
* `find_previous()`

# CSS selector

[A fun game to help you learn and practice CSS selectors.](https://flukeout.github.io/)

```py
soup.select(' ')
```

Command |  Description
------- | ------
`A` | **Type Selector**. Select elements by their type.
`#id` | **ID Selector**. Select elements with an ID.
`A B` | **Descendant Selector**. Select an element inside another element.
`#id A` | Combine any selector with the **descendent selector**.
`.classname` | **Class Selector**. Select elements by their class.
`A.classname` | Combine the **class selector** with other selectors.
`A B.classname` | Combine any selector with the **descendent** and the **class selector**.
`A, B` | **Comma Combinator**. Combine selectors with commas.
`*` | **The Universal Selector**. select everything.
`A *` | Combine the **The Universal Selector**.
`A + B` | **Adjacent Sibling Selector**. Select an element that directly follows another element.
`A ~ B` | **General Sibling Selector**. Select elements that follows another element.
`A > B` | **Child Selector**. Select direct children of an element.
`:first-child` | **First Child Pseudo-selector**. Select a first child element inside of another element.
`:only-child` | **Only Child Pseudo-selector**. Select an element that are the only element inside of another one.
`:last-child` | **Last Child Pseudo-selector**. Select the last element inside of another element.
`:nth-child(A)` | **Nth Child Pseudo-selector**. Select an element by its order in another element.
`:nth-last-child(A)` | **Nth Last Child Selector**. Select an element by its order in another element, counting from the back.
`:first-of-type` | **First of Type Selector**. Select the first element of a specific type.
`:nth-of-type(A)` | **Nth of Type Selector**. Selects a specific element based on its type and order in another element (or even or odd).
`:nth-of-type(An+B)` | **Nth-of-type Selector with Formula**.
`:only-of-type` | **Only of Type Selector**. Select elements that are the only ones of their type within of their parent element.
`:last-of-type` | **Last of Type Selector**. Select the last element of a specific type.
`:empty` | **Empty Selector**. Select elements that don't have children.
`:not(X)` | **Negation Pseudo-class**. Select all elements that don't match the negation selector.
`[attribute]` | **Attribute Selector**. Select all elements that have a specific attribute
`[attribute="value"]` | **Attribute Selector**. Select all elements that have a specific attribute value
`[attribute^="value"]` | **Attribute Starts With Selector**. Select all elements with an attribute value that starts with specific characters.
`[attribute$="value"]` | **Attribute Ends With Selector**. Select all elements with an attribute value that ends with specific characters.
`[attribute*="value"]` | **Attribute Wildcard  Selector**. Select all elements with an attribute value that contains specific characters anywhere.
`A[attribute]` | Combine the **attribute selector** with another selector.



```py

```