#include <iostream>
using namespace std;

int main() {
	
	int totalDoors;
	
	cout<<"Enter the total number of doors: ";
	cin>>totalDoors;
	
	int door[totalDoors]; //0 means closed, 1 means open
	for(int i = 0; i < totalDoors; i++)
		door[i] = 0;
	
	for(int i = 0; i < totalDoors; i++) {
		for(int j = i; j < totalDoors; j+=(i+1)) {
			if(door[j] == 0)
				door[j]++;
			else
				door[j]--;
		}
	}
	
label:
	
	cout<<"\n1. View all doors\n2. View open doors\n3. View closed doors\n4. Try with a different number\n5. Exit\n\nSelect your choice: ";
	int choice;
	cin>>choice;
	switch(choice) {
		case 1:
			
		case 4:
			clrscr();
			main();
		case 5:
			exit(0);
		default:
			goto label;
	}

}
