# Fireworks
Very Easy

500pts -> 300pts

21 solves

>Paid Hint: The set seed ensure that you always get the same numbers from randint. just like setting a world seed in Minecraft.

>Paid Hint: We need to undo what they have done to the flag

>Paid Hint: One of the operations they did is reversible

## Challenge Description
Some hacker got into the fireworks system and made it need a password! Lucky for us, they left this here. Maybe this can help us get the password.

Flag is in all uppercase separated by underscores.

## Solve
We are given REVERSE.py for the challenge. 

Reading through the code, it's... I suppose fairly easy to just reverse the whole thing. I swapped the + to a - for the first bit (not the randint one) and walah, FLAG!

The script I used is in ![](./reverseReverse.py)

**NYP{LET_THE_FIREWORKS_BEGIN}**