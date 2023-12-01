class Solution:
    def mergeTwoLists(self, list1, list2):
        # Create a dummy node to start the merged list
        dummy = ListNode(-1)
        current = dummy
        
        # Loop through both lists until one becomes None
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Append the remaining nodes of the non-empty list
        current.next = list1 or list2
        
        return dummy.next
