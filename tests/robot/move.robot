*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position. Test start of game. Let's play \n\n 
     https://desertsteel.net/cdn/shop/files/saguaro-web-34_c608300e-9aba-4dec-aa4a-f1bf5b321cb7.jpg

Test Template     Move character
Library           MoveLibrary.py 


*** Test Cases ***                  StartingX     StartingY     StartingMoveCount     Direction     EndingX     EndingY     EndingMoveCount
Move in the middle of the board      0             0            1                     NORTH         0           1           2
Move on the edge of the board        0             0            5                     SOUTH         0           0           6
Spec by example1                     0             0            103                   NORTH         0           1           104
Spec by example2                     0             0            32                    SOUTH         0           0           33
Spec by example3                     0             0            1                     EAST          1           0           2
Spec by example4                     0             0            67                    WEST          0           0           68
Spec by example5                     0             9            57                    NORTH         0           9           58
Spec by example6                     0             9            38                    SOUTH         0           8           39
Spec by example7                     0             9            45                    EAST          1           9           46    
Spec by example8                     0             9            25                    WEST          0           9           26                                                      
Spec by example9                     9             9            58                    NORTH         9           9           59
Spec by example10                    9             9            83                    SOUTH         9           8           84
Spec by example11                    9             9            9                     EAST          9           9           10
Spec by example12                    9             9            4                     WEST          8           9           5   
Spec by example13                    9             0            768                   NORTH         9           1           769   
Spec by example14                    9             0            35                    SOUTH         9           0           36   
Spec by example15                    9             0            83                    EAST          9           0           84
Spec by example16                    9             0            36                    WEST          8           0           37   
Spec by example17                    5             5            57                    NORTH         5           6          58 
Spec by example18                    5             5            75                    SOUTH         5           4          76
Spec by example19                    5             5            45                    EAST          6           5          46   
Spec by example20                    5             5            53                    WEST          4           5           54

*** Keywords ***
Move character
    [Arguments]    ${startingX}    ${startingY}    ${startingMoveCount}    ${direction}    ${endingX}    ${endingY}    ${endingMoveCount}
    Initialize character xposition with  ${startingX}
    Initialize character yposition with  ${startingY}
    Initialize character moveCount with  ${startingMoveCount}
    Move in direction                    ${direction}
    Character xposition should be        ${endingX}
    Character yposition should be        ${endingY}
    Character moveCount should be        ${endingMoveCount}