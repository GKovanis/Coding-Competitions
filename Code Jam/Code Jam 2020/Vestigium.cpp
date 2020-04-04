#include <iostream> // includes cin to read from stdin and cout to write to stdout
#include <bits/stdc++.h>
using namespace std; // since cin and cout are both in namespace std, this saves some text

int countFreq(int arr[], int n)
{
    unordered_map<int, int> mp;

    // Traverse through array elements and
    // count frequencies
    for (int i = 0; i < n; i++){
        mp[arr[i]]++;

        // If you get a frequency higher than 2, stop and return 1
        if (mp[arr[i]] > 1) {
            return 1;
        }
    }
    // Else, all frequencies were good so return 0
    return 0;
}


int main() {
  int T, N;
  cin >> T; // read t. cin knows that t is an int, so it reads it as such.

  for (int test = 1; test <= T; ++test)
  {
    cin >> N; // above two lines could be read in one with cin >> t >> n

    int table[N][N]; //array initialization
    int trace,rep_row,rep_col; //initialize output values

    trace = 0;
    // Read matrix
    for (int i = 0; i < N; i++)
        {
        for (int j = 0; j < N; j++)
            {
            cin >> table[i][j];
            // Calculate trace while reading matrix
            if (i==j) {
                trace += table[i][j];
            }

            }
        }

    // Check for each row if we have repeated ones
    rep_row = 0;
    for (int i = 0; i < N; i++)
        rep_row += countFreq(table[i],N);

    // Check the same for each column
    // Cannot directly pass the column, so creating the column manually first
    rep_col = 0;
    for (int j = 0; j < N; j++){
        int column[N];

        for (int i=0; i < N; i++)
            column[i] = table[i][j];

        rep_col += countFreq(column,N);
    }

    // Print result for each case
    cout << "Case #" << test << ": " << trace << " " << rep_row << " " << rep_col << endl;
  }
  return 0;
}
