//#include <string>
//#include <cstring>
//#include <cstdio>
//#include <stdio.h>
#include <bits/stdc++.h>

using namespace std;

inline int comparePairs(pair<int, int> pairA, pair<int, int> pairB) {
  return pairA.second < pairB.second;
}

class UnionFind {
  public:
    int n;
    int* array;

    UnionFind(int n) {
      this->n = n;
      array = new int[n];

      //fill(array, array+n, -1);
      memset(array, -1, n*sizeof(int));
    }

    ~UnionFind() {
      delete[] array;
    }

    int findSet(int a) {
      int root = a;

      while (array[root] >= 0) {
        root = array[root];
      }

      int curr = a;
      int old_parent;

      while (array[curr] >= 0) {
        old_parent = array[curr];
        array[curr] = root;
        curr = old_parent;
      }

      return root;
    }

    void unionSet(int a, int b) {
      int a_parent = findSet(a);
      int b_parent = findSet(b);

      if (a_parent != b_parent) {
        int size_a = -array[a_parent];
        int size_b = -array[b_parent];

        pair<int, int> aPair = make_pair(a_parent, size_a);
        pair<int, int> bPair = make_pair(b_parent, size_b);

        pair<int, int> maxPair = max(aPair, bPair, comparePairs);
        pair<int, int> minPair = min(bPair, aPair, comparePairs);

        array[minPair.first] = maxPair.first;
        array[maxPair.first] = -max(minPair.second+1, maxPair.second);
      }
    }

    string toString() {
      string out = "[ ";
      for (int i = 0; i < n; i++) {
        out += to_string(array[i]) + " ";
      }
      return out + "]";
    }

};


int main() {
  int n,q;
  int ret = scanf("%d %d\n", &n, &q);


  UnionFind uf(n);

  //cout << uf.toString() << endl;

  char type;
  int a, b;

  while (scanf("%c %d %d\n", &type, &a, &b) != EOF) {
    switch (type) {
    case '?': {
      string result = uf.findSet(a) == uf.findSet(b) ? "yes" : "no";
      printf("%s\n", result.c_str());
      break;

    }
    default:
      uf.unionSet(a,b);
    }
  }
};
