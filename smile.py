eyeSymbols = {"^": "xor", "-": "sub",
              "*": "mul", "+": "add",
              "%": "mod", "/": "div",
              "&": "and",
              "<": ("__lt__","__rt__")} # TODO: support <_<

# Note: < doesn't actually work, but only because of chained comparisons
# If there were any operators that didn't follow the __foo__, __rfoo__
# pattern, that "<": ("__lt__", "__rt__") thing is how you'd handle it

class Mouth(object): # the singleton mouth object _
    pass
class LeftFace(object): # a half-evaluated emoticon, like 5 ^_
    def __init__(self, leftEye, leftarg):
        self.leftEye, self.leftarg = leftEye, leftarg
        
for eye, functionName in eyeSymbols.items(): # note: fuck late binding
    if type(functionName) in (list, tuple):
        leftFunctionName, rightFunctionName = functionName
    else:
        leftFunctionName = "__"+functionName+"__"
        rightFunctionName = "__r"+functionName+"__"
        
    setattr(Mouth, rightFunctionName, # good luck figuring out
            lambda self, leftarg, eye=eye:LeftFace(eye, leftarg))
    setattr(LeftFace, leftFunctionName, # THIS code
            lambda self, rightarg, eye=eye: # bitches
                emoticon.function[self.leftEye+"_"+eye](self.leftarg, rightarg))

_ = Mouth()

class EmoticonDB(object): # omg singleton class for storing emoticon functions
    def __init__(self):
        self.function = {}
    def __call__(self, face):
        def addToDatabase(f):
            self.function[face] = f
        return addToDatabase

emoticon = EmoticonDB()
