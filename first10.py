from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import getpass
import pyautogui
import pyperclip


dollar = "$" * 99

# User Inputs

print('\n', dollar)


print('')
print('Coding is Just Like Copy And Paste')

print("Please check all the configurations before proceeding !!!")

print('\n')
print("Made For You By Hiten Singla And Sahil Vats")
print("Github Profile ----> https://github.com/Hiten1502")


print('\n', dollar)

username = input('Enter Your Email: ')
password = getpass.getpass(prompt='Enter Your Password:')


# Importing Chrome Driver

driver_path = "./chromedriver.exe"
chrome_options = Options()
driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)


# Where the Magic happens function


time.sleep(2)
driver.get("https://codequotient.com/login")
time.sleep(2)
driver.find_element_by_id("email").send_keys(username)
time.sleep(2)
driver.find_element_by_id("password").send_keys(password)
time.sleep(2)
driver.find_element_by_id("btnSubmit").click()
time.sleep(2)


############################################################


driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5b372a8af8379219939149f9")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);
driver.execute_script("arguments[0].click();",button[1])
time.sleep(2)
driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5b372db4f837921993914a10")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);
driver.execute_script("arguments[0].click();",button[1])
time.sleep(2)

driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5b3cdc4cf837921993916934")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);
driver.execute_script("arguments[0].click();",button[1])
time.sleep(2)
driver.execute_script("arguments[0].click();",button[2])
time.sleep(2)
driver.execute_script("arguments[0].click();",button[3])
time.sleep(2)

driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5b4c9d2d2a3f026b0f4f0e21")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);
driver.execute_script("arguments[0].click();",button[1])
time.sleep(2)
driver.execute_script("arguments[0].click();",button[2])
time.sleep(2)

driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5b3cde35f83792199391693e")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);
driver.execute_script("arguments[0].click();",button[1])
time.sleep(2)

driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5b4747a734eb16221f491227")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);
driver.execute_script("arguments[0].click();",button[1])
time.sleep(2)
driver.execute_script("arguments[0].click();",button[2])
time.sleep(2)
driver.execute_script("arguments[0].click();",button[3])
time.sleep(2)
driver.execute_script("arguments[0].click();",button[4])
time.sleep(2)


# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5aa2a1665ead875d7faa97f7")#link
driver.find_element_by_id("txtOutput0").send_keys("11")
driver.find_element_by_id("txtOutput1").send_keys("6")
driver.find_element_by_id("txtOutput2").send_keys("30")
driver.find_element_by_id("txtOutput3").send_keys("1")
driver.find_element_by_id("txtOutput4").send_keys("7")
driver.find_element_by_id("txtOutput5").send_keys("5")
driver.find_element_by_id("txtOutput6").send_keys("2")
driver.find_element_by_id("txtOutput7").send_keys("18")
driver.find_element_by_id("txtOutput8").send_keys("3")
driver.find_element_by_id("txtOutput9").send_keys("4")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5aa2a2a15ead875d7faa9808")#link
driver.find_element_by_id("txtOutput0").send_keys("9.0")
driver.find_element_by_id("txtOutput1").send_keys("9.6")
driver.find_element_by_id("txtOutput2").send_keys("2.2")
driver.find_element_by_id("txtOutput3").send_keys("6.0")
driver.find_element_by_id("txtOutput4").send_keys("6.0")
driver.find_element_by_id("txtOutput5").send_keys("8.0")
driver.find_element_by_id("txtOutput6").send_keys("1.25")
driver.find_element_by_id("txtOutput7").send_keys("3.0")
driver.find_element_by_id("txtOutput8").send_keys("4.0")
driver.find_element_by_id("txtOutput9").send_keys("6.4")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5aa2a3645ead875d7faa9814")#link
driver.find_element_by_id("txtOutput0").send_keys("val1%10;")
driver.find_element_by_id("txtOutput1").send_keys("val1/10%10;")
driver.find_element_by_id("txtOutput2").send_keys("val1/100%10;")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5aa2a4275ead875d7faa9857")#link
driver.find_element_by_id("txtOutput0").send_keys("(15*count-11)")
driver.find_element_by_id("txtOutput1").send_keys("(-10*count+40)")
driver.find_element_by_id("txtOutput2").send_keys("(4*count-11)")
driver.find_element_by_id("txtOutput3").send_keys("(-3*count+100)")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5aa557b75ead875d7faab603")#link
driver.find_element_by_id("txtOutput0").send_keys("true")
driver.find_element_by_id("txtOutput1").send_keys("false")
driver.find_element_by_id("txtOutput2").send_keys("false")
driver.find_element_by_id("txtOutput3").send_keys("true")
driver.find_element_by_id("txtOutput4").send_keys("true")
driver.find_element_by_id("txtOutput5").send_keys("false")
driver.find_element_by_id("txtOutput6").send_keys("true")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)
# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b41bb0af83792199391808e")#link
driver.find_element_by_id("txtOutput0").send_keys("7")
driver.find_element_by_id("txtOutput1").send_keys("8")
driver.find_element_by_id("txtOutput2").send_keys("7")

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)




# c1

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a2e09056dc3de029e4889e6")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

# include<bits/stdc++.h>
using namespace std;
int main(){
    int n;cin>>n;
    if(n%2 == 0){
        cout<<"Even"<<endl;
    }
    else{
        cout<<"Odd"<<endl;
    }
    return 0;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)



# c1

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a2e123c6dc3de029e488a24")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

# include<bits/stdc++.h>
using namespace std;
int main(){
    int arr[3];
    for (int i = 0; i < 3; i++)
    {
        cin>>arr[i];
    }
    cout<<(*max_element(arr,arr+3))<<endl;
    return 0;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)



# c1

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a2e0c006dc3de029e4889fb")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

# include<bits/stdc++.h>
using namespace std;
int main()
{
  	int n;
    cin>>n;
    if(n%4==0){
        if(n%100==0 && n%400!=0){
            cout<<"Not a Leap Year";
        }
        else{
            cout<<"Leap Year";
        }
    }
    else{
        cout<<"Not a Leap Year";
    }
    return 0;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)



# c1

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5d46dfdf695fda3b2cd0ac34")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

# include<bits/stdc++.h>
using namespace std;
int main(){
    int arr[] = {2000, 500, 100, 50, 20, 10, 5, 2, 1};
    int n;cin>>n;
    int x  = sizeof(arr)/sizeof(arr[0]);
    for (int i = 0; i < x; i++)
    {
        int z = n/arr[i];
        n  = n - z*arr[i];
        arr[i] = z;
    }
    for (int i = 0; i < x; i++)
    {
        cout<<arr[i]<<" ";
    }
    return 0;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)



# c1

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a2e1fd86dc3de029e488a94")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

#include<iostream>
//#include<cstdio>
//#include<cmath>
using namespace std;
int main()
{
  int n;
  cin>>n;
  int sum=0;
  for(int i=1;i<=n;i++){
    sum=sum+i; 
  }
  cout<<sum;
   return 0;
}

   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)



# c1

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a2e30b56dc3de029e488ad4")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

#include <iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    for (int i = 1; i <= n; i++){
        for(int j=i;j>=1;j--){
            cout<<j;
        }
        for(int j=2;j<=i;j++){
            cout<<j;
        }
        cout<<endl;
    }
    return 0;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)



# c1

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a2e33116dc3de029e488ad7")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

# include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    int p =1;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            cout<<p;
            if(j != i){
                cout<<" ";
            }
            p++;
        }
        cout<<endl;
    }
    return 0;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)



# c1

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a2e35746dc3de029e488ade")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

# include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
     for (int i = 0; i < 1; i++)
    {
        for (int j = 1; j < n-i+1; j++)
        {
            cout<<j;
        }
        int p = n-i-1;
        for (int j = 1; j < n; j++)
        {
            cout<<p;
            p--;
        }
        cout<<endl;
    }
    for (int i = 0; i < n-1; i++)
    {
        for (int j = 0; j < n-i-1; j++)
        {
            cout<<j+1;
        }
        for (int j = 0; j < 2*i+1; j++)
        {
            cout<<"*";
        }
        int p = n - i-1;
        for (int j = 0; j < (n-i-1); j++)
        {
            cout<<p;
            p--;
        }
        cout<<endl;
    }
    return 0;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)



# c1

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a2e20796dc3de029e488a9b")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

# include<bits/stdc++.h>
using namespace std;
int main(){
    int n,m;
    cin>>n>>m;
    for (int i = 1; i <= m; i++)
    {
        cout<<(n*i)<<endl;
    }
    return 0;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)


##########################################################3


#############################################33


driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5b419ab5f837921993917f93")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);
driver.execute_script("arguments[0].click();",button[1])
time.sleep(2)
driver.execute_script("arguments[0].click();",button[2])
time.sleep(2);
driver.execute_script("arguments[0].click();",button[3])
time.sleep(2)
driver.execute_script("arguments[0].click();",button[4])
time.sleep(2);
driver.execute_script("arguments[0].click();",button[5])
time.sleep(2)

driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5b38c52fc6a1d0259e728e74")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);


driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5b4a01613714c2304e8557ea")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);
driver.execute_script("arguments[0].click();",button[1])
time.sleep(2)

# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b41b68df83792199391806c")#link
driver.find_element_by_id("txtOutput0").send_keys("-2 + 4 = 7")
driver.find_element_by_id("txtOutput1").send_keys("4 + -2 = 3")
driver.find_element_by_id("txtOutput2").send_keys("2 + 11 = 5")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)
# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b41b6e7f837921993918071")#link
driver.find_element_by_id("txtOutput0").send_keys("12")
driver.find_element_by_id("txtOutput1").send_keys("2")
driver.find_element_by_id("txtOutput2").send_keys("16")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)
# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b41b7f9f837921993918077")#link
driver.find_element_by_id("txtOutput0").send_keys("1342213422")
driver.find_element_by_id("txtOutput1").send_keys("""quotient and coding like code
code and quotient like coding
""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)
# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b41b8c5f83792199391807e")#link
driver.find_element_by_id("txtOutput0").send_keys("""
cq3: x = 23, y = 7
cq2: x = 12, y = 1, z = 7
cq1: x = 7, y = 11, z = 12
""")
driver.find_element_by_id("txtOutput1").send_keys("""
cq3: x = 44, y = 11
cq2: x = 23, y = 1, z = 11
cq1: x = 11, y = 21, z = 23
""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

# c1

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a4e652dd2b99733e5c16900")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

int sumOfRange(int min, int max){
  int sum(0);
  for (int i = min; i <= max; i++)
  {
    sum += i;
  }
  return sum;
}

   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# c1

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a093c7917bcb854c302bd23")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/*
 * Complete the function 'verifyPrime'
 * @params
 *  n ->number which is to be checked from primality test
 *
 * @return
 *   true if the number is a prime number else false
 */
bool verifyPrime(int n){
  // Write your code her
  if(n == 0 || n == 1){
      return false;
  }
  for (int i = 2; i < n; i++)
  {
      if(n%i == 0){
          return false;
      }
  }
  return true;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# c1

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a11753954305147defdced0")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/*
 * Complete the function 'primeFactors'
 * Print all the prime factors of the number
 * @params
 *   n -> numbers whose prime factors are to be found
 */
void primeFactors(int n){
  // Write your code here
  while (n%2 == 0) 
    { 
        printf("%d", 2);
        cout<<endl; 
        n = n/2; 
    } 
    for (int i = 3; i <= sqrt(n); i = i+2) 
    { 
        while (n%i == 0) 
        { 
            printf("%d", i); 
            cout<<endl;
            n = n/i; 
        } 
    } 
    if (n > 2) 
        printf ("%d", n); 
        cout<<endl;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# c1

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a1056fb54305147defdcec2")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/*
 * Complete the function 'gcd'
 * @params
 *   i -> first integer
 *   j -> second integer
 *
 *  @returns
 *  an integer, denoting the gcd of i and j
 */
int gcd(int i, int j){
  if(j == 0){
    return i;
  }
  return gcd(j,i%j);
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# c1

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a4e7676d2b99733e5c16921")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

int binaryToDecimal(string binary){
  string num=binary;
  int sum=0;
  int base=1;
  for (int i=num.length()-1;i>=0;i--){
    if (num[i]=='1'){
      sum+=base;
    }
    base=base*2;
  }
  return sum;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b41bb0af83792199391808e")#link
driver.find_element_by_id("txtOutput0").send_keys("7")
driver.find_element_by_id("txtOutput1").send_keys("8")
driver.find_element_by_id("txtOutput2").send_keys("7")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)
# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b41ba29f837921993918087")#link
driver.find_element_by_id("txtOutput0").send_keys("m1-ii")
driver.find_element_by_id("txtOutput1").send_keys("Error")
driver.find_element_by_id("txtOutput2").send_keys("m1-if")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

# c1

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b4a03903714c2304e8557f4")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

// write the overloaded sum() functions for 2, 3 and 4 arguments
int sum(int a,int b){
  return a+b;
}
int sum(int a,int b,int c){
  return a+b+c;
}
int sum(int a,int b,int c,int d){
  return a+b+c+d;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)
# c1

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b4a06483714c2304e8557fc")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

// Write overloaded display(string a) and display(string a, string b) functions
void display(string a){
  cout<<a;
}
void display(string a,string b){
  cout<<a<<"-";
  cout<<b;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)



#######################################################33333333333

driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a006a24e63d6b7fd5dec29b")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);
driver.execute_script("arguments[0].click();",button[1])
time.sleep(2)
driver.execute_script("arguments[0].click();",button[2])
time.sleep(2)

driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a006b92e63d6b7fd5dec2bb")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);

driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a006a7de63d6b7fd5dec2a6")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);
driver.execute_script("arguments[0].click();",button[1])
time.sleep(2)

driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a006ac5e63d6b7fd5dec2ae")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);
driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5b419e91f837921993917fb1")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);
driver.execute_script("arguments[0].click();",button[1])
time.sleep(2);
driver.execute_script("arguments[0].click();",button[2])
time.sleep(2);
driver.execute_script("arguments[0].click();",button[3])
time.sleep(2);
driver.execute_script("arguments[0].click();",button[4])
time.sleep(2);
driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5b3908e9c6a1d0259e728f8f")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);
driver.execute_script("arguments[0].click();",button[1])
time.sleep(2);

# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a411e7f1fa97021c32ce070")#link
driver.find_element_by_id("txtOutput0").send_keys("70 25")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

#MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a411ec71fa97021c32ce073")#link
driver.find_element_by_id("chkOpt4").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a411f161fa97021c32ce074")#link
driver.find_element_by_id("txtOutput0").send_keys("31")
driver.find_element_by_id("txtOutput1").send_keys("1004")
driver.find_element_by_id("txtOutput2").send_keys("1004")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)
#MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a411f731fa97021c32ce079")#link
driver.find_element_by_id("chkOpt1").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)


#MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a2bcdae6dc3de029e4887c8")#link
driver.find_element_by_id("chkOpt4").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b4ad952f5c97d305544b0d7")#link
driver.find_element_by_id("txtOutput0").send_keys("68")
driver.find_element_by_id("txtOutput1").send_keys("88")
driver.find_element_by_id("txtOutput2").send_keys("76")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b44c4dce25fb6141524a0ef")#link
driver.find_element_by_id("txtOutput1").send_keys("True")
driver.find_element_by_id("txtOutput0").send_keys("True")
driver.find_element_by_id("txtOutput2").send_keys("True")
driver.find_element_by_id("txtOutput3").send_keys("False")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b44c555e25fb6141524a0f5")#link
driver.find_element_by_id("txtOutput0").send_keys("No")
driver.find_element_by_id("txtOutput1").send_keys("Yes")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b44c69de25fb6141524a0f9")#link
driver.find_element_by_id("txtOutput0").send_keys("True")
driver.find_element_by_id("txtOutput1").send_keys("True")
driver.find_element_by_id("txtOutput2").send_keys("False")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

#MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b4ada9ef5c97d305544b0dc")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b4adc14f5c97d305544b0dd")#link
driver.find_element_by_id("txtOutput0").send_keys("0")
driver.find_element_by_id("txtOutput1").send_keys("2")
driver.find_element_by_id("txtOutput2").send_keys("2")
driver.find_element_by_id("txtOutput3").send_keys("1")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

#MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b4adcddf5c97d305544b0e3")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# c1

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5ca2e6c893d7f626b4060811")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

vector<int> cutSticks(vector<int> lengths) {
  sort(lengths.begin() , lengths.end());
  int shortest = INT_MIN;
  vector<int> ans;
  for(int i=0;i<lengths.size();i++){
    if(lengths[i] > shortest){
    	ans.push_back(lengths.size() -i);
    	shortest = lengths[i];  
    }
    
  }
  return ans;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)



#########################################################3

driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5b38c12dc6a1d0259e728e56")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);
driver.execute_script("arguments[0].click();",button[1])
time.sleep(2)

driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5b38c21fc6a1d0259e728e63")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);
driver.execute_script("arguments[0].click();",button[1])
time.sleep(2)
driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5b38c902c6a1d0259e728e9b")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);
driver.execute_script("arguments[0].click();",button[1])
time.sleep(2)
driver.execute_script("arguments[0].click();",button[2])
time.sleep(2)
driver.execute_script("arguments[0].click();",button[3])
time.sleep(2)
driver.execute_script("arguments[0].click();",button[4])
time.sleep(2)

driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5b38c9aac6a1d0259e728ea9")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);

#MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b18b68d7becc0459de9bf72")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)
#MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b41e78a378b141faaf16c23")#link
driver.find_element_by_id("chkOpt4").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)


# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b41e856378b141faaf16c5c")#link
driver.find_element_by_id("txtOutput0").send_keys("No")
driver.find_element_by_id("txtOutput1").send_keys("No")
driver.find_element_by_id("txtOutput2").send_keys("Yes")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)
# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b41e8fa378b141faaf16c6c")#link
driver.find_element_by_id("txtOutput0").send_keys("No")
driver.find_element_by_id("txtOutput1").send_keys("Yes")
driver.find_element_by_id("txtOutput2").send_keys("No")
driver.find_element_by_id("txtOutput3").send_keys("No")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)
# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b41ea32378b141faaf16c7b")#link
driver.find_element_by_id("txtOutput0").send_keys("No")
driver.find_element_by_id("txtOutput1").send_keys("No")
driver.find_element_by_id("txtOutput2").send_keys("Yes")
driver.find_element_by_id("txtOutput3").send_keys("No")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)
# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b41ea7f378b141faaf16c81")#link
driver.find_element_by_id("txtOutput0").send_keys("No")
driver.find_element_by_id("txtOutput1").send_keys("No")
driver.find_element_by_id("txtOutput2").send_keys("Yes")
driver.find_element_by_id("txtOutput3").send_keys("No")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)
# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b4ae0d2f5c97d305544b0ec")#link
driver.find_element_by_id("txtOutput0").send_keys("Modular")
driver.find_element_by_id("txtOutput1").send_keys("Monolithic")
driver.find_element_by_id("txtOutput2").send_keys("Object-Oriented")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)



# c1

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5aba57adecf32f0f52165aa5")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""
class TimeSpan
{
  private: int hours;
  private: int minutes;
  public: TimeSpan(int initialHours, int initialMin){
    hours = 0;
    minutes = 0;
add(initialHours, initialMin);
  }
  public: int getHours(){
    return hours;
  }
  public: int getMinutes(){
    return minutes;
  }
  public: void add(int initialHours, int initialMin){
    hours += initialHours;
    minutes += initialMin;
	if(minutes >= 60){
      minutes -= 60;
      hours++;
    }
  }
  public: void add(TimeSpan tp){
	add(tp.hours, tp.minutes);
  }
  public: double getTotalHours(){
    return hours + minutes / 60.0;
  }
  public: std::string toString(){
std::string str{std::to_string(hours)+" Hours, "+std::to_string(minutes)+" Minutes"};
    return str;
  }
};
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)


# c1

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5aba5b3becf32f0f52165adb")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

class Date
{
  // Write your code here
  private:
  int month,day;
  public:
  Date(int m,int d){
    month=m;
    day=d;
  }
  int daysInMonth(){
    if(month==4|| month==6 || month==9 || month==11){
      return 30;
    }else if(month==2){
      return 28;
    }
    else{
      return 31;
    }
  }
  int getDay(){
    return day;
  }
  int getMonth(){
    return month;
  }
  void nextDay(){
    day++;
    if(day>=daysInMonth()){
      month++;
      day=1;
      if(month>12){
        month=1;
      }
    }
  }
  string toString(){
    string result="";
    result+=to_string(month);
    result+="/";
    result+=to_string(day);
    return result;
  }
  int absoluteDay(){
    int days;
    days=day;
    switch(getMonth()){
      case 2:
        days+=31;
        break;
      case 3:
        days+=31+28;
        break;
      case 4:
        days+=31+28+31;
        break;
      case 5:
        days+=31+28+31+30;
        break;
      case 6:
        days+=31+28+31+30+31;
        break;
      case 7:
        days+=31+28+31+30+31+30;
        break;
      case 8:
        days+=31+28+31+30+31+30+31;
        break;
      case 9:
        days+=31+28+31+30+31+30+31+31;
        break;
      case 10:
        days+=31+28+31+30+31+30+31+31+30;
        break;
      case 11:
        days+=31+28+31+30+31+30+31+31+31;
        break;
      case 12:
        days+=31+28+31+30+31+30+31+31+31+30+30;
        break;
    }
    return days;
  }
};
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)


# c1

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b4cad9d2a3f026b0f4f0fc9")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

int cnt=0;	// manipluate this variable in your code
class Counter
{ 
  public: 
	Counter(){
            cnt++;
            //cout<<"c1 id "<<cnt<<endl;
        }
        ~Counter(){
            cnt--;
            //cout<<"c2 id "<<cnt<<endl;
        }
};
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)




#######################################333

driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/60db0fb0a85d46f848f4c912");
time.sleep(2)

driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/60db1774a85d46f848f4c915");
time.sleep(2)

driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a4a420eb1afa55f38fed780");
time.sleep(2)
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);
driver.execute_script("arguments[0].click();",button[1])
time.sleep(2)
driver.execute_script("arguments[0].click();",button[2])
time.sleep(2)

###########################Array Module####################33

driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/59fde2a0e63d6b7fd5dec004")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);
driver.execute_script("arguments[0].click();",button[1])
time.sleep(2)

driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/59fde6f5e63d6b7fd5dec01e")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);

# driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a12edf146765b2b63e3476b")
# button = driver.find_elements_by_xpath("//a[text()='run']")
# driver.execute_script("arguments[0].click();",button[0])
# time.sleep(2);
# driver.execute_script("arguments[0].click();",button[1])
# time.sleep(2);

# MCQ1
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a42313b1fa97021c32ce0a3")#link
time.sleep(2)
driver.find_element_by_id("txtOutput0").send_keys("1 2 3 4 5")
driver.find_element_by_id("txtOutput1").send_keys("5 4 3 2 1")
driver.find_element_by_id("txtOutput2").send_keys("5 -15 -58 -35 25")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

# MCQ2
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a42313b1fa97021c32ce0a3")#link
driver.find_element_by_id("txtOutput0").send_keys("1 2 3 4 5")
driver.find_element_by_id("txtOutput1").send_keys("5 4 3 2 1")
driver.find_element_by_id("txtOutput2").send_keys("5 -15 -58 -35 25")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)


# MCQ2
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a4231711fa97021c32ce0a8")#link
driver.find_element_by_id("txtOutput0").send_keys("1 -1 -4 -8 -13")
driver.find_element_by_id("txtOutput1").send_keys("5 1 -2 -4 -5")
driver.find_element_by_id("txtOutput2").send_keys("5 -60 -105 -107 -132")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a4231aa1fa97021c32ce0ad")#link
driver.find_element_by_id("txtOutput0").send_keys("2 1 4 3 6")
driver.find_element_by_id("txtOutput1").send_keys("6 3 4 1 2")
driver.find_element_by_id("txtOutput2").send_keys("6 64 46 1 26 ")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a4231ef1fa97021c32ce0b2")#link
driver.find_element_by_id("txtOutput0").send_keys("1 2 3 4 5")
driver.find_element_by_id("txtOutput1").send_keys("5 4 3 2 1")
driver.find_element_by_id("txtOutput2").send_keys("5 25 27 2 25")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

#MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a42359e1fa97021c32ce0c2")#link
driver.find_element_by_id("chkOpt3").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

#MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a487f12b1afa55f38fed739")#link
driver.find_element_by_id("chkOpt1").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

#MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a487f45b1afa55f38fed73a")#link
driver.find_element_by_id("chkOpt1").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

#MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a487fabb1afa55f38fed73b")#link
driver.find_element_by_id("chkOpt1").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)



# c1

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/59ff2beae63d6b7fd5dec1af")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

#include<iostream>
#include<cstdio>
#include<cmath>
# include<bits/stdc++.h>
// Include headers as needed
using namespace std;
int main()
{
  int n = 5;
  int arr [n];
  for(int i=0;i<n;i++){
    cin>>arr[i];
  }
  int max1 = INT_MIN , max2 = INT_MIN;
  for(int i=0;i<n;i++){
    if(arr[i]>max1){
      max1 = arr[i];
    }
  }
  for(int j=0;j<n;j++){
    if(arr[j]>max2 && arr[j]<max1){
      max2 = max(max2 , arr[j]);
    }
  }
  if(max2 == INT_MIN){
    cout<<0<<endl;
  }
  else{
  	cout<<max2;  
  }
    return 0;
}

   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)


# c2

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a4fb5ee7a3c1824dba91428")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
int main()
{
   int T;
   cin>>T;
   for (int i = 0; i < T; i++)
   {
       int mf = 0;
       int max_count = 0;
       int n;
       cin>>n;
       int a[n];
       for (int i = 0; i < n; i++)
       {
           cin>>a[i];
       }
       for (int i = 0; i < n; i++)
       {
             	int count = 0;
           for (int j = i+1; j < n; j++)
           {
               if(a[i] == a[j]){
                   count++;
               }
               if(count >= max_count){
                   max_count = count;
                   mf = a[i];
               }
           }
       }
       cout<<mf<<endl;
   }
   return 0;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)


# c3

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a2e543e6dc3de029e488b37")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

# include<bits/stdc++.h>
using namespace std;
int main(){
    int arr[10];
    for (int i = 0; i < 10; i++)
    {
        cin>>arr[i];
    }
    int neg(0),pos(0),even(0),odd(0);
    for (int i = 0; i < 10; i++)
    {
        if(arr[i]>=0){
            pos++;
        }
        if(arr[i]<0){
            neg++;
        }
        if(arr[i]%2 == 0){
            even++;
        }
        else{
            odd++;
        }
    }
    cout<<pos<<endl;
    cout<<neg<<endl;
    cout<<even<<endl;
    cout<<odd<<endl;
    return 0;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)


# c4

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5d9f41ae5f73f530a20bd5d6")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

   int arraysEqualorNot(vector<int> A, vector<int> B) {
  sort(A.begin(),A.end());
  sort(B.begin(),B.end());
  for (int i = 0; i < A.size(); i++)
   {
       if(A[i] != B[i]){
           return 0;
       }
   }
   return 1;
}

 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)


# c5

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a4fafbb7a3c1824dba9141c")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""
void moveElements(int arr[], int n){
   int key,j;
   for (int i = 0; i < n; i++)
   {
       key = arr[i];
       j = i-1;
       while (j>=0 && arr[j]<0 && key>=0)
       {
           arr[j+1] = arr[j];
           j--;
       }
       arr[j+1] = key;
   }
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)


###########################3333

#############################7th mod#########################

driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a12ef3746765b2b63e3477e")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);
driver.execute_script("arguments[0].click();",button[1])
time.sleep(2)

#MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a487fdfb1afa55f38fed73c")#link
driver.find_element_by_id("chkOpt1").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)
#MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a48801bb1afa55f38fed73d")#link
driver.find_element_by_id("txtOutput0").send_keys("9")
driver.find_element_by_id("txtOutput1").send_keys("29")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)
#MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a488049b1afa55f38fed741")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)
#MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a488065b1afa55f38fed742")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)


# c1

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a4fc0117a3c1824dba91440")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

int getPairsCount(int arr[], int n, int sum){
  // Write your code here
  int s=0;
  int l=n-1;
  int count=0;
  while(s<l){
    if(arr[s]+arr[l]<sum) s++;
    else if(arr[s]+arr[l]==sum){
      int p=l;
      while(arr[l]==arr[p] && p>s){
        count++;
        p=p-1;
      }
      s++;
    }
    else{
    l--;
    }
  }
  return count;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)
# c2

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a50df747a3c1824dba915dc")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

# include<bits/stdc++.h>
using namespace std;
int find(int arr[],int n,int k){
    for (int i = 0; i < n; i++)
    {
         if(arr[i] == k){
            return i;
            break;
        }
    }
    return -1;
}
int main(){
    int t;cin>>t;
    while (t--)
    {
        int n,k;
        cin>>n>>k;
        int arr[n];
        for (int i = 0; i < n; i++)
        {
            cin>>arr[i];
        }
        cout<<find(arr,n,k)<<endl;
    }
    return 0;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)
# c3

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5d81f1f6e9156a66a25b7709")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

int rotationCount(int a[], int size){
   int mn = *min_element(a,a+size);
    for (int i = 0; i < size; i++)
    {
        if(a[i] == mn){
            return i;
        }
    }
    return 0;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)
# c4

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a539b04f239e2076be893e8")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

void sort(int arr[],int n){
   for (int i = 0; i < n; ++i)
    {
        for (int j = i + 1; j < n; ++j)
        {
            if (arr[i] > arr[j])
            {
                int temp =  arr[i];
                arr[i] = arr[j];        
                arr[j] = temp;
            }
        }
    }
}
int getMissingElement(int* a,int a_size,int* b ,int b_size){
  	sort(a,a_size);
    sort(b,b_size);
    for (int i = 0; i < b_size; i++)
    {
        if(a[i] != b[i]){
            return a[i];
        }
    }
    return a[a_size-1];
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)


#########################33


###############################################333333

driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a59dbc1a4af025f554a0bb2")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);
driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a59dc57a4af025f554a0bbd")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);
driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a59de12a4af025f554a0bcb")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);
driver.execute_script("arguments[0].click();",button[1])
time.sleep(2);
driver.execute_script("arguments[0].click();",button[2])
time.sleep(2);
driver.execute_script("arguments[0].click();",button[3])
time.sleep(2);





driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a59dcb5a4af025f554a0bc1")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);
driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a59df31a4af025f554a0be8")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);


#MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f280f89496f09677d64e9")#link
driver.find_element_by_id("chkOpt3").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)
#MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f287289496f09677d64f2")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)
#MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f291189496f09677d64fd")#link
driver.find_element_by_id("chkOpt1").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)
#MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f298989496f09677d6527")#link
driver.find_element_by_id("chkOpt4").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)
#MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f29d789496f09677d652e")#link
driver.find_element_by_id("txtOutput0").send_keys("True")
driver.find_element_by_id("txtOutput1").send_keys("False")
driver.find_element_by_id("txtOutput2").send_keys("True")
driver.find_element_by_id("txtOutput3").send_keys("False")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)
#MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f2ba289496f09677d6563")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)
#MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f2be889496f09677d656d")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)


# c1

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f515c89496f09677d6947")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
    int data;
    struct Node* next;
};
Above structure is used to define the linked list, You have to complete the below functions only */
void forwardPrint(struct Node* head)
{
	if(head != NULL){
      cout<<head->data<<"-";
      forwardPrint(head->next);
    }
}
void backwardPrint(struct Node* head)
{
	if(head != NULL){
    backwardPrint(head->next);
    cout<<head->data<<"-";
  }
}

   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)


# c2

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a70766389496f09677d7734")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/*
struct Node
{
    int data;
    struct Node* next;
};
Above structure is used to define the linked list, You have to complete the below functions only */
struct Node *copyList(struct Node *org)
{
	 Node *ptr = NULL;
    while (org != NULL)
    {
      insertEnd(&ptr , org->data);
      org = org->next;
    }
    return ptr;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

#MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f2ccb89496f09677d6585")#link
driver.find_element_by_id("chkOpt3").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)


# c1

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a707dd489496f09677d78ad")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
    int data;
    struct Node* next;
};
Above structure is used to define the linked list, You have to complete the below functions only */
# include<bits/stdc++.h>
int minNode(Node *head){
    Node *last = head;
    int min = INT_MAX;
    while (last != NULL)
    {
        if(last->data < min){
            min = last->data;
        }
        last = last->next;
    }
    return min;
}
int maxNode(Node *head){
    Node *last = head;
    int max = INT_MIN;
    while (last != NULL)
    {
        if(last->data > max){
            max = last->data;
        }
        last = last->next;
    }
    return max;
}
void insertBeg(struct Node** head, int data){
  struct Node* node = (struct Node*) malloc(sizeof(struct Node));
  node->data  = data;     
  node->next = (*head);   
  (*head)    = node;  
}
struct Node * shiftSmallLarge(struct Node *org)
{
  	int x = minNode(org);
    int y = maxNode(org);
    if(org == NULL){
        return org;
    }
  	Node *ptr = NULL;
  	if(org->next == NULL){
        insertBeg(&ptr , x);
        return ptr;
    }
    Node *last = org;
    while (last != NULL)
    {
        if(last->data == x){
            last = last->next;
        }
        else if(last->data == y){
            last = last->next;
        }
        else{
            insertEnd(&ptr , last->data);
            last = last->next;
        }
    }
    insertBeg(&ptr , x);
    insertEnd(&ptr , y);
    return ptr;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)


# c2

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a71b21d89496f09677d87e7")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
    int data;
    struct Node* next;
};
Above structure is used to define the linked list, You have to complete the below functions only */
# include<bits/stdc++.h>
int checkPalindrome(struct Node* head) 
{
    if(head == NULL){
        return 0;
    }
	Node *ptr = head;
    stack<int> s;
    while (ptr != NULL)
    {
        s.push(ptr->data);
        ptr = ptr->next;
    }
    while (head != NULL)
    {
      int i = s.top();
      s.pop();
      if(head->data != i){
        return 0;
      }
      head = head->next;
    }
  return 1;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)


# c3

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a71aeac89496f09677d8758")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
    int data;
    Node* next;
};
Above structure is used to define the linked list, You have to complete the below functions only */
int countNodes(struct Node *n)
{
    int res = 1;
    struct Node *temp = n;
    while (temp->next != n)
    {
        res++;
        temp = temp->next;
    }
    return res;
}
int  loopInList(Node* head) {
  struct Node *slow_p = head, *fast_p = head;
    while (slow_p && fast_p &&
                     fast_p->next)
    {
        slow_p = slow_p->next;
        fast_p = fast_p->next->next;
        if (slow_p == fast_p)
            return countNodes(slow_p);
    }
    return 0;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)


# c4

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a71abef89496f09677d871c")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
    int data;
    struct Node* next;
};
Above structure is used to define the linked list, You have to complete the below functions only */
Node *ptr = NULL;
void giveReverse(Node *head){
  ptr = NULL;
    if(head != NULL){
      giveReverse(head->next);
      insertEnd(&ptr,head->data);
    }
}
struct Node* reverseList(struct Node* head) {
    giveReverse(head);
  	return ptr;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)


#MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f2ea689496f09677d65b4")#link
driver.find_element_by_id("txtOutput0").send_keys("1 3 5 5 3 1")
driver.find_element_by_id("txtOutput1").send_keys("1 2 3 3 2 1")
driver.find_element_by_id("txtOutput2").send_keys("1 1 2 2 1 1")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)
#MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f2fdd89496f09677d65e0")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)
#MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f309a89496f09677d65f9")#link
driver.find_element_by_id("txtOutput0").send_keys("2 1 4 3 6 5")
driver.find_element_by_id("txtOutput1").send_keys("1 1 2 2 3 3")
driver.find_element_by_id("txtOutput2").send_keys("1 1 2 1 2 2")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)
#MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f317b89496f09677d6626")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)


# c1

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a71b40f89496f09677d880a")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

// struct Node
// {
//   int data;
//   Node* next;
// };
// Above node is used to declare a node
Node* addListNumbers(Node* head1,Node* head2){
  	int x = 0;
    int i = 0;
    while (head1 != NULL)
    {
      int m = head1->data;
      x = m*pow(10,i) + x;
      i++;
      head1 = head1->next;
    }
    int y = 0;
    int j = 0;
    while (head2 != NULL)
    {
      int m = head2->data;
      y = m*pow(10,j) + y;
      j++;
      head2 = head2->next;
    }
    int sum = x+y;
    Node *ptr = NULL;
    while (sum > 0 )
    {
      int x = sum%10;
      insertEnd(&ptr ,x);
      sum = sum/10;
    }
    return ptr;
}   
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)


# c2

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a71b84689496f09677d8879")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""
void deleteNodeK(Node* node){
    if(node == NULL){
      return;
    }
    if (node->next == NULL)
    {
        //free(node);
        return;
    }
    Node* temp = node->next;
    node->data = temp->data;
    node->next = temp->next;
    free(temp);
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)


#########################################333
driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a6342b4e2509a3288171d66")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);
driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a634522e2509a3288171d76")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);
driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a634448e2509a3288171d72")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);
driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a6345c6e2509a3288171d7c")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);




#MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f336f89496f09677d6669")#link
driver.find_element_by_id("chkOpt4").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f496589496f09677d6863")#link
driver.find_element_by_id("txtOutput0").send_keys("5 4 3 2 1")
driver.find_element_by_id("txtOutput1").send_keys("3 3 2 2 1 1")
driver.find_element_by_id("txtOutput2").send_keys("6 5 2 3 4")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

#MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f49d489496f09677d686d")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)
#MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f4ac489496f09677d688c")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)
#MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f4b5389496f09677d68a0")#link
driver.find_element_by_id("chkOpt3").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)
#MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f4cc589496f09677d68c6")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)
#MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f4d4489496f09677d68ca")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)
#MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f4dca89496f09677d68d4")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)




# c1

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a71b9a389496f09677d88a7")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

   /* struct Node
{
    int data;
    struct Node *next;
  	struct Node *prev;
};
Above structure is used to define the linked list, You have to complete the below functions only */
void swapNodes(Node** head, int x, int y){
  		if(x == y){
       return;
   }
    Node *prevX = NULL , *currX = *head;
    while (currX && currX->data != x)
    {
        prevX = currX;
        currX = currX->next;
    }
    Node *prevY = NULL , *currY = *head;
    while (currY && currY->data != y)
    {
        prevY = currY;
        currY = currY->next;
    }
    if(currX == NULL || currY == NULL){
        return;
    }
    if(prevX != NULL){
        prevX->next = currY;
    }
    else{
        *head = currY;
    }
    if(prevY != NULL){
    prevY->next = currX;
    }
    else{
        *head = currX;
    }
    Node *temp = currY->next;
    currY->next = currX->next;
    currX->next = temp;
}


 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)


# c2

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a71d09b89496f09677d8d92")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

   /* struct Node
{
    int data;
    Node *next;
  	Node *prev;
};
Above structure is used to define the linked list, You have to complete the below functions only */
void insertAtBeg(Node **head , int data){
    Node *node = new Node(data);
    node->data = data;
    node->next = *head;
    node->prev = NULL;
    if(head != NULL){
        (*head)->prev = node;
    }
    *head = node;
}
int deleteAtEnd(Node *head){
    Node *last = head;
    while (last->next != NULL)
    {
        last = last->next;
    }
    int x = last->data;
    last->prev->next = NULL;
    delete(last);
    return x;
}
Node* rotateByK(Node* head, int k)
{
	 if(head == NULL){
        return head;
    }
    for (int i = 0; i < k; i++)
    {
        int x = deleteAtEnd(head);
        insertAtBeg(&head,x);
    }
    return head;
}


 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)


# c3

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a71d13989496f09677d8d9d")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
    int data;
    Node *next;
  	Node *prev;
};
Above structure is used to define the linked list, You have to complete the below functions only */
Node* rearrangeList(Node* head){
   int i = 1;
    Node *even = NULL;
    Node  *odd = NULL;
    Node *last = head;
    while (last != NULL)
    {
      if(i%2 == 0){
        even = insertEnd(even , last->data);
      }
      if(i%2 != 0){
        odd = insertEnd(odd , last->data);
      }
      last = last->next;
      i++;
    }
    Node *final = NULL;
    while (even != NULL)
    {
      final = insertEnd(final , even->data);
      even = even->next;
    }
    while (odd != NULL)
    {
      final = insertEnd(final , odd->data);
      odd = odd->next;
    }
    return final;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)


######################################################################333333

driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a6346f9e2509a3288171d86")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);
driver.execute_script("arguments[0].click();",button[1])
time.sleep(2)

#MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f4e8389496f09677d68eb")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f4f0a89496f09677d68f2")#link
driver.find_element_by_id("txtOutput0").send_keys("5")
driver.find_element_by_id("txtOutput1").send_keys("4")
driver.find_element_by_id("txtOutput2").send_keys("5")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)


# c1

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7593d2a0bdb04eb16c3c04")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
    int data;
    struct Node* next;
};
Above structure is used to define the linked list, You have to complete the below functions only */
int isCircular(Node* head){
  	if(head == NULL){
      return 1;
    }
  	Node *node = head->next;
      while (node != head && node != NULL)
      {
        node = node->next;
      }
      return (node == head);    
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)


# c2

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a759518a0bdb04eb16c3c0f")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

   /* struct Node
{
    int data;
    Node* next;
};
Above structure is used to define the linked list, You have to complete the below functions only */
Node* insertBeg(Node* head, int data){
  	 Node *ptr = new Node();
    ptr->data = data;
    ptr->next = NULL;
    Node *temp ;
    if(ptr == NULL){
        cout<<endl;
        printf("OVERFLOW");
    }
    else{
        if(head  == NULL){
            head = ptr;
            ptr->next = head;
        }
        else{
            temp = head;
            while (temp->next != head)
            {
                temp = temp->next;
            }
            ptr->next = head;
            temp->next = ptr;
            head = ptr;
        }
    }
  return head;
}
Node* insertEnd(Node* head, int data){
  Node *ptr = new Node();
    ptr->data = data;
    ptr->next = NULL;
    Node *temp ;
    if(ptr == NULL){
        cout<<endl;
        printf("OVERFLOW");
    }
    else{
        if(head  == NULL){
            head = ptr;
            ptr->next = head;
        }
        else{
            temp = head;
            while (temp->next != head)
            {
                temp = temp->next;
            }
            temp->next = ptr;
            ptr->next = head;
            return head;
        }
    }
}

 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)


# c3

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7595baa0bdb04eb16c3c19")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
    int data;
    Node* next;
};
Above structure is used to define the linked list, You have to complete the below functions only */
Node* deleteBeg(Node* head){
  	Node *p = head;
    while (p->next != head)
    {
        p = p->next;
    }
    p->next = head->next;
    int x = head->data;
    delete head;
    head = p->next;
    return head;
}
Node* deleteEnd(Node* head){
  	Node *p = head;
    while (p->next->next != head)
    {
        p = p->next;
    }
    Node *q = p->next;
    p->next = head;
    delete q;
    return head;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)


# c4

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a75964aa0bdb04eb16c3c20")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
    int data;
    Node* next;
};
Above structure is used to define the linked list, You have to complete the below functions only */
int countNodes(Node* head){
   int length = 0;
    if(head == NULL){
        return 0;
    }
    Node *p = head;
    while (p->next != head)
    {
        length++;
        p = p->next;
    }
    return length+1;
}

   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)


# c5

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7597cfa0bdb04eb16c3c26")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
    int data;
    struct Node* next;
};
Above structure is used to define the linked list, You have to complete the below functions only */
void sortedInsert(Node **head , Node *newN){
    Node *current = *head;
    if(current == NULL){
        newN->next = newN;
        *head = newN;
    }
    else if(current->data >= newN->data){
        /* If value is smaller than head's value then
        we need to change next of last node */
        *head = insertBeg(*head , newN->data);
    }
    else{
        /* Locate the node before the point of insertion */
        while (current->next != *head && current->next->data < newN->data)
        {
            current = current->next;
        }
        newN->next = current->next;
        current->next = newN;
    }
}
Node* insertSorted(Node* head , int k){
    Node *ptr = new Node();
    ptr->data = k;
    sortedInsert(&head ,ptr);
    return head;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)


# c6

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a759729a0bdb04eb16c3c23")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
    int data;
    struct Node* next;
};
Above structure is used to define the linked list, You have to complete the below functions only */
Node* listCut(Node* head){
 Node *head1=NULL;
  Node *head2=NULL;
  Node *temp1=head;
  Node *temp2=head;
  if(head==NULL) return 0;
  while(temp2->next!=head && temp2->next->next!=head){
    temp2=temp2->next->next;
    temp1=temp1->next;
  }
  if(temp2->next->next==head) temp2=temp2->next;
  head1=head;
  if(head->next!=head) head2=temp1->next;
  temp2->next=temp1->next;
  temp1->next=head;
  return head1,head2;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)
