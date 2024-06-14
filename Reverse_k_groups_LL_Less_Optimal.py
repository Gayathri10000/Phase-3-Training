# Less Optimal
class Solution(object):
    def reverseKGroup(self, head, k):
        def findlenght(curr): # O(n)
            length =0:
            while curr:
                curr = curr.next
                length +=1
            return length
            
        def reversell(head): #
            curr = head
            prev = None
            while curr:
                nextnode = curr.next
                curr.next = prev
                prev = curr
                curr = nextnode
            return prev
        
        mainhead,tail = None,None
        curr = head
        while lenght >= k:
            temp = curr
            prev = None
            for i in range(k):
                prev = curr
                curr = curr.next
            prev.next = None
            revll = reversell(temp)
            if mainhead == None:
                minhead = revll
                tail = temp
            else:
                tail.next = reavll
                tail = tamp
            lenght -= k
        tail.next = curr
        return mainhead
      
