//Shiming Huang CSCI360 project 1 frequency analysis
#include <iostream>
#include <fstream>
using namespace std;
int main(){
	char letter = 'a';//used for starting letters
	char letterAr[26];//array to hold char 'a' to 'z'
	int amountAr[26];//holds the number each char appears
	char check;//getting char value from file
	int totalLetters;
	
	for(int i=0;i<26;i++){//filling letter array with char from a-z
		letterAr[i]=static_cast<char>(letter+i);
	}
	for(int i=0;i<26;i++){//clear array in case there's random garbage in it
		amountAr[i]=0;
	}

	fstream myfile("toDecrypt.txt",fstream::in);//finding total amount of letters used for finding frequency
	while(myfile>>check)totalLetters++;
	myfile.close();
	
	for (int i=0;i<26; i++){
		fstream myfile("toDecrypt.txt",fstream::in);//open file and close each reiteration to start beginning of file
		while(myfile>>check){
			if(check==letterAr[i]) amountAr[i]++;//check if the char are equal. if it is, increase counter
		}
		myfile.close();
	}
	
	for(int i=0;i<26;i++){//printing all result
		float frequency=(float)amountAr[i]/(float)totalLetters*100;//getting the frequency percantage
		cout<<letterAr[i]<<":"<<amountAr[i]<<" frequency= "<<frequency<<endl;
	}
		
	return 0;
}
