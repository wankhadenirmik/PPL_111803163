#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<string.h>

int inner(void) {
	return 1;
}


int overflow(void) {
	int arr[2];
	arr[0] = 2;
	arr[1] = 12;
	arr[2] = 1;
	arr[3] = 0x00005555;
	arr[4] = 0x55555125;
	return 1;
}

int main() {
	int i;
	i = 1;
	
	overflow();
	
	return 0; 
}
