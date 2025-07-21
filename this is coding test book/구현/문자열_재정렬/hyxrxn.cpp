#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    string s;

    cin >> s;

    string alphabet = "";
    int num = 0;
    for (int i = 0; i < s.length(); i++) {
        char dummy = s[i];
        if (dummy >= '0' && dummy <= '9') {
            num += dummy - '0';
        } else {
            alphabet += dummy;
        }
    }

    sort(alphabet.begin(), alphabet.end());

    cout << alphabet << num;

    return 0;
}