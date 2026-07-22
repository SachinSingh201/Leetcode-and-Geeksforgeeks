class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        listA = []
        curr = head
        while curr:
            listA.append([curr,curr.val])
            curr = curr.next
        listA.sort(key= lambda x:x[1] )    

        dummy = ListNode(0)
        dummy.next = None
        tail = dummy 
        for i in range(len(listA)):
            dummy.next = listA[i][0]
            dummy = dummy.next
        dummy.next = None

        return  tail.next