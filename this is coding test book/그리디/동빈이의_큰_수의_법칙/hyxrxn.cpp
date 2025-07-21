#include <iostream>
#include <algorithm>
using namespace std;

int arr[1000];

int main() {
    int n, m, k;
    int sum = 0;

    cin >> n >> m >> k;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    sort(arr, arr + n); // 크기순 정렬

    for (int i = 1; i <= m; i++) {
        if (i % (k + 1) == 0) { // k+1의 배수 번째 라면 두 번째로 큰 값 더하기
            sum += arr[n - 2];
        } else { // 아니라면 가장 큰 값 더하기
            sum += arr[n - 1];
        }
    }

    cout << sum;

    return 0;
}