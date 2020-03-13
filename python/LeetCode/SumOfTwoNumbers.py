'''Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
#Program 1
####################### Code below #########################
class NumberGame():
    '''def __init__(self,nums,target):
        self.nums = nums
        self.target = target
    '''
    def sumtotarget(self,nums,target):        
        val=''
        index = 0
        secondNoIndex = 0
        SecondNo = 0
        i=0
        for i in range(len(nums)):
            index = i
            #print('i = '+str(i))
            SecondNo = target - nums[index]
            if SecondNo < 0:
                SecondNo = SecondNo * -1
            try:
                if (SecondNo != nums[index]):
                    secondNoIndex = nums.index(SecondNo)
                    val = 'Because nums['+str(index)+'] + nums['+str(secondNoIndex) +'] = '+ str(nums[index])+' + '+str(SecondNo)+' = '+str(target)
                
                    #print(str(SecondNo)+' '+str(secondNoIndex))
                    return val
            except:
                print('Error')

####Execute####
a=[2,7,11,15]
t = 9
ng = NumberGame()
ng.sumtotarget(a,t)
