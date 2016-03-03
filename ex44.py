class Parent(object):
    def override(self):
        print "Parent overrided()"
        
    def implicit(self):
        print "Parent implicit()"
        
    def altered(self):
        print "Altered way of Parent"
        

class Child(Parent):
    def override(self):
        print "Child overrided()"

    def altered(self):
        print "Altered way of Child"
        print "Alter after Suped command: "
        
    def superaltered(self):
        super(Child, self).altered()    

         
dad = Parent()
son = Child()
dad.implicit()
son.implicit()
dad.override()
son.override()
dad.altered()
son.altered()
son.superaltered()