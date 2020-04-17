#include <string>
using namespace std;
#include <iostream>


int main() {

    int numTypes;
    scanf("%d", &numTypes);

    cout << numTypes;

    int numPages[numTypes];

    for (int i = 0; i < numTypes; i++) {
        scanf("%d", &numPages[i]);
        cout << numPages[i];
    }

    for (int i = 0; i < numTypes; i++)
        cout << numPages[i];
}
