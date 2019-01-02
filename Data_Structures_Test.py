 k=addTwoNumbers(23,45)
 print(k)

    def addTwoNumbers(self, l1, l2):
        n1 = ''
        n2 = ''
        node = l1
        while node:
            n1 += str(node.val)
            node = node.next
        node = l2
        while node:
            n2 += str(node.val)
            node = node.next

        n1 = int(n1[::-1])
        n2 = int(n2[::-1])

        s = str(n1 + n2)
        s = s[::-1]
        s = [int(i) for i in s]

        s = [ListNode(i) for i in s]
        for i in range(len(s) - 1):
            s[i].next = s[i + 1]

        return s[0]


