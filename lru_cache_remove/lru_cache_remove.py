from caching import lru_cache_custom

class X:
    a = 1

    @lru_cache_custom(maxsize=100)
    def t(self, n):
        print("calc")
        return self.a + n


x = X()
print(x.t(3))
x.a = 9
print(x.t(3))
x.t.remove(3)
print(x.t(3))
x.t.remove(x, 3)
print(x.t(3))