s="""
// I am a single comment and you must remove me :((
/*
I am a block comment and you must remove me
*/

#include<iostream>
using namespace std;

int main() {

int a, b;
cin » a » b; // Reading two variables from user (please remove me!! :( )
cout « a + b « endl;

// End of the program (remove me please :))
return 0;

}

"""
import sys
def cleanCode(s:str):
	startcomLine=s.find("/*")
	endtcomLine=s.find("*/")+2

	s=s[:startcomLine]+ s[endtcomLine:]
	s=s.splitlines()
	for i in range(len(s)):
		if s[i]!="":
			find=s[i].find("//")
			if find==-1:
				print(s[i])
			elif find>0:
				print(s[i][:find])

s=sys.stdin.read()
cleanCode(s)