//recursion

"use strict";

function printRE(n,i,j)
{
    if(n==1){print("*");return;}
    if(j>n)  return;
  print(" ".repeat((n-j++))+"*".repeat(i));
  printRE(n,2*j-1,j);
}
let n=parseInt(readline());
printRE(n,1,1);

