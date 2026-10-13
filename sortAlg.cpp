#include <iostream>
using namespace std;

int main() {
    int n, v[100];

    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }

    for (int i = 0; i < n - 1; i++) {
        int poz = i;

        for (int j = i + 1; j < n; j++) {
            if (v[j] < v[poz]) {
                poz = j;
            }
        }

        swap(v[i], v[poz]);
    }

    for (int i = 0; i < n; i++) {
        cout << v[i] << " ";
    }

    return 0;
}
