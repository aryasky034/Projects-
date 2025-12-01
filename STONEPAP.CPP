#include<stdio.h>
#include<conio.h>
#include<dos.h>
#include<stdlib.h>
int main()
{
int choice,p1[10],p2[10],result,points1=0,points2=0,i,rounds;
char namep1[15],namep2[15];
clrscr();
printf("\n\t@@@@--(\\^_^/)--WELCOME TO THE GAME--(\\^_^/)--@@@@\n");
printf("\t@#$----@#$\n\t\t ROCK-@@@\n\t\t\t PAPER-###\n\t\t\t\t SCISSOR-$$$\n\t\t\t\t\t@#$----@#$\n ");
printf("\t@#$----RULES TO FOLLOW----@#$\n");
printf("@@@-ROCK--IF A PLAYER CHOSSES ROCK AND THE OTHER PLAYER CHOSSES:-");
printf("\n-->ROCK ITS A TIE\n-->PAPER YOU LOSSE\n-->SCISSORS YOU WIN\n ");
printf("###-PAPER--IF A PLAYER CHOSSES PAPER AND THE OTHER PLAYER CHOSSES:-");
printf("\n-->PAPER ITS A TIE\n-->SCISSORS YOU LOSSE\n-->ROCK YOU WIN\n ");
printf("$$$-SCISSORS--IF A PLAYER CHOSSES SCISSORS AND THE OTHER PLAYER CHOSSES:-");
printf("\n-->ROCK ITS A TIE\n-->PAPER YOU LOSSE\n-->SCISSOR YOU WIN\n ");
printf("press enter to begin (\\^_^/)");
delay(getchar());
clrscr();
printf("\n@#$----SELECT PLAYING MODE----@#$");
printf("\nMODE1= 2 PLAYER\nMODE2= COMPUTER VS PLAYER");
printf("\nENTER YOUR MODE:");
scanf("%d",&choice);
switch(choice){
	case 1:
	printf("\nSELECTED MODE1= 2 PLAYER----(\\^_^/)");
	printf("\nENTER THE FULLNAME OF PLAYER 1ST: ");
	fflush(stdin);
	fgets(namep1,sizeof(namep1),stdin);
	printf("\nENTER THE FULLNAME OF PLAYER 2ND: ");
	fflush(stdin);
	fgets(namep2,sizeof(namep2),stdin);
	fflush(stdin);
	printf("@#$----ENTER NUMBER OF ROUNDS YOU WISH TO PLAY:");
	scanf("%d",&rounds);
	fflush(stdin);
	printf("\n@#$----(\\^_^/)--PLAYERS GET READY--(\\^_^/)----@#$");
	printf("\nPRESS ENTER TO BEGIN----(\\^_^/)");
	delay(getchar());
	clrscr();
	for(i=1;i<=rounds;i++){
	printf("\n\n@#$----ROUND %d BEGINS----@#$",i);
	printf("\nOPTION1:ROCK-@@@\nOPTION2:PAPER-###\nOPTION3:SCISSOR-$$$");
	printf("\n@#$----PLAYER-1 ENTER YOUR OPTION:");
	scanf("%d",&p1[i]);
	printf("\n@#$----PLAYER-2 ENTER YOUR OPTION:");
	scanf("%d",&p2[i]);
	if(p1[i]&&p2[i]!=0&&p1[i]&&p2[i]!=4){
		switch(p1[i]){
		case 1:
		if(p1[i]==1&&p2[i]==1){
		continue;
		}
		if(p1[i]==1&&p2[i]==2){
		points2++;
		}
		if(p1[i]==1&&p2[i]==3){
		points1++;
		}
		break;

		case 2:
		if(p1[i]==2&&p2[i]==1){
		points2++;
		}
		if(p1[i]==2&&p2[i]==2){
		continue;
		}
		if(p1[i]==2&&p2[i]==3){
		points1++;
		}
		break;

		case 3:
		if(p1[i]==3&&p2[i]==1){
		points2++;
		}
		if(p1[i]==3&&p2[i]==2){
		points1++;
		}
		if(p1[i]==3&&p2[i]==3){
		continue;
		}
		break;
			}
		}
	printf("\n@#$----END OF ROUND %d ----@#$\n",i);
	}
	delay(1000);
	clrscr();
	printf("\nRESULTS:\n");
	if(points1>points2){
		for(i=0;i<=15;i++){
		printf("%c",namep1[i]);
		}

		printf("  WINS !!!");
	}
	else if(points1==points2){
	printf("\n\tTHE GAME WAS A TIE ");
	}
	else{
	for(i=0;i<=15;i++){
		printf("%c",namep2[i]);
		}
		printf("  WINS !!!");
	}
	break;

	case 2:
	printf("\nSELECTED MODE2= COMPUTER VS PLAYER----(\\^_^/)");
	printf("\nENTER THE FULLNAME OF PLAYER: ");
	fflush(stdin);
	fgets(namep1,sizeof(namep1),stdin);
	fflush(stdin);
	printf("@#$----ENTER NUMBER OF ROUNDS YOU WISH TO PLAY:");
	scanf("%d",&rounds);
	fflush(stdin);
	printf("\n@#$----(\\^_^/)--PLAYER GET READY--(\\^_^/)----@#$");
	printf("\nPRESS ENTER TO BEGIN----(\\^_^/)");
	delay(getchar());
	clrscr();
	for(i=1;i<=rounds;i++){
	printf("\n@#$----ROUND %d BEGINS----@#$",i);
	printf("\nOPTION1:ROCK-@@@\nOPTION2:PAPER-###\nOPTION3:SCISSOR-$$$");
	printf("\n@#$----PLAYER-1 ENTER YOUR OPTION:");
	scanf("%d",&p1[i]);
	printf("\n@#$----COMPUTER MAKING CHOICE----(\\^_^/)\n");
	p2[i]=(rand()%3)+1;
	delay(1000);
	if(p1[i]&&p2[i]!=0){
		switch(p1[i]){
		case 1:
		if(p1[i]==1&&p2[i]==1){
		continue;
		}
		if(p1[i]==1&&p2[i]==2){
		points2++;
		}
		if(p1[i]==1&&p2[i]==3){
		points1++;
		}
		break;

		case 2:
		if(p1[i]==2&&p2[i]==1){
		points2++;
		}
		if(p1[i]==2&&p2[i]==2){
		continue;
		}
		if(p1[i]==2&&p2[i]==3){
		points1++;
		}
		break;

		case 3:
		if(p1[i]==3&&p2[i]==1){
		points2++;
		}
		if(p1[i]==3&&p2[i]==2){
		points1++;
		}
		if(p1[i]==3&&p2[i]==3){
		continue;
		}
		break;
				}
			}
		printf("\n@#$----END OF ROUND %d ----@#$\n",i);
		}
		delay(1000);
		clrscr();
		printf("\nRESULTS:\n");
		if(points1>points2){
			for(i=0;i<=15;i++){
			printf("%c",namep1[i]);
			}
			printf("  WINS !!!");
		}
		else if(points1==points2){
		printf("\n\tTHE GAME WAS A TIE ");
		}
		else{
		printf("\n\t----COMPUTER WINS !!! ----");
		}
		break;
}
printf("\n\n\t(\\^_^/)@#$----WE HOPE YOU ENOJOYED THE GAME COMEBACK SOON----@#$(\\^_^/)");
/*
for(i=1;i<=rounds;i++){
printf("\n@#$----ROUND %d BEGINS----@#$",i);
printf("\nOPTION1:ROCK-@@@\nOPTION2:PAPER-###\nOPTION3:SCISSOR-$$$");
printf("\n@#$----PLAYER-1 ENTER YOUR OPTION:");
scanf("%d",&p1[i]);
printf("\n@#$----PLAYER-2 ENTER YOUR OPTION:");
scanf("%d",&p2[i]);
	if(p1[i]&&p2[i]!=0){
		switch(p1[i]){
		case 1:
		if(p1[i]==1&&p2[i]==1){
		continue;
		}
		if(p1[i]==1&&p2[i]==2){
		points2++;
		}
		if(p1[i]==1&&p2[i]==3){
		points1++;
		}
		break;

		case 2:
		if(p1[i]==2&&p2[i]==1){
		points2++;
		}
		if(p1[i]==2&&p2[i]==2){
		continue;
		}
		if(p1[i]==2&&p2[i]==3){
		points1++;
		}
		break;

		case 3:
		if(p1[i]==3&&p2[i]==1){
		points2++;
		}
		if(p1[i]==3&&p2[i]==2){
		points1++;
		}
		if(p1[i]==3&&p2[i]==3){
		continue;
		}
		break;
		}
	}
	printf("\n@#$----END OF ROUND %d ----@#$",i);
}
1
if(points1>points2){
	for(i=0;i<=10;i++){
	printf("%c",namep1[i]);
	}
else if(points1==points2){
printf("\n\tTHE GAME WAS A TIE ");
}
else{
for(i=0;i<=10;i++){
	printf("%c",namep2[i]);
	}
}
*/

getch();
return 0;
}