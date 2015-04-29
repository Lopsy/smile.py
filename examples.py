from smile import emoticon, _



def testSmile():
    import itertools
    
    @emoticon("^_^") # This creates the operator ^_^ globally!
    def smile(a, b):
        return itertools.chain(a,b)

    # Now ^_^ is an infix iterator chainer!!! ^_^

    funIterator = [1,2,3] ^_^ xrange(10,20,5) ^_^ {"apple":1, "banana":4}
    assert list(funIterator) == [1, 2, 3, 10, 15, "apple", "banana"]



def testMixedFace():
    
    @emoticon("-_+")
    def lcm(a, b): # -_+ is lcm operator. Again, overrides globally!
        product = a*b
        while b != 0:
            a, b = b, a%b
        return product/a

    chainLCM = 2 -_+ 12 -_+ 27 -_+ 5
    assert chainLCM == 540

    @emoticon("-_^")
    def lcm(a, b): return a -_+ b

    # mixed faces are harder, because 2 -_^ 12 -_^ 27 is evaluated as
    # ((2 - _) ^ (12 - _)) ^ 27
    # The problem is, the eyes have a different operator precedence.
    # Protip: don't chain mixed faces without parentheses.
    try:
        chainLCM = 2 -_^ 12 -_^ 27 -_^ 5
        if chainLCM == 540:
            print "Wow, this shouldn't have worked but it did"
        else:
            assert False
    except TypeError:
        chainLCM = (2 -_^ 12) -_^ (27 -_^ 5)
        assert chainLCM == 540


def testLeftEyes():
    # TODO: make this test work
    # right now it fails because of chained comparisons:
    # (5 <_< str) is evaluated as (5 < _) and (_ < str)
    # Should be easy to fix!

    @emoticon("<_<")
    def leftGlance(obj, f):
        return f(obj)

    five = 5 <_< str
    assert five == "5"
