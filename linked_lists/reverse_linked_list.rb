=begin
PROBLEM:
We are given head of a linked list and we want to reverse the linked list.
A linked list is consisted of nodes that are connected to each other. There are doubly linked lists and singly linked lists.
In our problem we are give the head of singly linked list. Which means nodes are linked sort as follows:

1 --> 2 --> 3 --> 4

Each node is linked to the next node. Ruby doesn't have linked lists so we have to implement one.

Once we are given the head, we can iterate over the linked list and on each iteration start reversing the links

AL:

Let's say we are given head (a) of the following linked list

a -- > b --> c --> d

we are going iterate over the linked list and at the end what we want is the following

d --> c --> b --> a

So on first iteration we want a's next node to be nil and previous node to be b

we can start a loop that check while current node is not nil

current = head
prev = nil (head's before is nil)

save the next node so we don't lose touch of the list

so we want a's next node to be nil
current.next = prev
we want current to be previous
prev = current
we want next node to be current
current = next_node 

so after this iteration
a.next nil
current node is b
prev node is a

Att he second iteration

next_node = b.next(c)
b.next = prev(a)
prev = current(b)
current = next_node(c)

Now b's next is a and we have reference to the next node to continue iterating.


=end

class ListNode
  attr_accessor  :val, :next

  def initialize(val, _next = nil)
    @val = val
    @next = _next
  end
end

node_4 = ListNode.new(4)
node_3 = ListNode.new(3, node_4)
node_2 = ListNode.new(2, node_3)
node_1 = ListNode.new(1, node_2)

def reverse_list(head)
  current = head
  prev = nil

  while current
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node
  end

  prev
end