#include <iostream>
using namespace std;

int main() {
    int row, col;
    string input;
    int num = 0;

    cin >> input;
    row = input[0] - 'a' + 1; // 숫자로 변경
    col = input[1] - '0';

    if (row - 2 >= 1) { // 먼저 2칸 위로 이동했을 때
        if (col - 1 >= 1) num++;
        if (col + 1 <= 8) num++;
    }

    if (row + 2 <= 8) { // 먼저 2칸 아래로 이동했을 때
        if (col - 1 >= 1) num++;
        if (col + 1 <= 8) num++;
    }

    if (col - 2 >= 1) { // 먼저 2칸 왼쪽으로 이동했을 때
        if (row - 1 >= 1) num++;
        if (row + 1 <= 8) num++;
    }

    if (col + 2 <= 8) { // 먼저 2칸 오른쪽으로 이동했을 때
        if (row - 1 >= 1) num++;
        if (row + 1 <= 8) num++;
    }

    cout << num;

    return 0;
}