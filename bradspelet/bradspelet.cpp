#include <iostream>
#include <bits/stdc++.h>
#include <string>
#include <utility>
#include <vector>

using namespace std;

const bool ANN = true;
const bool BERIT = false;

bool solve(map<pair<pair<int, int>, bool>, bool>* cache, int n, int m, bool turn) {
  /* cout << "solve " << (turn == ANN ? "ANN " : "BERIT ") <<  n << ", " << m << endl; */
  if (n == 1 && m == 1) {
    /* cout << "BASE CASE " << ((!turn == ANN) ? "ANN" : "BERIT") << endl; */
    return !turn;
  }

  if (cache->count({{n, m}, turn})) {
    return (*cache)[{{n,m}, turn}];
  }

  bool winsN = false;
  for (int i = 1; i < n; i++) {
    if ((solve(cache, i, m, !turn) == turn) && (solve(cache, n - i, m, !turn) == turn)) {
      /* cout << (turn == ANN ? "ANN" : "BERIT") << " " << n << ", " << m << " wins by cutting col " << i << endl; */
      winsN = true;
      break;
    }
  }

  bool winsM = false;
  for (int i = 1; i < m; i++) {
    if ((solve(cache, n, i, !turn) == turn) && (solve(cache, n, m - i, !turn) == turn)) {
      /* cout << (turn == ANN ? "ANN " : "BERIT ") << n << ", " << m << " wins by cutting row " << i << endl; */
      winsM = true;
      break;
    }
  }

  bool res = (winsN || winsM) ? turn : !turn;

  (*cache)[{{n,m}, turn}] = res;

  return res;
}


int main() {
  int n, m;
  scanf("%d %d", &n, &m);
  map<pair<pair<int, int>, bool>, bool> cache;

  bool res = solve(&cache, n, m, ANN);

  if (res == ANN) {
    cout << "A" << endl;
  } else {
    cout << "B" << endl;
  }
}


