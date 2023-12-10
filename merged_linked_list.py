class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_sorted_lists(list1, list2):
    dummy = ListNode()
    current = dummy

    while list1 is not None and list2 is not None:
        if list1.value <= list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1 is not None:
        current.next = list1
    elif list2 is not None:
        current.next = list2

    return dummy.next

def print_linked_list(head):
    while head is not None:
        print(head.value, end=" -> ")
        head = head.next
    print()

# Get user input for list1
input_list1 = input("Kindly type in the elements for list1, separated by spaces: ")
elements_list1 = list(map(int, input_list1.split()))
list1 = ListNode(elements_list1[0])
current = list1
for value in elements_list1[1:]:
    current.next = ListNode(value)
    current = current.next

# Get user input for list2
input_list2 = input("Kindly type in the elements for list2, separated by spaces: ")
elements_list2 = list(map(int, input_list2.split()))
list2 = ListNode(elements_list2[0])
current = list2
for value in elements_list2[1:]:
    current.next = ListNode(value)
    current = current.next

# Merge the lists
merged_list = merge_sorted_lists(list1, list2)

# Print the merged list
print("\nMerged List: ", end="")
print_linked_list(merged_list)
