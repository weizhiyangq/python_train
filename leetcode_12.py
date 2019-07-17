'''
#3双指针方法
算法思路：
  这道题应该可以用动态规划做，我用的是double point的方法
  一个指针start指向子串头部，另一个指针end指向子串尾部
  每次递增end，判断end所指字符是否在当前子串中出现过
◦如果出现过，则将start指针向后移动一位
◦否则，将end指针向后移动，并更新最长子串长度                           
  最后返回子串最大长度即可
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str

        :rtype: int

        """
        sLen = len(s)
        if sLen == 0 or sLen == 1:
            return sLen
        letters = list(s)
        hashSet = {}
        hashSet[letters[0]] = 1
        start = 0
        end = 1
        maxLen = 1
        while end != sLen:
            letter = letters[end]
            #if hashSet.has_key(letter) and hashSet[letter] > 0:#这是python2写法
            if letter in hashSet and hashSet[letter] > 0:
                hashSet[letters[start]] -= 1#减一是因为start要+1了，即是向前移动一位，所以原先的start对应的字符不应在已出现字符的字典中存在
                start += 1                 #start会一直+1，直到经过了重复的那个字符（这样就重新变为无重复的了）
                continue
            hashSet[letter] = 1
            end += 1
            if end - start > maxLen:
                maxLen = end - start
        return maxLen
'''




'''
#15  指针法
解题思路：两边夹逼，跳过重复，使用set去重。

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                    while(nums[k] == nums[k + 1] and j < k):   
                        k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j+=1
                    while(nums[j] == nums[j - 1] and j < k):   
                        j += 1
                else:
                    list1 = (nums[i], nums[j], nums[k])
                    ans.append(list1)
                    j += 1
                    k -= 1
                    while(nums[k] == nums[k + 1] and j < k):   
                        k -= 1
                    while(nums[j] == nums[j - 1] and j < k):   
                        j += 1

        return list(set(ans))
'''
'''
#15测试用  报错？？
nums = [-1, 0, 1, 2, -1, -4]
ans = []
nums.sort()

for i in range(len(nums) - 2):
    if nums[i] > 0:
        break
    if i > 0 and nums[i] == nums[i-1]:
        continue
    j = i + 1
    k = len(nums) - 1
    while j < k:
        if nums[i] + nums[j] + nums[k] > 0:
            k -= 1
            while(nums[k] == nums[k + 1] and j < k):   
                k -= 1
        elif nums[i] + nums[j] + nums[k] < 0:
            j+=1
            while(nums[j] == nums[j - 1] and j < k):   
                j += 1
        else:
            list1 = (nums[i], nums[j], nums[k])
            ans.append(list1)
            j += 1
            k -= 1
            while(nums[k] == nums[k + 1] and j < k):   
                k -= 1
            while(nums[j] == nums[j - 1] and j < k):   
                j += 1

print(list(set(ans)))

'''

'''
n
um=37
chu=1000
i=0
roman_list=[0,0,0,0]
chu_list=[1000,100,10,1]
while num>0:
    roman_list[i]=num//chu
    num=num%chu_list[i]
    chu//=10
    i+=1
print(roman_list)
'''
'''
#6

s="PAYPALISHIRING"
numRows=6

#len_s=len(s)
def get_ans(s,numRows):
    l_clean=[]
    l_all=[]
    sum=len(s)
    num=len(s)    #未处理字符个数
    i=0  #列表序号
    while(num>0):
        if (numRows==1)|(sum<numRows):
            return s
        elif i%(numRows-1)==0:
            if num<=numRows:
                l=s+' '*(numRows-num)
                l_all.append(l)
                break
            l=s[:numRows]
            s=s[numRows:]
            num-=numRows
        else:
            l=' '*(numRows-i%(numRows-1)-1)+s[0]+(i%(numRows-1))*' '
            s=s[1:]
            num-=1
        l_all.append(l)
        i+=1
    j=0
    print(l_all)
    while j<numRows:
         l=' '.join([i[j] for i in l_all])
         l_clean.extend(l)
         j+=1
    l_connect=''.join(l_clean)
    l_connect=l_connect.replace(' ','')
    return l_connect

s=get_ans(s,numRows)
print(s)
'''
'''
#8
import re
input="   -42"
num = '^[-+]{0,1}[0-9]{1,}'
print(re.findall(num,input))
'''
'''
x=121

reverse=0
while(x>reverse):
    reverse=reverse*10+x%10
    x//=10
print(x,reverse)
print(reverse/10)
print((x==(reverse/10))|(x==reverse))
'''

'''
#18
nums = [1, 0, -1, 0, -2, 2]
target=0
   
nums.sort()
res=[]
for i in range(0,len(nums)):
    if i>0 and nums[i]==nums[i-1]:
        continue
    for j in range(i+1,len(nums)):
        if j>i+1 and nums[j]==nums[j-1]:
            continue
        start =j+1
        end=len(nums)-1
        while start < end:
            sum = nums[i]+nums[j]+nums[start]+nums[end]
            if sum < target:
                start += 1
            elif sum > target:
                end -= 1
            else:
                res.append((nums[i],nums[j],nums[start],nums[end]))
                start+=1
                end-=1
                while start<end and nums[start]==nums[start-1]:
                    start+=1
                while start<end and nums[end]==nums[end+1]:
                    end-=1
print( res)
'''





'''
#20
s="()[]{}"
char_dict={'(':')',')':'(','[':']',']':'[','{':'}','}':'{'}
if s=='':
    print(True)
len_s=len(s)
i=0
while(True):
    if (i+1)>=len(s):
        break

    if(s[i+1]==char_dict[s[i]]):
        if((i+2)<len(s)):
            s=s[:i]+s[i+2:]
            i-=2
        else:
            s=s[:i]
            i-=2
    i+=1
    if(i<0):
        i=0
    print(i)
    if(i>=(len(s)-1)):
        break
    print(s,i)
print(len(s)==0)
'''
'''
#35
index=0
nums=[1,2,4,6,7]
target=3
len_nums=len(nums)
for i in range(0,len_nums-1):
    if nums[i]==target:
        index=i
        break
    elif (nums[i]<target) & (nums[i+1]>=target):
        index=i+1
        break
    print(i)
print(index)
'''



'''

s="a "
s_list=s.split(' ')
print(s_list)
while s_list[-1]=='':
    s_list.pop()
print(len(s_list[-1]))
'''
'''
x=3
max=x
min=0

while(max>=min):
    med=(max+min)//2
    if med*med>x:
        max=med
    elif med*med<x:
        min=med
    if med*med==x:
        break
    if (max-min==1)& (min*min<x)&(max*max>x):
        med=min
        break
        
  
    
print(int(med))
'''
'''
#88

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6,9,3]       
while((nums1[-1]==0)&(len(nums1)>1)):
    nums1.pop()
nums1.extend(nums2)
nums1=sorted(nums1)
print(nums1)

'''
'''
#119
numRows=5
yang_hui=[[1] * n for n in range(1, numRows + 1)]

print(yang_hui)
i=2
while(i<numRows):
  
    for j in range(1,i):
        yang_hui[i][j]=yang_hui[i-1][j-1]+yang_hui[i-1][j]
    i+=1

print(yang_hui)
'''
'''
prices=[1,2]
prices_sorted=sorted(prices,reverse=True)
print(prices)
print(prices_sorted)
if prices==prices_sorted:
    print(9)
max_get=0
for i in range(0,len(prices)-1):
    for j in range(i+1,len(prices)):
        get=prices[j]-prices[i]
        if get>max_get:
            max_get=get
print(max_get)
    
'''
'''
#168
ans = ""
n=27
while n > 0:
    y = n % 26
    if y == 0:
        char = "Z"
        n -= 26
    else:
        char = chr(ord("A") + y - 1) #ord得到ascii位置
    ans += char
    n = n // 26
print(ans[::-1])
'''
'''
#49
strs=["eat","tea","tan","ate","nat","bat"]
sort_str,sort_str_dict,ret=[],{},[]
strs_list=[list(i) for i in strs]
print(strs_list)

[i.sort() for i in strs_list]
print(strs_list)
sort_str=[''.join(i) for i in strs_list]
print(sort_str)
'''
'''
#48
matrix=[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
'''
'''
#旋转90度
length = len(matrix)
for i in range(length):
        for j in range(i+1,length): #先对角翻转
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
for i in range(len(matrix)):
    matrix[i] = matrix[i][::-1]
print(matrix)
'''
'''
#旋转180度

left=0
right=len(matrix)-1
while right>left:
    temp=matrix[left]
    matrix[left]=matrix[right]
    matrix[right]=temp
    right-=1
    left+=1
for i in range(0,len(matrix)):
    matrix[i]=matrix[i][::-1]
print(matrix)
 
'''
'''
#845
#time limit
A=[2,1,4,7,3,2,5]
length_max=0
len_a=len(A)
for i in range(1,len_a-1):
    flag_left=flag_right=0
    left=right=i
    while left-1>=0:
        if A[left-1]<A[left]:
            left-=1
            flag_left=1
        else:
            break
    while right+1<=len_a-1:
        if A[right]>A[right+1]:
            right+=1
            flag_right=1
        else:
            break
    if (flag_left==1 and flag_right==1):
        length=right-left+1
    else:
        length=0
    length_max=max(length_max,length)
    print('=========')
    print(i)
    print(length)

'''


'''
#50 成功的做法
class Solution:
    def myPow(self, x, n):
        if n == 0: return 1.0
        if n == -1: return 1.0 / x  # 如果是负数，就取倒数。
        return self.myPow(x * x, n // 2) * ([1, x][n % 2])  # 递归求解，,这里([1, x][n % 2])是返回1或者x


if __name__ == '__main__':
    x, n =1.00001, 123456
    print(Solution().myPow(x, n))
'''
'''
# 50 我的做法，本地编译可以，但由于超出递归的深度，所以leetcode没成功

class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        #return x**n 
        
        import sys
 
        sys.setrecursionlimit(1000000) #例如这里设置为一百万
    
    
        if n<0:
            n=-n
            x=1/x
        if n==0:
            return 1
       
        return self.myPow(x,n-1)*x

if __name__ == '__main__':
    x, n =2, 3
    print(Solution().myPow(x, n))


'''
'''
#367

class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<0:
            return False
        if num==0 or num==1:
            return True
        start=1
        end=num//2
        while start<=end:
            mid=(start+end)//2
            if mid*mid==num:
                return True
            if mid*mid<num:
                start=mid+1
            if mid*mid>num:
                end=mid-1
        return False
        

if __name__ == '__main__':
    n =2147483647
    print(Solution().isPerfectSquare( n))
'''
'''
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.rec(res, 0, n, k, [])
        return res
    def rec(self, res, i, n, k, temp) :
        if k == 0 :
            res.append(temp)
            return
        for j in range(i+1, n+1) :
            self.rec(res, j, n, k-1, temp+[j])

if __name__ == '__main__':
    n =5
    k=3
    print(Solution().combine(n,k))

'''
'''
#39
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(candidates,start,target,path,res):
            if target==0:
                return res.append(path+[])
            for i in range(start,len(candidates)):
                if target-candidates[i]>=0:
                    path.append(candidates[i])
                    dfs(candidates,i,target-candidates[i],path,res) #因为可以重复，所以可以从自己开始，否则应该从i+1开始
                    path.pop()
        res=[]
        dfs(candidates,0,target,[],res)
        return res
'''
'''

#78
#本解法采用回溯算法实现，回溯算法的基本形式是“递归+循环”，正因为循环中嵌套着递归，递归中包含循环，这才使得回溯比一般的递归和单纯
#的循环更难理解，其实我们熟悉了它的基本形式，就会觉得这样的算法难度也不是很大。原数组中的每个元素有两种状态：存在和不存在。

#① 外层循环逐一往中间集合 temp 中加入元素 nums[i]，使这个元素处于存在状态

#② 开始递归，递归中携带加入新元素的 temp，并且下一次循环的起始是 i 元素的下一个，因而递归中更新 i 值为 i + 1

#③ 将这个从中间集合 temp 中移除，使该元素处于不存在状态
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums :
            for temp in res[:] :
                x = temp[:]  #注意如果是x=temp,那么，x改变后temp也会跟着改变，但用temp[:]不会有这个问题
                print(x)
                x.append(num)
                res.append(x)
                print(res)
                print('\n')
        return res


if __name__ == '__main__':
    nums=[1,2,3]
   
    Solution().subsets(nums)


'''
'''
class Solution:
    def addBinary(self, a, b):
  
        
        #a=int(a,2)
        #b=int(b,2)
        #c=a+b
        #c_binary=bin(c)
        #c_binary=c_binary[2:] #使用bin后可以将十进制转为二进制的字符串，并且以0x开头
        
       #return c_binary
        
        #更底层的写法
        a=[int(i) for i in a]
        b=[int(i) for i in b]
        lena=len(a)
        lenb=len(b)
        if lena<lenb:
            a,b=b,a
        itera=len(a)-1
        iterb=len(b)-1
        while itera>=0 and iterb>=0:
            a[itera]+=b[iterb]
            itera-=1
            iterb-=1
        for i in reversed(range(len(a))):
            digit=a[i]%2
            carry=a[i]//2
            a[i]=digit
            if i>0:
                a[i-1]+=carry
        if carry==1:
            a.insert(0,1)
        print(a)
        a_str_list=[str(i) for i in a]
        return ''.join(a_str_list)

if __name__ == '__main__':
    a='11'
    b='1'
   
    print(Solution().addBinary(a,b))
'''
'''
#54
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix==[]:
            return []
        def dfs(m,res,num):
            
            if len(res)==num:
                return res
            res.extend(m[0]) #把第一行加进
            print('res')
            print(res)
            
            del(m[0])
            
            if len(res)==num:
                return res
            
            for i in range(len(m)):
                res.append(m[i][-1]) #把每个列表元素的最后一个元素加进
                del(m[i][-1])
            if len(res)==num:
                return res
            
            res.extend(m[-1][-1::-1]) #把最后一行按反序加进去
            del(m[-1])
            if len(res)==num:
                return res
            
            for i in range(len(m)-1,-1,-1):
                res.append(m[i][0])  #把每个列表元素的第一个元素加进去，到此，第一轮结束（外围）
                del(m[i][0])
            if len(res)==num:
                return res
            dfs(m,res,num)
        num=(len(matrix)*len(matrix[0]))
        res=[]
        dfs(matrix,res,num)
        print('answer')
        print(res)
        return res
        
         
if __name__ == '__main__':
    
    matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]

    a=Solution().spiralOrder(matrix)
    print('a')
    print(a)
'''
'''
#55
#思路：记录当前位置能走的最远位置max（maxpos，i+nums[i]）,如果最远位置等于该位置，则返回False，如果一直到结尾则返回Ture，具体代码如下：
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
 #思路：记录当前位置能走的最远位置max（maxpos，i+nums[i]）,如果最远位置等于该位置，则返回False，如果一直到结尾则返回Ture，具体代码如下：
        maxpos=0
        for i in range(len(nums)-1):
            maxpos=max(maxpos,i+nums[i])
            if maxpos==i:
                return False
        return True
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        #注意题目说机器人只能往右或者下走
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        if m<1 or n<1:   #说明为空
            return 0
        if obstacleGrid[m-1][n-1]==1:  #最后一格为1，注定到达不了
            return 0
        #dp=[[0]*n]*m  #不要这样写，因为这样写，dp[1][1]=2后，所有行的[1]位置都变为2
        dp=[[0 for index in range(n)] for index in range(m)]
        for i in range(m): #m为行数，给第一列设置初始值
            if obstacleGrid[i][0]==1:
                dp[i:][0]=0
                break
            dp[i][0]=1
        for j in range(n):  # n为列数，给第一行设置初始值
            if obstacleGrid[0][j]==1:
                dp[0][j:]==0
                break
            dp[0][j]=1
      
        for i in range(1,m):
            for j in range(1,n):
                
                if obstacleGrid[i-1][j]!=1 and obstacleGrid[i][j-1]!=1:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
                    
                elif obstacleGrid[i-1][j]!=1:
                    dp[i][j]=dp[i-1][j]
                elif obstacleGrid[i][j-1]!=1:
                    dp[i][j]=dp[i][j-1]
                #print(dp)     
        
        return dp[m-1][n-1]


if __name__ == '__main__':
    
    #matrix=[[0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0],[1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,1],[0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0],[0,0,0,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0],[1,0,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0],[0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0],[0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0],[0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0],[0,1,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,1],[1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,1,1,0,1,0,0,0,0,1,1],[0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,1],[1,1,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0]]
    matrix=[[0,0,0,1],[1,0,0,1],[1,1,0,0]]
    print(Solution().uniquePathsWithObstacles(matrix))


