
a = "ABcdefGhiJKlmNOpQrStUvwXYz"
a1=a.lower()
print(a1)
a2=a.upper()
print(a2)
print(a.isalnum())
print(a.isalpha())
print(a2.islower())
print(a2.isupper())

b = "      Maitri Sheta Vishalbhai    "
print(b)
print(b.rstrip(" "))
print(b.lstrip(" "))
print(b.split(" "))
print(b.count("a"))

c = "Mitu"
print(c.replace("iru", "aitri"))

d="mAiTRI"
d1=(d.capitalize())
print(d1)
print(d1.center(50))
print(d1.center(50,"."))

e="maitrisheta@gmail.com"
print(e)
print(e.endswith("@gmail.com"))
print(e.startswith("maitri"))
print(e.find("@gmail"))
print(e.index(".com"))

f="          "
print(f.isspace())

g="Sheta Maitri"
print(g.istitle())#return true only if all first letter is capital
print(g.swapcase())
g="sheta Maitri"
print(g.title())
