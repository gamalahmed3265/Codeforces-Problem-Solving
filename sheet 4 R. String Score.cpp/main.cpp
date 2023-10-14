
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
  int n ;cin>>n;
  string s; cin>>s;
  int score = 0 ;
  for(int i=0 ; i<s.size() ; i++)
  {
      char c = s[i];
      if(c =='V')
      {
          score += 5;
      }
      else if(c == 'W')
      {
        score += 2;  
      }
      else if(c == 'Z')
      {
          if(i != s.size() -1)
          {
              if(s[i+1] == 'W')
              {
                score /= 2;
                s[i+1] = 'a';
              }
              else if(s[i+1] == 'V')
              {
                  score /= 5;
                  s[i+1] = 'a';
              }
          }
      }
      else if(c == 'Y')
      {
          if(i != s.size() -1)
          {
              s.push_back(s[i+1]);
              s[i+1] = 'a';
          }
      }
      else if (c == 'X')
      {
          if(i != s.size() -1)
          {
              s[i+1] = 'a';
          }
      }
  }
  cout<<score;
}



