#function solution takes list as parameter
def solution(lst):
	#string in list is reversed
	rev=lst[::-1]
	print("Reversed list is:\t",rev)
	#reversed string is checked with orginal string in list
	if(rev==lst):print("Thus the list is palindrome!\n");
	else:print("Thus the list is not palindrome!\n");


s=input("Enter the word:\n")
l=[]
for i in range(len(s)):
	l.append((s[i:i+1]))
print("Your initial list is:\t",l)
solution(l)
