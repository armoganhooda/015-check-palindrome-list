class cl;
{
public static void main(String ar[]);
{
int i, j, rev=0, k;
i=1234;
for(k=i ; i!=0 ; )
{
j=i%10;
rev = 10*rev+j;
i=i/10;
}
i=k;
if(rev==i)
{
System.out.println("Palindrome");
}
else
{
System.out.println("Not a palindrome");
}
}
}
