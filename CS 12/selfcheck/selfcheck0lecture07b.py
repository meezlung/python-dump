class A:
    def f(self):
        print("A's f was called")
 
    def g(self):
        print("A's g was called")
 
    def g2(self):
        print("A's g2 was called")
        self.g() 
 
class B(A):
    def g(self):
        print("B's g was called")
 
    def h(self):
        print("B's h was called")
        super().f()
        super().g()
        self.f()
        self.g()
 
class C(B):
    def g(self):
        print("C's g was called")
 
# b = B()
# b.f() # "A's f was called"
# b.g() # "B's g was called"
# b.h() # "B's h was called", "A's f was called", "A's g was called", "A's f was called", "B's g was called"
# b.g2() # "A's g2 was called", "B's g was called"
# print('---')
 
c = C()
 
c.f() # "A's f was called"
c.g() # "C's g was called"
c.h() # "B's h was called", "A's f was called", "A's g was called", "A's f was called", "C's g was called"
c.g2() # "A's g2 was called", "C's g was called"