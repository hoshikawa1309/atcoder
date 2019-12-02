#include <bits/stdc++.h>
using namespace std;

string S; int N, cnt;

int main() {
	cin >> N >> S;
	for (int i = 0; i < 1000; i++) {
		int c[3] = {i / 100, (i / 10) % 10, i % 10};
		int f = 0;
		for (int j = 0; j < N; j++) {
			if (S[j] == ('0' + c[f])) f++;
			if (f == 3) break;
		}
		if (f == 3) cnt++;
	}
	cout << cnt << endl;
	return 0;
}
