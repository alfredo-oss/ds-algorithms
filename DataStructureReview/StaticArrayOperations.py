from typing import List

# Initialize an array.
myArray = [1,2,3]

# Access an arbitrary element, where i is the index of the desired value.
i = len(myArray)-1 # Accesing the last element which is always located at the index = (length of the array) - 1
print(f"Single index {myArray[i]}")

#########################################################################
## Traversing through an array (Pointing to the Left side of the array)##
#########################################################################

## for loops:
for i in range(len(myArray)): # When traversing an array with a for loop there is no need to specify the boundaries of the iteration, for loops have that functionality built-in in the class
    print(f"Traversing the array to the LEFT with a for loop, iteration:#{i}: {myArray[i]}")

## While loops:
i = 0 # When traversing an array using while loops you have to initialize the index manually
      # One thing to have in consideration when traversing an array using while loops is that While loops dont have the built-in functionality to set the boundaries of the array.
while i < len(myArray): # So this states that while the condition is met, in this case that i is less than the length of the array, the set of instructions inside the while loop will be evaluated.
    print(f"Traversing the array to the LEFT with a while loop, iteration:#{i}: {myArray[i]}")
    # After you did what you wanted to do you can either subtract or sum positions to the index (as long as you dont go out of boundaries of the array or the condition being evaluated in the while loop)
    i += 1

##############################################################################################
## Traversing through an array (Pointing to the Right side of the array) or "Reverse Order"###
##############################################################################################

## "for" loop:
for i in range(len(myArray)-1, -1, -1):
    print(f"Traversing the array to the RIGHT with a for loop, iteration:#{i}: {myArray[i]}")

## "while" loop:

i = len(myArray)-1

while i >= 0:
    print(f"Traversing the array to the RIGHT with a while loop, iteration:#{i}: {myArray[i]}")
    i-=1

#############################################################################
#####                   Deleting from an array    ###########################
#############################################################################

## "Deleting" at the end of the array: When operating with static arrays, there is no option to deallocate the memory associated with an element in the array so, the only way to "delete" an element is through the operation of replacing the element.

def removeEndElement(array: List[int], length:int) -> List[int]:
    if length > 0:
        array[length - 1] = 0 
    return array

print(f"Remove element from the end of the array: \n Original: {myArray} \n Modified: {removeEndElement(myArray, len(myArray))}")

## "Deleting an element at the #ith index"
## Since elements can't be actually removed from memory, the technique when removing an element from the middle of an array is shift every element that is to the right of that element, to the left of the array, the found element will be replaced by the the contiguous element. Shifting all the elements to the left is neccessary because we cant break the "contiguous values" concept of arrays.

def removeIthElement(array: List[int], index: int, length: int) -> List[int]:
    for i in range(index+1, length): ## There is no "if" to check since the we already know at what index is the element we want to get rid off.
        array[i-1] = array[i]
    return array

print(f"Remove element from an i-th index: \n Original: {myArray} \n Modified: {removeIthElement(myArray, 1, len(myArray))}")


