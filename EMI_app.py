st.header('EMI calculator App') 
def emi(p,n,r):
  output=(p*(r/12)*((1+((r/12)/100))**(n*12)))/100*(((1+((r/12)/100))**(n*12))-1)
  return output
tenure=st.slider('Set Tenure of a loan in months: ',1,30) 
principal=st.slider('Set Principal Loan Amount: ',1000,1000000) 
rate=st.slider('Set Rate of interest: ',1,15) 
if st.button('Calculate'): 
  value=emi(principal,tenure,rate) 
  st.write(f'EMI calculated is {value}')
