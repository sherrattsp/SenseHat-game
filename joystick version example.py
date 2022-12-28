from sense_hat import SenseHat
sense = SenseHat()

# additional code to use if you wanted to make use of the SenseHAT emulator online combined with the joystick/keyboard
# our modified while loop which also incorporates some bonus lives code


while play:  

    sense.show_message("Press Enter to begin", scroll_speed=0.05, text_colour=red, back_colour=e)
    for event in sense.stick.get_events():  # takes the joystick movement and sets it to the user_event variable
        user_event = event.direction


            if user_event == 'up' and position == 0:  # if up is pressed and arrow is up turn arrow green and add 1 to the score
                draw_arrow(green)  # this passes the value of the green variable to the draw_arrow function
                score += 1

            elif user_event == 'down' and position == 180:  # if down is pressed and arrow is down turn arrow
                draw_arrow(green)  # green and add 1 to score
                score += 1

            elif user_event == 'left' and position == 270:  # if left is pressed and arrow is left turn arrow
                draw_arrow(green)  # green and add 1 to score
                score += 1

            elif user_event == 'right' and position == 90:  # if right is pressed and arrow is right turn arrow
                draw_arrow(green)  # green and add 1 to score
                score += 1

            else:
                draw_arrow(red)  # this passes the red variable to the draw_arrow function
                lives -= 1  # take away one life


            if lives == 0:  # if no lives left end game
                play = False
