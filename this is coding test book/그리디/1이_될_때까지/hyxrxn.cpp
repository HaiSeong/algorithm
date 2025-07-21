#include <iostream>
using namespace std;

int main() {
    int n, k;
    int num = 0;

    cin >> n >> k;

    while (n != 1) {
        if (n % k == 0) { // k의 배수라면 나누기
            n /= k;
        } else { // 아니라면 빼기
            n -= 1;
        }
        num++;
    }

    cout << num;

    return 0;
}