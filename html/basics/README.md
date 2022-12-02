# HTML5
Hyper Text Markup Language or called HTML for short is a markup language
used to structure a web page semantically, this mean that HTML isn't based
on design with beautiful colors, in other hand this is for meaningful text
structure.

## Standard 
The standard means that organization are met to created the features of
HTML that all the user or implementers following to create a only one
HTML.

[Living Standard](https://html.spec.whatwg.org/multipage/) 
 
## Basic Structure
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Basic Structure</title>
    </head> 
    <body></body>
</html>
```

The basic structure is composed of **tags**.
## Tags 
A tag is a label for elements, this means that a label is a container of
any elements in it, a metaphor of this is a jar with a tag of strawberries jam. 
How a jar this has an jar container and lid this is called open and close tags
in HTML, so to define a tag you need open tag and close tag to defined an 
element you need first enclosed the tag name in an less than and greater 
than symbol.

To close the tag there is two forms when the element is void, this mean that 
don't have a content, this is know as **self-closing** tag you need put a
slash before the name of the tag. And the other form is where the tag has
some value. 


```html
<meta/>
<p>content</p>
```

The tag can have attributes, this attributes are in the first tag. An 
attribute has a attribute name with an attribute value separated with a
equals. 

```html
<button target=_blank ></button>
``` 

The attribute value is _blank and the attribute name is target. 
>In HTML5 the attribute value doesn't require has enclosed between a quotation marks,  and also doesn't require the slash and the end of close tag. 

## Check your HTML 
There a page to check your HTML with the standard. [Checker](https://validator.w3.org/)


## Doctype
The doctype specified the document type for old browsers for reasons of 
compability. Without it the browser can interprate a but specification.
The doctype is case-insensitivy, this means that there isn't problem 
with all in lower case.

```html
<!DOCTYPE html>
```

## The a tag
The anchor tag is the most important tag of the web because this is the
hyperlink to another pages, the web is created with hyperlinks. 

```html
<a href="https://www.w3.org/">W3C</a>
```

## Semantic in HTML5
The semantic is the meaning of the text, in other words a meaningful structure
that be self-explanatory.

## Section Elements
### The `main` tag
The content of the main tag is a unique information of your page, that 
isn't find in another page, this tag must be appear only once in the 
structure. 

```html
<main></main>
```

### The `section` tag
The section tag is used how generic section wrapper, this means that if
you can create a section for news information you can do it with this tag,
but if the purposes of group is only visual you can use `div` instance.

```html
<section></section>
``` 

### The `nav` tag
This tag is for group navigation links to section of the same page or 
another pages, you can add one or multilpes `a` tag to the links wrapper by a `nav` tag.

```html
<nav>
    <a href="https://github.com/camilo-camargo">My GitHub</a>
</nav>
```

### The `article` tag
In the article tag can wrapper a whole lump of another page, or in other words
can wrap a block or news stories. So the content of this wrapper is
reusable for another pages. If you create a children element of more articles
this means that this child articles are related with the parent.

```html
<article>

</article>
```
### The `aside` tag
The aside tag is used to has a relationship to the content around it. This
can be an advertising.

```html
<aside>
</aside>
``` 
### The `header` tag
The header tag is used how introductory content of an article or another
element, we can use it many times on the page.
```html
<header></header>
```

### The `footer` tag
This is used for represents information about the author, but not the 
information of contacting he, related documents and the like.

```html
<footer>
</footer>
```


### Headings

### The HTML Outline Algorithm
This is algorithms tell us that the level of the heading items are related
with the actual section that is contained. You can check it with the 
following outliners.
[HTML5 Outliner](https://gsnedders.html5.org/outliner/)
[HTML5 Outliner GitHub](https://hoyois.github.io/html5outliner/)

