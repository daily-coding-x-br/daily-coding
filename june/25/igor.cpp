// Backtracking, storing a matrix of booleans for cols, rows and boxes 
// which tells which numbers are already in that area.
#include <bits/stdc++.h>
using namespace std;

class Board {
private:
    int b[9][9];
    bool contR[9][10]; // true if row i contains number j
    bool contC[9][10]; // true if column i contains number j
    bool contB[9][10]; // true if box i contains number j

public:
    Board(int **c) {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                b[i][j] = c[i][j];
                contR[i][j] = contC[i][j] = contB[i][j] = false;
            }
            contR[i][9] = contC[i][9] = contB[i][9] = false;
        }
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                contR[i][b[i][j]] = true;
                contC[j][b[i][j]] = true;
                contB[3 * (i / 3) + (j / 3)][b[i][j]] = true;
            }
        }
    }

    bool solveRec(int i, int j) {
        if (i == 9) return true;
        if (b[i][j] != 0) {
            if (j == 8 && solveRec(i+1, 0)) return true; 
            else if (j != 8 && solveRec(i, j+1)) return true;
            else return false;
        } else {
            for (int k = 1; k <= 9; k++) {
                if (contR[i][k]) continue;
                else if (contC[j][k]) continue;
                else if (contB[3 * (i / 3) + (j / 3)][k]) continue;
                
                contR[i][k] = contC[j][k] = contB[3 * (i / 3) + (j / 3)][k] = true;
                b[i][j] = k;
                if (j == 8 && solveRec(i+1, 0)) return true;
                else if (j != 8 && solveRec(i, j+1)) return true;
                b[i][j] = 0;
                contR[i][k] = contC[j][k] = contB[3 * (i / 3) + (j / 3)][k] = false;
            }
            return false;
        }
    }

    void solve() {
        solveRec(0, 0);
    }

    void print() {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++)
                cout << b[i][j] << " ";
            cout << endl;
        }
    }
};

int main() {
    int **m = new int*[9];
    for (int i = 0; i < 9; i++) {
        m[i] = new int[9];
        for (int j = 0; j < 9; j++)
            m[i][j] = 0;
    }
    m[0][0] = 5; m[0][1] = 3; m[0][4] = 7;
    m[1][0] = 6; m[1][3] = 1; m[1][4] = 9; m[1][5] = 5;
    m[2][1] = 9; m[2][2] = 8; m[2][7] = 6;
    m[3][0] = 8; m[3][4] = 6; m[3][8] = 3;
    m[4][0] = 4; m[4][3] = 8; m[4][5] = 3; m[4][8] = 1;
    m[5][0] = 7; m[5][4] = 2; m[5][8] = 6;
    m[6][1] = 6; m[6][6] = 2; m[6][7] = 8;
    m[7][3] = 4; m[7][4] = 1; m[7][5] = 9; m[7][8] = 5;
    m[8][4] = 8; m[8][7] = 7; m[8][8] = 9;
    Board b(m);
    b.print();
    cout << endl;
    b.solve();
    b.print();

    return 0;
}
