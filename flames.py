import streamlit
streamlit.header("FLAMES GAME")
name1=list(streamlit.text_input("Enter first name:"))
name2=list(streamlit.text_input("Enter second name:"))
for i in name1:
    if i in name2:
        name2.remove(i)
        name1.remove(i)
n=len(name1+name2)
s="FLAMES"
while len(s)!=1:
    i=n%len(s)-1
    if i==-1:
        s=s[:len(s)-1]
    else:
        s=s[i+1:]+s[:i]
if streamlit.button("Get Results"):
    streamlit.success(s)