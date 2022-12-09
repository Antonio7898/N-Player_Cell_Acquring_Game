# N-Player_Cell_Acquring_Game

It's game where moto is to acquire maximum no of cells in
a 2D matrix of dimension m .
This game can be played either :
- Multiplayer mode
 -  Vs Bot 
 - Combination of above two (ie some players are humans and some are bots)
 
I have designed this game from scratch using knowledge of search and adversary algorithms in AI

## Rules

- Players choose starting coordinate of matrix such that no two players have choosen coordinates adjacent to each other. 
- Players can acquire cell either horizontally or vertically in the direction of the head.(ie point choosen just before current one)
- The game ends when no player has any cell left to acquire in accordance to rule 1 and 2.
- Player with the maximum acquision wins the game ( thier may be more than 1 winner if maximum acquision is same for some players )


