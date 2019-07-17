# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 21:05:43 2018

@author: YWZQ
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        print(head.val)
        cur=None
        pre=None
        while head:
            cur=head
            head=head.next
            print('cur')
            print(cur.val)
            cur.next=pre
            #head=head.next #注意，这句要放在 cur.next=pre前面，否则第一次时，由于pre是None，而cur指向None,head也会跟着指向None,不符合                              #while条件，结束
            pre=cur
        return cur
if __name__=='__main__':
    a=Solution().reverseList(ListNode([5,6,7])).val
    print(a)
    