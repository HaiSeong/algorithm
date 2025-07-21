#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;

    cin >> s;

    string front = s.substr(0, s.length() / 2);
    string back = s.substr(s.length() / 2, s.length() / 2);

    int front_num = 0;
    int back_num = 0;
    for (int i = 0; i < front.length(); i++) {
        front_num += front[i] - '0';
        back_num += back[i] - '0';
    }

    if (front_num == back_num) {
        cout << "LUCKY";
    } else {
        cout << "READY";
    }

    return 0;
}