#include <bits/stdc++.h>
#include <iostream>

using namespace std;

int main() {
  int l, r, circle_d, square_d;

  scanf("%d %d", &l, &r);
  circle_d = r*2;
  square_d = l*sqrt(2);

  string out = square_d >= circle_d ? "nope" : "fits";

  cout << out << endl;
}
