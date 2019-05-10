Wordsearch Generator
====================

Random wordsearch generator, using random words pulled from an online dictionary.

Clone
-----

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

You can also specify a wordsearch size and whether or not to allow to fill the board with random characters

.. code-block:: python

    from wordsearch_generator import WordSearchGenerator

    ws = WordSearchGenerator(dim=8, max_word_length=4, fill=False)
    ws.make_wordsearch()

    ...

          g a m    
      c            
        a a u g   f
    c r t g   f   a
      i c y e a   l
              r n l
    h o l t   e b  
    b a l m     c  

    Word bank
    ---------
    balm cage nbc gam holt fall fare icy crt aug