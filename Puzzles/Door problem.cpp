#include <iostream>
#include <conio.h>
#define clrscr() system("cls")
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
	
	cout<<"\n1. View open doors\n2. View closed doors\n3. Search for a door\n4. Try with a different number\n5. Exit\n\nSelect your choice: ";
	int choice;
	cin>>choice;
	switch(choice) {
		case 1:
			cout<<"{";
			for(int i = 0; i < totalDoors; i++) {
				if(door[i] == 1)
					cout<<i+1<<", ";
			}
			cout<<"\r\r}\n\nPress any key to continue...";
			getch();
			goto label;
		case 2:
			cout<<"{";
			for(int i = 0; i < totalDoors; i++) {
				if(door[i] == 0)
					cout<<i+1<<", ";
			}
			cout<<"\r\r}\n\nPress any key to continue...";
			getch();
			goto label;
		case 3:
			int search;
			cout<<"Enter the door number: ";
			cin>>search;
			if(door[search-1] == 0)
				cout<<"Door is closed\nPress any key to continue";
			else
				cout<<"Door is open\nPress any key to continue";
				getch();
				goto label; 
		case 4:
			clrscr();
			main();
		case 5:
			exit(0);
		default:
			goto label;
	}

}
