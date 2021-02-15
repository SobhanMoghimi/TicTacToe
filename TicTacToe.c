//The_SnM

#include<stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <stdbool.h>

void instructions(void);
void printbase(void);
int endgame(int a[]);
void printgame(int a[]);
void instruct(char a[],char b[]);



int main ()
{
	char first_name[40],second_name[40],safe_inp[20];
	int myproj=1,mat[9],count,i,live_result,game,block_inp,playerno,k,continue_q;
	printf("Welcome to Tic-Tac-Toe game!\n This game is made for two players.\n");
	printf("First Player's name: ");
	gets(first_name);
	fflush(stdin);
	printf("Second Players name: ");
	gets(second_name);
	fflush(stdin);
	while(1)
	{
		for(i=0;i<9;i++) mat[i]=0;
		game=1;
		count=1;
		while(game)	
		{
			system("cls");
			instruct(first_name,second_name);
			printgame(mat);
			
			//check whether the game is ended or not
			live_result=endgame(mat);
			if(live_result==1) printf("Congrats! %s is the winner!!\n",first_name);
			else if(live_result==2) printf("Congrats! %s is the winner!!\n",second_name);
			if(count==10 && !live_result)	printf("Draw!!\n");
			if(live_result || count==10) break;
			
			
			playerno=!(count%2);
			if(!playerno) printf("%s! Enter the block number: ",first_name);
			else printf("%s! Enter the block number: ",second_name);
			//this while tries to get the valid input
			while(1)
				{
					scanf("%s",safe_inp);
					if(safe_inp[1]!='\0')
						{
							printf("Invalid Input or Block! Try again: ");
							continue;
						}
					block_inp=atoi(safe_inp);
					if(mat[block_inp-1]!=0 || block_inp<1 || block_inp>9)
						{
							printf("Invalid Input or Block! Try again: ");
							continue;
						}
					break;
				}
		
			mat[block_inp-1]=playerno+1;
			count++;
		}
			//check if they want to play again
			printf("%10s","Enter '1' to play again or '0' to exit:  ");
			scanf("%d",&continue_q);
			if(continue_q==1) continue;
			else if(!continue_q) break;
			else printf("You entered wrong number; Exiting automaticlly!");
			break;
		}
		return 0;
}


//***************************Functions!********************************


void printbase(void)
	{
		//just the base as tutorial
		int i,x=-2,y=-1,z=0;
		for(i=0;i<5;i++)
			{
				printf("%100s"," ");
				if(!(i%2))printf("   %d  |  %d  |  %d\n",x+=3,y+=3,z+=3);
				else if(i%2==1 && i!=5) printf("------------------\n");
				else { printf("      |     |   \n");};
			}
	}
	
	
void instruct(char a[],char b[])
{
	//the 3 first lines that appears all the time
	printf("Here is an instruction for the game dear (%s) and (%s).\n",a,b);
			printf("Player:%s Symbol: X\n",a);
			printf("Player:%s Symbol: O\n",b);
				printbase();
			printf("\n\n\n");
}
	
	
int endgame(int a[])
{
	//we check if any player wins now!
	if(a[0]==a[1] && a[1]==a[2] && a[0]!=0) return a[0];
	if(a[3]==a[4] && a[4]==a[5] && a[3]!=0) return a[3];
	if(a[6]==a[7] && a[7]==a[8] && a[6]!=0) return a[6];
	if(a[0]==a[3] && a[3]==a[6] && a[0]!=0) return a[0];
	if(a[1]==a[4] && a[4]==a[7] && a[1]!=0) return a[1];
	if(a[2]==a[5] && a[5]==a[8] && a[2]!=0) return a[2];
	if(a[0]==a[4] && a[4]==a[8] && a[0]!=0) return a[0];
	if(a[2]==a[4] && a[4]==a[6] && a[2]!=0) return a[2];
	return 0;
}

void printgame(int a[])
	{
		//here we print the live board
		int i,j=0;
		char x=' ',y=' ',z=' ';
		for(i=0;i<5;i++)
			{
				printf("%50s"," ");
				if(!(i%2))
					{		
							if(!a[j]) x=' ';else if(a[j]==1) x='X';else x='O';j++;
							if(!a[j]) y=' ';else if(a[j]==1) y='X';else y='O';j++;
							if(!a[j]) z=' ';else if(a[j]==1) z='X';else z='O';j++;
							printf("   %c  |  %c  |  %c\n",x,y,z);
					}
			 else if(i%2==1 && i!=5) printf("------------------\n");
				else { printf("      |     |   \n");};
			}
	}
