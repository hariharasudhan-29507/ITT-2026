#author-Hariharasudhan A
from collections import defaultdict
class Solution(object):
    def twoSum(self, nums, target):

        map=defaultdict(int) # initialize the hashmap using placeholders they are integerss

        for i,val in enumerate(nums): # enumerate helps us to traverse through values on array along respective positions
            difference=target - val #hash function h(x)=target - x 
            if difference in map:
                return [map[difference],i] # if it is not unique then the already existing value and the new value are the values that sum up to target 
            else:
                map[val]=i # insert the value in hashmap if it is unique
