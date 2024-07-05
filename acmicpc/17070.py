from collections import deque

RIGHT = 0
DOWN = 1
RIGHT_DOWN = 2

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
dp[0][1][RIGHT] = 1

for i in range(n):
    for j in range(n):
        if 0 <= i < n and 0 < j < n:
            if graph[i][j] == 0:
                dp[i][j][RIGHT] += dp[i][j - 1][RIGHT]
                dp[i][j][RIGHT] += dp[i][j - 1][RIGHT_DOWN]

        if 0 < i < n and 0 <= j < n:
            if graph[i][j] == 0:
                dp[i][j][DOWN] += dp[i - 1][j][DOWN]
                dp[i][j][DOWN] += dp[i - 1][j][RIGHT_DOWN]

        if 0 < i < n and 0 < j < n:
            if graph[i][j] == 0 and graph[i - 1][j] == 0 and graph[i][j - 1] == 0:
                dp[i][j][RIGHT_DOWN] += dp[i - 1][j - 1][DOWN]
                dp[i][j][RIGHT_DOWN] += dp[i - 1][j - 1][RIGHT]
                dp[i][j][RIGHT_DOWN] += dp[i - 1][j - 1][RIGHT_DOWN]

print(sum(dp[n-1][n-1]))


'''
# 아루의 재귀
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
constexpr int INF = 0x3f3f3f3f;
constexpr ll LINF = 0x3f3f3f3f3f3f3f3f;

int N, dp[4][20][20], g[20][20], y, x;

// k : 1 (가로), 2(세로), 3(대각) 
int f(int k, int y, int x) {
	if (y == N-1 && x == N-1) return g[y][x] == 0;
	if (g[y][x] == 1) return 0;
	if (y >= N || x >= N) return 0;
	
	int& ret = dp[k][y][x];
	if (ret != -1) return ret;
	
	ret = 0;
	if (k == 1) {
		if (g[y][x+1] == 0) ret += f(k, y, x+1);
		if (g[y][x+1] + g[y+1][x] + g[y+1][x+1] == 0) ret += f(3, y+1, x+1);
	}
	else if (k == 2) {
		if (g[y+1][x] == 0) ret += f(k, y+1, x);
		if (g[y][x+1] + g[y+1][x] + g[y+1][x+1] == 0) ret += f(3, y+1, x+1);
	}
	else {
		if (g[y][x+1] + g[y+1][x] + g[y+1][x+1] == 0) ret += f(k, y+1, x+1);
		if (g[y][x+1] == 0) ret += f(1, y, x+1);
		if (g[y+1][x] == 0) ret += f(2, y+1, x);
	}
	
	return ret;
}

int main(){
	cin.tie(nullptr)->sync_with_stdio(false);
	memset(dp, -1, sizeof dp);
	
	cin >> N;
	for (int i = 0; i < N; i++) 
		for (int j = 0; j < N; j++) cin >> g[i][j];
		
	cout << f(1, 0, 1) << '\n';
	
	return 0;
}
'''