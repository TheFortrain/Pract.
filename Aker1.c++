#include <iostream>

// Directive to increase stack size
#pragma comment(linker, "/STACK:10000000000")

unsigned int A(unsigned int n, unsigned int m)
{
    if (n == 0)
        return m + 1;
    else
        if ((n != 0) && (m == 0))
            return A(n - 1, 1);
        else
            return A(n - 1, A(n, m - 1));
}

int main()
{
    // Example: A(4, 0)
    unsigned int res = A(4, 0);
    std::cout << "Result of A(4, 0) = " << res << "\n";

    system("pause");
    return 0;
}
