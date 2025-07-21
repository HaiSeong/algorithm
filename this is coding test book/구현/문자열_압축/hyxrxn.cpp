#include <string>
#include <iostream>

using namespace std;

int solution(string s) {
    int answer = 10000;

    for (int i = 1; i <= s.length(); i++) {
        string front = ""; // 바로 앞의 문자열
        int length = s.length();
        int num = 1;

        for (int j = 0; j < s.length() / i; j++) {
            string dummy = s.substr(j * i, i);
            if (dummy == front) { // 바로 앞과 같다면 i만큼 길이 줄어듬
                length -= i;
                num++;
                if (num == 2 || num == 10 || num == 100 || num == 1000) { // 특정 개수가 되는 순간 숫자 추가를 위해 길이 늘어남
                    length++;
                }
            } else { // 다르다면 앞 문자열과 개수 갱신
                front = dummy;
                num = 1;
            }
        }
        answer = answer > length ? length : answer;
    }

    return answer;
}