"""
   Python-121 2023W
   Name: Haani Syed
   Date: 2023-03-30
"""

from Stack_class import Stack

def main():
    """
    -------------------------------------------------------
    Main function that shows the use of the reverse method on the stack object.
    Pushing a list onto the stack and then using reverse method to show how it works.
    Use: Calling the main function demonstrates how reverse method can be used on a stack object.
    -------------------------------------------------------
    Returns:
    None
    -------------------------------------------------------
    """
    stack = Stack() #creates new instane of Stack class and assigned to variable 'stack'
    stack.push(1) #pushes 1 onto stack
    stack.push(2) #pushes 2 onto stack
    stack.push(3) #pushes 3 onto stack
    print('BEFORE reversing it will be:', stack._values) #current values of stack before reversed
    stack.reverse() #stack reverser
    print('AFTER reversing it will be: ', stack._values) #values of stack after reversed


main()
