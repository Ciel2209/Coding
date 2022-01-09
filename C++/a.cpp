#include <iostream>
using namespace std;

int main() {
    int n,k,d,ib;
    ib = 0;
    cout << "Tim kiem so k trong day so nguyen A co N chu so \n";
    cout << "N="; cin >> n;
    int a[n], b[n];
    cout << "k="; cin >> k;
    cout << "Nhap day so A: \n";
    for (int ia = 0; ia<n; ia++) {
        cin >> a[ia];
        if (a[ia] = k) {
            d++;
        }
    }
    cout << "Trong day so nguyen A co " << d << " chu so bang " << k;
    return 0;
}
