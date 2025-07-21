#include <iostream>
using namespace std;

int arr[100][100];

int main() {
    int n, m;
    int num = 0;

    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> arr[i][j];
        }
        sort(arr[i], arr[i] + m); // 각 행별로 정렬
    }

    // 행의 가장 작은 값 중 가장 큰 값 구하기
    for (int i = 0; i < n; i++) {
        num = num < arr[i][0] ? arr[i][0] : num;
    }

    cout << num;

    return 0;
}
