#include <iostream>
using namespace std;

int main() {
    string s;
    int num = 0;

    cin >> s;

    // 숫자가 변하는 횟수 세기
    char dummy = s[0] - '0';
    for (int i = 1; i < s.length(); i++) {
        if (s[i] - '0' != dummy) {
            num++;
            dummy = s[i] - '0';
        }
    }

    // 가장 바깥부터 차례대로 뒤집기
    if (num % 2 == 0) {
        num /= 2;
    } else {
        num /= 2;
        num++;
    }

    cout << num;

    return 0;
}