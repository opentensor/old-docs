
part: Documentation
title: Markdown Usage
description: While this is not a complete markdown reference, here are markdown features that you can use right away in your books.
tags: [markdown, reference, NextBook, md]
updated: '2021-03-14'


## Front Matter

YAML front matter can be used to add title, description, part info, tags and update date to your pages. This page includes a front matter like this:

```yaml nocopy

part: Documentation
title: Markdown Usage
description: While this is not a complete markdown reference, here are markdown features that you can use right away in your books.
tags: [markdown, reference, NextBook, md]
updated: '2021-03-14'

```

## HTML Tags

Markdown allows using html tags except scripts. This way you can use modern html5 tags, embed audio and video and everything else not covered by standard markdown.

## Text Manipulation

```text nocopy
**This is bold text**

_This is italic text_

**_This is bold italic text_**

~This is strikethrough text~

Superscript: 19<sub>th</sub>

Subscript: H<sub>2</sub>O

This is <mark>highlighted</mark> text.
```
results in:

**This is bold text**

_This is italic text_

**_This is bold italic text_**

~~This is strikethrough text~~

Superscript: 19<sub>th</sub>

Subscript: H<sub>2</sub>O

This is <mark>highlighted</mark>

## Horizontal Lines

Both of these work:

```text nocopy

***
```
results in:


***

## Blockquotes

```text nocopy
> Here is a blockquote.

> Blockquotes can also be nested...
>
> > ...by using additional greater-than signs right next to each other...
> >
> > > ...or with spaces between arrows.
```
results in:

> Here is a blockquote.

> Blockquotes can also be nested...
>
> > ...by using additional `greater-than` signs right next to each other...
> >
> > > ...or with spaces between arrows.

## Footnotes

```text nocopy
Footnote 1 link. [^first]

Footnote 2 link. [^second]

[^first]: Footnote **can have markup**.

[^second]: Simple footnote text.
```
results in:

Footnote 1 link. [^first]

Footnote 2 link. [^second]

[^first]: Footnote **can have markup**

[^second]: Footnote text.

## Code

A special care was given to displaying code on screen.

### Inline Code

~~~text nocopy
`$ rm -rf /`
~~~
results in: `$ rm -rf /`

### Fenced Code Blocks

Most of the time you'll use codefences. Here is a simple example, but you can do a lot more with them. For advanced fenced code block usages, see [Fenced Code](/reference/fencedcode) chapter.

````text nocopy
```bash
#!/bin/bash
echo "Hello World"
```
````
results in:

```bash nocopy
#!/bin/bash
echo "Hello World"
```

## Lists

### Unordered List

```text nocopy
- Create a list by starting a line with +, -, or *
- Sub-lists are made by indenting 2 spaces:
  - Marker character change forces new list start:
    * Facilisis in pretium nisl aliquet
    - Nulla volutpat aliquam velit
+ Very easy!
```
results in:

- Create a list by starting a line with `+`, `-`, or `*`
- Sub-lists are made by indenting 2 spaces:
  - Marker character change forces new list start:
    * Facilisis in pretium nisl aliquet
    - Nulla volutpat aliquam velit
+ Very easy!

### Ordered List

```text nocopy
1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa
4. You can use sequential numbers...
1. ...or keep all the numbers as `1.`
```
results in:

1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa
4. You can use sequential numbers...
1. ...or keep all the numbers as `1.`

## Checkboxes

These are often used to indicate task items.

```text nocopy
- [x] Clone repo
- [x] Create some pages
- [ ] Commit & Push
- [ ] Deploy!
```
results in:

- [x] Clone repo
- [x] Create some pages
- [ ] Commit & Push
- [ ] Deploy!

## Tables

Tables are a bit tricky, because you have to use all those pipes, but this is how markdown was designed. Using a special markdown editor like [Typora](https://typora.io/) will make your life easier with these.

### Standard Columns

```
| Option | Description                                                 |
| ------ | ------------------------------------------------------------|
| data   | path to data files to supply the data passed into templates.|
| engine | engine to be used for processing templates.                 |
| ext    | extension to be used for dest files.                        |
```
results in:

| Option | Description                                                 |
| ------ | ------------------------------------------------------------|
| data   | path to data files to supply the data passed into templates.|
| engine | engine to be used for processing templates.                 |
| ext    | extension to be used for dest files.                        |

### Right Aligned Columns

```
| Option | Description                                                   |
| -----: | ------------------------------------------------------------: |
| data   | path to data files to supply the data passed into templates.  |
| engine | engine to be used for processing templates.                   |
| ext    | extension to be used for dest files.                          |
```
results in:

| Option | Description                                                   |
| -----: | ------------------------------------------------------------: |
| data   | path to data files to supply the data passed into templates.  |
| engine | engine to be used for processing templates.                   |
| ext    | extension to be used for dest files.                          |

### Mixed Columns

```
| Left-aligned | Center-aligned | Right-aligned |
| :----------- | :------------: | ------------: |
| git status   | git status     | git status    |
| git diff     | git diff       | git diff      |
```
results in:

| Left-aligned | Center-aligned | Right-aligned |
| :----------- | :------------: | ------------: |
| git status   | git status     | git status    |
| git diff     | git diff       | git diff      |

## Images

You will use images a lot! Drop your images or svg vectors in public folder and link to them. NextBook will autoscale them for small displays. You can add captions and `alt` information to your images.

```text nocopy
![The Octocat](/images/octocat.png)
![The Surface](/images/surface.jpg 'The Surface Device')
```
results in:

![he Octocat](/images/octocat.png)
![The Surface](/images/surface.jpg 'The Surface Device')

If you use [Excalidraw](https://excalidraw.com/) svg drawings and want them to change colors accordingly in dark mode, add `|ex` to image alt text. See below example in light/dark modes:

```
![Git Branching|ex](/images/git-branching.svg)
```

results in:

![Git Branching|ex](/images/git-branching.svg)

## Links

Links can be auto-detected, but it would be better to be implicit and have support other markdown tools. Also, all external links in your documentation will be autodetected and appropriate html code will be generated.

```
- [Basic link](https://github.com)
- [Link with title](https://github.com 'Github FTW')
- Autoconverted link https://github.com/remarkjs
- Cross page [absolute link](/nextbook/getting-started) for single page app navigation.
- Link to [part of a page](#links)
- Linking with image:
- [![Deploy with Vercel raw][1]][2]

[1]:  https://vercel.com/button
[2]:  https://vercel.com/new/git/external?repository-url=https%3A%2F%2Fgithub.com%2Famiroff%2FNextBook "Deploy With Vercel now!"

```
results in:

- [Basic link](https://github.com)
- [Link with title](https://github.com 'Github FTW')
- Autoconverted link https://github.com/remarkjs
- Cross page [absolute link](/nextbook/getting-started) for single page app navigation.
- Link to [part of a page](#links)
- Linking with image: [![Deploy with Vercel raw][1]][2]

[1]:  https://vercel.com/button
[2]:  https://vercel.com/new/git/external?repository-url=https%3A%2F%2Fgithub.com%2Famiroff%2FNextBook "Deploy With Vercel now!"


## Notifications

These are custom features often needed to display hints. I find them very useful.

### Hints

```
!> A Hint Title
Make sure to check out [Markdown Guide](https://www.markdownguide.org/) to check the basic markdown syntax you can use with NextBook.
```
results in:

!> A Hint Title
Make sure to check out [Markdown Guide](https://www.markdownguide.org/) to check the basic markdown syntax you can use with NextBook.

### Warnings

```
?> And Warning Title
Try to keep usage of html elements to rare cases where standard markdown does not cover your basic markup needs.
```
results in:

?> And Warning Title
Try to keep usage of html elements to rare cases where standard markdown does not cover your basic markup needs.

### Errors

```
x> An Error Title
Ooooops, an unknown error occured.
```
results in:

x> An Error Title
Ooooops, an unknown error occured.

## Emojis

Nothing fancy, just use native os supported 🥳 emoji characters or their text representations like `:partying_face:` for :partying_face:.
Press <kbd>control + command + space</kbd> on macOS and <kbd>windows + .</kbd> on Windows.

## Containers

### Accordion

``` markdown
<Accordion title="Toggle Me">
...and see my content
</Accordion>
```

<Accordion title="Toggle Me">
...and see my content
</Accordion>


?> Warning
Accordion component is not print compatible. Use responsibly.

### Tabs

While [markdown spec](https://commonmark.org) does not offer any tabbed interface, NextBook has you covered here. Use `tabs` and `tab` containers as follows:

``` markdown
<Tabs>
  <Tab title="Windows Directions">
      Install via [chocolatey](https://chocolatey.org):

      `choco install python`
  </Tab>
  <Tab title="macOS Directions">
      Install via [brew](https://brew.sh):

     `brew install python3`
  </Tab>
  <Tab title="Linux Directions">
      Install via apt:

      `sudo apt install python3`
  </Tab>
</Tabs>
```
results in:

<Tabs>
  <Tab title="Windows Directions">
    Install via [chocolatey](https://chocolatey.org):

    `choco install python`
  </Tab>
  <Tab title="macOS Directions">
    Install via [brew](https://brew.sh):

    `brew install python3`
  </Tab>
  <Tab title="Linux Directions">
    Install via apt:

    `sudo apt install python3`
  </Tab>
</Tabs>





part: Documentation
title: Fenced Code Block Usage


Oftentimes, you need to display a code example on the page. This example could be as simple as a one-liner or as complex as a diff view. Below are the ways you can use fenced code blocks with NextBook.

## Simple Fenced Block

Wrap your code using triple \``` characters for the simplest code formatting.

~~~
```
Everything within fenced code will
be displayed in monospace font.
```
~~~

results in:

```text nocopy
Everything within fenced code will
be displayed in monospace font.
```

## Syntax Highlighting

### Theme-Aware Highlighting

You can add syntax highlighting by specifying code's [language](https://prismjs.com/index.html#supported-languages) after triple ```. NextBook uses [PrismJS](https://github.com/PrismJS) for themes and language definitions as it is currently the most complete one.

When application's theme changes, so does the fenced code theme. Try it now by pressing <kbd>T</kbd>.

~~~
```jsx
import React, { useState } from 'react'

function Square(props) {
  const [value, setValue] = useState(null)

  return (
    <button className="square" onClick={() => alert('click')}>
      {props.value}
    </button>
  )
}
```
~~~

results in:

```jsx nocopy
import React, { useState } from 'react'

function Square(props) {
  const [value, setValue] = useState(null)

  return (
    <button className="square" onClick={() => alert('click')}>
      {props.value}
    </button>
  )
}
```

### Forced Dark Theme

You can force dark syntax highlighting even on light theme. Provide `dark` parameter to do that. Swith to light theme by pressing <kbd>T</kbd>. to see code block below still using dark theme.

~~~
```jsx dark
import React, { useState } from 'react'

function Square(props) {
  const [value, setValue] = useState(null)

  return (
    <button className="square" onClick={() => alert('click')}>
      {props.value}
    </button>
  )
}
```
~~~

results in:

```jsx dark nocopy
import React, { useState } from 'react'

function Square(props) {
  const [value, setValue] = useState(null)

  return (
    <button className="square" onClick={() => alert('click')}>
      {props.value}
    </button>
  )
}
```

## Clipboard Button

Any code block will have automatic `Copy` icon clicking which copies contents of code block to clipboard unless you pass `nocopy` meta value to code fence.

## Code Header Information

You can display various information like title and link to source in code header.

### Code Title

Often you need to tell which file you are talking about. You can specify this by adding `title` info:

~~~
```jsx title=somefolder/app.jsx
import React, { useState } from 'react'

function Square(props) {
  const [value, setValue] = useState(null)

  return (
    <button className="square" onClick={() => alert('click')}>
      {props.value}
    </button>
  )
}
```
~~~

results in:

```jsx title=somefolder/app.jsx nocopy
import React, { useState } from 'react'

function Square(props) {
  const [value, setValue] = useState(null)

  return (
    <button className="square" onClick={() => alert('click')}>
      {props.value}
    </button>
  )
}
```

### Linked Code Title

In case you need to link to original source you can pass `link` metadata. Now, title will be a link to the specified URL.

~~~
```python numbered title=colors/primary_colors.py link=https://github.com/geekcomputers/Python/blob/master/Colors/primary_colors.py
def diff(a, b):
    """
    TODO: fix this function!!
    """
    return a - b
```
~~~

results in:

```python numbered title=colors/primary_colors.py link=https://github.com/geekcomputers/Python/blob/master/Colors/primary_colors.py nocopy
def diff(a, b):
    """
    TODO: fix this function!!
    """
    return a - b
```

## Line Numbering

### Automatic Numbering

Lines of code can have automatic numbering. Provide `numbered` metadata to achive that:

~~~
```html numbered
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Document</title>
</head>
<body>
    <h1>Hello World!</h1>
</body>
</html>
```
~~~

results in:

```html numbered nocopy
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Document</title>
</head>
<body>
    <h1>Hello World!</h1>
</body>
</html>
```

### Numbering With Manual Offset

Code can start from any provided number. Use `numbered` together with `startline` metadata to achive that. Default startline is `1` unless provided.

~~~
```html numbered startline=3
<head>
    <meta charset='UTF-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Document</title>
</head>
```
~~~

results in:

```html numbered startline=3 nocopy
<head>
    <meta charset='UTF-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Document</title>
</head>
```

## Line Marking

In some cases there's a need to highlight/mark some lines and then describe each line seperately. Any number of lines can be marked by providing `marked` parameter:

~~~
```html marked=2,5,6,10
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Document</title>
</head>
<body>
    <h1>Hello World!</h1>
</body>
</html>
```
~~~

results in:

```html marked=2,5,6,10 nocopy
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Document</title>
</head>
<body>
    <h1>Hello World!</h1>
</body>
</html>
```

## Line Diffing

Sometimes you want to show which lines were added or removed from code. This can be achieved by passing related line numbers as `added` and `removed` parameters. Added lines will be highlighted with light green, removed lines with light red color. Note that displaying numbers, although works, in this case would cause a confusion as line numbers do not repeat.

~~~
```html removed=2,8 added=3,9,10
<!DOCTYPE html>
<html lang='en'>
<html lang='ja'>
<head>
...
</head>
<body>
    <h1>Hello World!</h1>
    <h1>こんにちは世界!</h1>
    <p>今日は天気がいいですね。</p>
</body>
</html>
```
~~~

results in:

```html removed=2,8 added=3,9,10 nocopy
<!DOCTYPE html>
<html lang='en'>
<html lang='ja'>
<head>
...
</head>
<body>
    <h1>Hello World!</h1>
    <h1>こんにちは世界!</h1>
    <p>今日は天気がいいですね。</p>
</body>
</html>
```

You can also pass every other parameter mentioned above together. Here we are adding some of them:

~~~
```html numbered marked=2,5,6,10 title=public/index.html link=https://gist.github.com/amiroff/04d57ef025845b191d9cd30c7ca13f20
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Document</title>
</head>
<body>
    <h1>Hello World!</h1>
</body>
</html>
```
~~~
results in

```html numbered marked=2,5,6,10 title=public/index.html link=https://gist.github.com/amiroff/04d57ef025845b191d9cd30c7ca13f20 nocopy
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Document</title>
</head>
<body>
    <h1>Hello World!</h1>
</body>
</html>
```

## Escaping Code Blocks

To escape (prevent from displaying as highlighted code) block and simply display how fenced code is being used in source, wrap it with `~~~`:

````
~~~
```html
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Document</title>
</head>
<body>

</body>
</html>
```
~~~
````
will result in:

~~~text nocopy
```html
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Document</title>
</head>
<body>

</body>
</html>
```
~~~



part: Documentation
title: Using MDX


## What Is MDX?

MDX to markdown is the same as JSX to JS. To quote the [original site](https://mdxjs.com/),

> MDX is an authorable format that lets you seamlessly write JSX in your Markdown documents. You can import components, such as interactive charts or alerts, and embed them within your content. This makes writing long-form content with components a blast 🚀.

... and this one:

> Writing is fun again when you combine components, that can even be dynamic or load data, with the simplicity of Markdown for long-form content.

Basically, renaming your `.md` file to `.mdx` gives you ability to import and use React components as if it was a normal React or Next.js app.

Here is a small demo video for curious:


<iframe
  width='100%'
  height='400'
  src='https://www.youtube-nocookie.com/embed/d2sQiI5NFAM'
  frameBorder='0'
  allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture'
  allowFullScreen
></iframe>

## Using Custom Components

Say we have a basic React counter component like this:

```jsx title=components/example-counter.jsx
import React, { useState } from 'react'
export default function Counter() {
  const [count, setCount] = useState(0)

  return (
    <div className='border border-gray-500 p-2 m-10 rounded-md bg-gray-700 text-gray-100'>
      <p>You clicked {count} times!</p>
      <button
        onClick={() => setCount(count + 1)}
        className='rounded border border-gray-500 bg-gray-900 p-1 mt-2'
      >
        Click me
      </button>
    </div>
  )
}
```

If you need to use components in your markdown content files, use `.mdx` extension, and provide any custom components through the `components/component-mapper.jsx` file. Then include it in your `.mdx` file and display it just like in React application:

``` markdown
### Example Counter Component
<Counter />
```

becomes:

### Example Counter Component
<Counter />

Voila! This way you can create dynamic components for your documentation like never before. Live code editors, quizes, exams, cheatsheets, comments, you name it. Possibilities are endless. Notice that you can use tailwindcss classnames in components for styling.

## More MDX Wizardry

For more information what can be achieved with MDX, see the [official site](https://mdxjs.com/).
