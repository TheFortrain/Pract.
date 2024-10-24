#include <iostream>

// Директива для збільшення розміру стеку
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
    // Приклад: A(5, 1)
    unsigned int res = A(5, 1);
    std::cout << "Результат A(5, 1) = " << res << "\n";

    system("pause");
    return 0;
}
