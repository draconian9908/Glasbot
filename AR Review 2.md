# Architectural Review Reflection #2

## Feedback and Decisions:
  - Collision Issues
      > We recieved alot of helpful feedback on this issue and have put it to use. We currently have functioning collisions between
        both enemies and items. We had already implemented our own colision system with the coordinates and have decided to contine using this method of collision detection. For removing the items, we took Amon's advice and sent the enemies to a 'time out box' thousands of pixels off screen and halted their movement. 
      > The next problem we are trying to figure out is creating functional player tracking for the enemies to act on. We are 
        currently having an error whenever we call our 'move_enemy' function that says our Player class is undefined. Part of
        how our NPS's movements work (enemies included) is through the use of an anonymous or lambda function, a part of 
        python we are not too familiar with. We think the problem might lie there. 
  - Aesthetics
      > Our main question which was about item bag design came to the close decision of using identifiable bags instead of having 
        'mystery bags'. This decision won with 53% votes so now we will change the images to be identifiable.
      > Other than that most, if not all, of the feedback we recieved on our game's aesthetics was positive.
      
## Review Process Reflection:
  - We felt like we did well during this architectural review. We got useful feedback that we have since applied with sucess. 
  - Unfortunately we had this AR just after cracking how to make the tile placement mechanic work. We were having lots of trouble
    with this and being able to bring it up at the AR probably would have helped. We were at a transition point between two main parts of the game and therefore the questions were a bit more broad than we would have liked.
   
