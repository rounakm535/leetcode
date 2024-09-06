class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a set from the nums array for efficient lookups
        num_set = set(nums)
        
        # Initialize a dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        # Iterate through the linked list
        while current.next:
            # If the next node's value is in the set, remove it
            if current.next.val in num_set:
                current.next = current.next.next
            else:
                current = current.next
        
        return dummy.next