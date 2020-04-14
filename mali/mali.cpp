using namespace std;
#include <string>
#include <sstream>
#include <vector>
#include <iostream>



int main() {
    int numCases;
    scanf("%d", &numCases);

    int min_a = -1;
    int min_b = -1;
    int max_a = 0;
    int max_b = 0;


    for (int i = 0; i < numCases; i++) {
        int num1, num2;

        scanf("%d", &num1);
        scanf("%d", &num2);

        min_a = (min_a == -1 || num1 < min_a) ? num1 : min_a;
        min_b = (min_b == -1 || num2 < min_b) ? num2 : min_b;

        max_a = (num1 > max_a) ? num1 : max_a;
        max_b = (num2 > max_b) ? num2 : max_b;

        int pot1 = max_a + min_b;
        int pot2 = min_a + max_b;

        int biggest = (pot1 > pot2) ? pot1 : pot2;

        cout << biggest << "\n";

    }
}
