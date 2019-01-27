# neild.wordsearch

Random wordsearch generator, using random words pulled from an online dictionary.

# Clone and run

    git clone https://github.com/n768d465/neild.wordsearch
    cd src
    python src/wordsearch_generator.py

# Sample output

    h c l i h o k c g v
    g e v x p y a t i d
    l f b k e p u h a o
    a d i d r s t s p m
    s e q k b r o n c o
    s c x j b e c v v a
    w i h k b p r g i t
    a b s y k i a n g l
    r e r m e c c a i c
    e l g j g f y t l e

    {'bernie', 'vigil', 'glassware', 'decibel', 'autocracy', 'tid', 'ernie', 'gnat', 'keg', 'bronco'}

You can also specify a wordsearch size and whether or not to allow to fill the board with random characters

    python wordsearch_generator.py --dim=8 --no-fill
                
    p           m
    t o s h i b a
        m       r
    p u r p o r t
        e   e   i
        a   t i n
        m   c   i
    {'etc', 'pompeii', 'purport', 'ream', 'toshiba', 'martini'}