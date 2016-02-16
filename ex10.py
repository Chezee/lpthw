tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non the line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
\a Something
I dont know\bsm
\f dont know
\r new
\v wtf is this
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,