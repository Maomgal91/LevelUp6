*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position. Test start of game. Let's play \n\n 
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***                  StartingX     StartingY     StartingMoveCount     Direction     EndingX     EndingY     EndingMoveCount
Move in the middle of the board     0             0             1                     NORTH         0           1           2
Move on the edge of the board       0             0             5                     SOUTH         0           0           6
Spec by exampe1                     0             0             103                   NORTH         0           1           104
Spec by exampe2                     0             0             32                    SOUTH         0           0           33
Spec by exampe3                     0             0             1                     EAST          1           0           2
Spec by exampe4                     0             0             67                    WEST          0           0           68
Spec by exampe5                     0             9             57                    NORTH         0           9           58
Spec by exampe6                     0             9             38                    SOUTH         0           8           39


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