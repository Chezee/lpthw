class Other(object):
    def override(self):
        print "OTHER override"
    
    def implicit(self):
        print "OTHER implicit"
        
    def altered(self):
        print "OTHER altered"
        
class Child(object):
    def __init__(self):
        self.other = Other()
        
    def implicit(self):
        self.other.implicit()
        
    def override(self):
        print "Child override()"
        
    def altered(self):
        print "Child before super"
        self.other.altered()
        print "Child after super"
        
son = Child()

son.implicit()
son.override()
son.altered()