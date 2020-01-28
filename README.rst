Wordsearch Generator
====================

Random wordsearch generator, using random words pulled from an online dictionary.

Clone
-----
::

    $ git clone https://github.com/n768d465/neild.wordsearch
    $ cd wordsearch

Examples
--------

.. code-block:: python

    from wordsearch_generator import WordSearchGenerator

    ws = WordSearchGenerator()
    ws.make_wordsearch()

    for row in ws.grid:
        print(" ".join(row))

    print("\nWord bank")
    print("---------")
    for word in ws.bank:
        print(word, end=" ")
    print()


This will produce the following output::

    i s n m r e s l m e
    p h o n e b e m r b
    c d u p l e x r v t
    o t x v m r t i k r
    s x i q i r o j j a
    e g n o m o n i o n
    t y b k m r l a x u
    g a u g u i n e i e
    y o h a n g v k t t
    d c k w e l c o m e

    Word bank
    ---------
    welcome error violet onion immune gnomon coset duplex sexton phone gauguin

You can also specify a wordsearch size, and a maximum word length.

.. code-block:: python

    from wordsearch_generator import WordSearchGenerator

    ws = WordSearchGenerator(dim=8, max_word_length=4)
    ws.make_wordsearch()
    ...

::

    c k r k g n a t
    e r r y l e i w
    r o h c e t e t
    c c a r r y d e
    o l i s r u g x
    t i j o c o i u
    q r t p x l p z
    g u y s x k b o

    Word bank
    ---------
    silo carr cork uri tang cot err echo ego tory 


If you want to show only the words within the grid, use `grid_words_only`.

.. code-block:: python

    ...
    for row in ws.grid_words_only:
        print(" ".join(row))
    ...

    l             h
    l   n a t s   y
    e w   l   z   d
    y t o u t   a e
      j s j a r   p
          p        
            a      
            f r o m

    Word bank
    ---------
    hyde jar jowl stan jolt paz tout yell spar from 