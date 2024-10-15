#include <iostream>
#include <type_traits>
#include <vector>
#include <cstdint>

class Superclass {

};

template <typename T>
class TemplatizedSubclass : public Superclass {
    static_assert(std::is_arithmetic_v<T>);
    public:
        T member;
        TemplatizedSubclass(T value) : member{value} {}
};

int main () {
    std::vector<Superclass> v;
    TemplatizedSubclass<uint64_t> intMetric(1);
    TemplatizedSubclass<float> floatMetric(1.0);
    v.push_back(intMetric);
    v.push_back(floatMetric);
    for (Superclass& s : v) {
        /*
        Right so here's the problem: for this kind of thing to compile, Superclass has to define all the
        operations we might want to use, because we're working on a Superclass, and we don't know that
        it is actually a TemplatizedSubclass (by design, since we're trying to hide the template!). We can't
        use anything that relies on knowing T. That's tough to deal with w.r.t. T's own functionality, and
        impossible when it's type-specific logic in another class, e.g. a stringstream's overloaded
        operator<<.
        */
        std::cout << s << ", ";
    }
    std::cout << std::endl << std::flush;
}