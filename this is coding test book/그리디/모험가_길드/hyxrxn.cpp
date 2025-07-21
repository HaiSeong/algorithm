#include <iostream>
using namespace std;

int arr[100000];

int main() {
    int n;
    int num = 0;

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    sort(arr, arr + n); // 공포도 순 정렬

    for (int i = 0; i < n; i++) {
        int max = 0;
        int people = 0;

        // 팀이 구성될 때까지
        while (true) {
            max = max < arr[i] ? arr[i] : max; // 팀원들의 최대 공포도 갱신
            people++; // 팀원 인원수 추가
            if (max == people) { // 최대 공포도와 인원수가 같다면 팀 구성
                num++;
                //cout << "1. i = " << i << ", num = " << num << ", max = " << max << ", people = " << people << endl;
                break;
            }
            // 팀 구성 실패하면 인원 추가를 위해 while문 다시 돌기
            i++;
            if (i >= n) { // n명까지 다 봤는데도 팀 구성 실패하면 끝내기
                //cout << "2. i = " << i << ", num = " << num << ", max = " << max << ", people = " << people << endl;
                break;
            }
            //cout << "3. i = " << i << ", num = " << num << ", max = " << max << ", people = " << people << endl;
        }
    }

    cout << num;

    return 0;
}