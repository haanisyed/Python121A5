"""
   CISC-121 2023W

   Name: Haani Syed
   Student Number: 20331181
   Email: 21ahs7@queensu.ca
   Date: 2023-03-30

   I confirm that this assignment solution is my own work and conforms to
   Queen's standards of Academic Integrity
"""

class Stack:
    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty stack through creation of empty list storing the elements.
        -------------------------------------------------------
        """
        self._values = [] #initializing array for stack. Initializes an empty stack. Data is stored in a Python list.

    def is_vacant(self):
        """
        -------------------------------------------------------
        Determines whether the stack is empty or not.
        -------------------------------------------------------
        Returns:
        False if stack is not empty, True otherwise.
        -------------------------------------------------------
        """
        return len(self._values) == 0 #boolean expression checking if len of stack empty: True, if not: False


    def push(self, value):
        """
        -------------------------------------------------------
        Will add the given value to the top of the stack.
        -------------------------------------------------------
        Args:
        value: the value that is to be added to the stack.
        -------------------------------------------------------
        """
        self._values.append(value) #adds given value to top of stack by appending to end of underlying list.

    def pop(self):
        """
        -------------------------------------------------------
        Will remove and return top element of the stack.
        Before the condition: Stack is Not Empty
        After the condition: top element removed from stack.
        -------------------------------------------------------
        Return:
        value of top element
        -------------------------------------------------------
        """
        assert len(self._values) > 0 #checks if stack is not empty
        value = self._values[-1] #last element accessed and assigned variable value
        del self._values[-1] #last element of list removed
        return value #value returned (top element of stack popped)

    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the contents of the source stack
        Use: source.reverse()
        -------------------------------------------------------
        Returns:
        None
        -------------------------------------------------------
        """
        self._values.reverse() #reverses order of elements in the stack


