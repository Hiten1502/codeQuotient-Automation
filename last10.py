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





#################################### Module Stack##############################

# # 4
# driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a12f3ec46765b2b63e347fe")
# driver.find_element_by_class_name("btn").click()#Submit Button
# time.sleep(2)

driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a12f3ec46765b2b63e347fe")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);

driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a12f48346765b2b63e34805")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);
driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a706b9c89496f09677d755f")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);
driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a706cd489496f09677d7578")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);
driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a706ebd89496f09677d75cd")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);


# MCQ1
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a705c2489496f09677d73cf")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# MCQ2
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a705ca889496f09677d73d0")#link
driver.find_element_by_id("txtOutput0").send_keys("DEOOUQITCETN")
driver.find_element_by_id("txtOutput1").send_keys("EDOCOUQITNET")
driver.find_element_by_id("txtOutput2").send_keys("OCEDOITEUQTN")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a705d8789496f09677d73e1")#link
driver.find_element_by_id("chkOpt3").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# MCQ4
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a705e2589496f09677d73e6")#link
driver.find_element_by_id("chkOpt4").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# # MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a705ea889496f09677d73ef")#link
driver.find_element_by_id("chkOpt3").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)


#c1
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a71d4bc89496f09677d8f1d")#link


t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

int isFull()
{
	return top == SIZE - 1;
}
// Function to check if stack is empty.
int isEmpty()
{
	return top == -1;
}
// Function to add an item to stack.
int push(int item)
{
	 if (isFull())
    {
        return -1;
    }
    else{
        Stack[++top] = item;
    }
}
// Function to remove an item from stack.
int pop()
{
	if(isEmpty()){
        return -1;
    }
    else{
        int val = Stack[top--];
        return val;
    }
}

""")
pyautogui.hotkey('ctrl', 'v')



WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)


# #c2

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a71d80889496f09677d8f55")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

string reverseString(CQStack *stack,string s){
  	 string ans = "";
    CQStack *sp = new CQStack(s.length());
    for (int i = 0; i < s.length(); i++)
    {
        sp->push(s[i]);
    }
    for (int i = 0; i < s.length(); i++)
    {
        int temp = sp->pop();
        ans += temp;
    }
    return ans;
}


""")
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)


# MCQ6
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a705f0989496f09677d73f0")#link
driver.find_element_by_id("chkOpt4").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# #c3

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a71d70489496f09677d8f46")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

class LinkStack{
  LinkList *first; // ref to first item on list
  int size;
  public:
    LinkStack(){
      	first = NULL;
        size = 0; 
    }
    bool isEmpty(){
		return first == NULL;
    }
    void push(int dd){
 		LinkList *ptr = new LinkList(dd);
         ptr->next = first;
         first = ptr;
         size ++;
     }
     int pop(){
 		if(isEmpty()){
             return -1;
         }
         size--;
         int temp = first->data;
         first = first->next;
         return temp;
     }
 };
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)


# #c4

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7338967e4d2702dca0472c")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""
 void push(int item)
 {
 	if (isFull())
     {
         return;
     }
     else{
         Stack[++top] = item;
     }
 }
 // Function to remove an item from stack.
 int pop()
 {
 	 if(isEmpty()){
         return -1;
     }
     else{
         int val = Stack[top--];
         return val;
     }
 }
 // Function to return the minimum item from stack.
 int getMin()
 {
 	 int a = top;
     int min = Stack[a];
     while (a != -1)
     {
         int x = Stack[a];
         if(x<min){
             min = x;
         }
         a--;
     }
     return min;
 }


 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)


# #c5

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a73399d7e4d2702dca04734")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

 void printNextGreaterElement(int arr[],int n){
   for (int i = 0; i < n; i++)
     {
         for (int j = i; j < n; j++)
         {
             if(arr[j]>arr[i]){
                 cout<<arr[j]<<" ";
                 break;
             }
             else if(j == n-1){
                 cout<<"-1"<<" ";
             }
         }
     }
 }
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# #c6

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a733a277e4d2702dca0473c")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

 int minReversal(char* expr){
   int len = strlen(expr);
     if (len%2)
 	return -1;
 	stack<char> s;
 	for (int i=0; i<len; i++)
 	{
 		if (expr[i]==']' && !s.empty())
 		{
 			if (s.top()=='[')
 				s.pop();
 			else
 				s.push(expr[i]);
 		}
 		else
 			s.push(expr[i]);
 	}
 	int x = s.size();
 	int n = 0;
 	while (!s.empty() && s.top() == '[')
 	{
 		s.pop();
 		n++;
 	}
 	return (x/2 + n%2);
 }
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)


# MCQ1
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a705f5f89496f09677d73f6")#link
driver.find_element_by_id("txtOutput0").send_keys("-24")
driver.find_element_by_id("txtOutput1").send_keys("52")
driver.find_element_by_id("txtOutput2").send_keys("4")
driver.find_element_by_id("txtOutput3").send_keys("-18")
driver.find_element_by_id("txtOutput4").send_keys("350")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

# MCQ2
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a705fa089496f09677d73fe")#link
driver.find_element_by_id("txtOutput0").send_keys("3")
driver.find_element_by_id("txtOutput1").send_keys("2205")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a70601589496f09677d7409")#link
driver.find_element_by_id("txtOutput0").send_keys("xy+2^x4-3/+")
driver.find_element_by_id("txtOutput1").send_keys("+^+xy2/-x43")
driver.find_element_by_id("txtOutput2").send_keys("ABC+-D*")
driver.find_element_by_id("txtOutput3").send_keys("*-A+BCD")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)


# MCQ4
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7060fd89496f09677d7423")#link
driver.find_element_by_id("chkOpt1").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)


# #c7

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a733bbc7e4d2702dca04794")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""
 struct stack{
   int size;
   char data;
   int top;
 };
 int isOperand(char ch){
     return (ch>= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z' || (isdigit(ch)));
 }
 int checkPrecedence(char ch){
     switch(ch){
         case '+':
         case '-':
             return 1;
         case '*':
         case '/':
             return 2;
         case '^':
             return 3;
     }
     return -1;
 }
 int infixToPostfix(char exp[], char output[])
 {
 	 int i = 0,k = 0;
     while (exp[i])
     {
         if(isOperand(exp[i])){
             output[k++] = exp[i];
         }
         else if(exp[i] == '('){
             push(exp[i]);
         }
         else if(exp[i] == ')'){
             while (!isEmpty() && Stack[top] != '(')
             {
                 output[k++] = Stack[top];
                 pop();
             }
             if(!isEmpty() && Stack[top] != '('){
                 return -1;
             }
             else{
                 pop();
             }
         }
         else{
             while (!isEmpty() && checkPrecedence(exp[i]) <= checkPrecedence(Stack[top]))
             {
                 output[k++] = Stack[top];
                 pop();
             }
             push(exp[i]);
         }
         i++;
     }
     while (!isEmpty())
     {
         output[k++] = Stack[top];
         pop();
     }
     output[k++] = '\\0';
 }
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# #c8

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a733c607e4d2702dca0479b")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

 int evalPostfix(CQStack *stack,string exp){
     int answer;
     CQStack *st = new CQStack(exp.length());
     for (int i = 0; i < exp[i]; i++)
     {
         if(isdigit(exp[i])){
             st->push(exp[i] - '0');
         }
         else{
             int op2 = st->pop();
             int op1 = st->pop();
             switch (exp[i])
             {
             case '+':
                 st->push(op1 + op2);
                 break;
             case '-':
                 st->push(op1 - op2);
                 break;
             case '*':
                 st->push(op1 * op2);
                 break;
             case '/':
                 st->push(op1 / op2);
                 break;
               case '^':
                 st->push(pow(op1,op2));
             }
         }
     }
     answer = st->pop();
     return answer;
 }
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# #c9

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a733d077e4d2702dca047ab")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""
 int evalPrefix(char* exp)
 {
 	int i,op1,op2;
   	int len = strlen(exp);
 	for ( i = len-1; i>=0 ; i--)
     {
       char c = exp[i];
       if (isdigit(c))
         push(c-'0');
       else
       {
         op1 = pop();
         op2 = pop();
         switch(c)
         {
           case '+': push(op1 + op2); break;
           case '-': push(op1 - op2); break;
           case '*': push(op1 * op2); break;
           case '/': push(op1 / op2); break;
           case '^':push(pow(op1,op2)); break;
         }
       }
     }
  	return pop();
 }
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)



################Queue Module#####################

driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a563aa5c83e417a5c00dbf3")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);
driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a563c20c83e417a5c00dc13")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);

# MCQ1
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a70659c89496f09677d74bb")#link
driver.find_element_by_id("chkOpt3").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)


# MCQ2
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7065fe89496f09677d74c2")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)


# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a70663389496f09677d74c8")#link
driver.find_element_by_id("txtOutput0").send_keys("CODEQUOTIENT")
driver.find_element_by_id("txtOutput1").send_keys("CODEQUOTIENT")
driver.find_element_by_id("txtOutput2").send_keys("CODEQUOTIENT")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)


# c1

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a733ecf7e4d2702dca04877")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""
 void enqueue(int item)
{
	if(rear == SIZE){
      return;
    }
    if(front == -1 && rear == -1){
      front++;
      rear++;
    }
    else{
      rear++;
    }
    array[rear] = item;
}
// Method to remove an item from queue.
int dequeue()
{
	if(front>rear){
    return -1;
  }
  int item = array[front];
  front++;
  return item;
}
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)


# MCQ4
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a70668889496f09677d74d3")#link
driver.find_element_by_id("chkOpt3").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a70675389496f09677d74eb")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# MCQ6
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7067c889496f09677d74f3")#link
driver.find_element_by_id("chkOpt3").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# MCQ7
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a70684489496f09677d74f4")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)


# c2

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7340417e4d2702dca04904")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""
class Queue { 
    struct QNode { 
        int data; 
        QNode* next; 
        QNode(int d){ 
            data = d; 
            next = NULL; 
        } 
    }; 
    QNode *front, *rear; 
    public:
  		// Constructor
        Queue(){
        }
  		// Add an element to the queue
        void enQueue(int x){
			QNode* newNode = new QNode(x);
      if(rear == NULL){
          front = rear = newNode;
          return;
      }
      rear->next = newNode;
      rear = newNode;
        }
  		// Delete front element from the queue
        int deQueue() { 
			 if(front == NULL){
          return -1;
       }
        int temp = front->data;
        front = front->next;
        if (front == NULL){
            rear = NULL;
        }
        return temp;
        }
};
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)


# c3

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7341a37e4d2702dca0492c")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""
 void reverseQueue(Queue *queue){
  // Write your code here 
  int arr[1000];
   int i = 0;
   while (!queue->isEmpty())
   {
       int temp = queue->deQueue();
       arr[i] = temp;
      i++;
   }
  for (int j = i-1; j >= 0; j--)
  {
    int x = arr[j];
    queue->enQueue(x);
  }
}
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)


# c4

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7344a27e4d2702dca04960")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""
/* push(int), pop(), isEmpty(), isFull() are available on Stack. */
class Queue
{
  //Beaware to do it public
  public:
  void enqueue(CQStack *st1, CQStack *st2, int item)
  {
		st1->push(item);
  }
  int dequeue(CQStack *st1, CQStack *st2)
  {
		if(st2->isEmpty() && st1->isEmpty()){
          return -1;
        }
        if(st2->isEmpty()){
            while (!st1->isEmpty())
            {
                st2->push(st1->pop());
            }
        }
        int temp = st2->pop();
        return temp;
  }
};
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)


# c5

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7345b27e4d2702dca049b4")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""
class Stack
{
  public:
  void push(QueueArray* qa1, QueueArray* qa2, int item)
  {
     while (!(qa1->front > qa1->rear))
      {
          qa2->enqueue(qa1->dequeue());
      }
      qa1->enqueue(item);
      while (!(qa2->front > qa2->rear))
      {
          qa1->enqueue(qa2->dequeue());
      }
  }
  int pop(QueueArray* qa1, QueueArray* qa2)
  {
    if((qa1->front > qa1->rear)){
          return -1;
      }
      int x = qa1->dequeue();
      return x;
  }
};
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)



################CQueue Module#####################


driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a563b1fc83e417a5c00dc06")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);

# MCQ1
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7068a289496f09677d7505")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)
# MCQ2
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a70690489496f09677d750e")#link
driver.find_element_by_id("txtOutput0").send_keys("2 5")
driver.find_element_by_id("txtOutput1").send_keys("2 0")
driver.find_element_by_id("txtOutput2").send_keys("2 1")
driver.find_element_by_id("txtOutput3").send_keys("3 1")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

# c1

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a759ed8a0bdb04eb16c3d28")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""
// class QueueArray{
//   const int SIZE = 4; // Size of queue array
//   int front = -1; // front variable
//   int rear = -1; // rear variable
//   int *queue; // queue array 
//   public:
//   	QueueArray() // constructor 
//   	void enQueue(int data); // add data to the queue
//   	int deQueue(); // remove data from the queue
// };
// The above declaration is already done. Complete the function given below.
// Add data to the circular queue
void QueueArray::enQueue(int data){
   if((front == 0 && rear == SIZE-1) || (rear == (front - 1)%(SIZE-1))){
        return ;
    }
    if(front == -1){
        front = rear = 0;
    }
    else if(rear == SIZE-1 && front != 0){
        rear = 0;
    }
    else{
        rear++;
    }
    queue[rear] = data;
}
// Remove First element from queue
int QueueArray::deQueue(){
  if(front == -1){
        return -1;
    }
    int item = queue[front];
    if(front == rear ){
        front  = rear = -1;
    }
    else if(front == SIZE-1){
        front = 0;
    }
    else{
        front++;
    }
    return item;
}
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)


################CQueue Module#####################

driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a634bade2509a3288171dae")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);
driver.execute_script("arguments[0].click();",button[1])
time.sleep(2)
driver.execute_script("arguments[0].click();",button[2])
time.sleep(2)

# MCQ1
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a70693989496f09677d7516")#link
driver.find_element_by_id("chkOpt3").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# MCQ2
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a70698e89496f09677d7522")#link
driver.find_element_by_id("chkOpt4").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)


# c1

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a75d71da0bdb04eb16c3f35")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

// struct Node{
//   int data;
//   int priority;
//   Node* next;
//   Node();
//   Node(int d,int p);
// };
// The above structure is used to declare a node
# include<bits/stdc++.h>
class PriorityQueue{
    Node *front, *rear;
    public:
      PriorityQueue(){
        front = NULL;
        rear = NULL;
      }
    void enQueue(int data,int priority){
      Node *tmp , *q;
      tmp = new Node(data,priority);
      if(front == NULL || priority < front->priority){
        tmp->next = front;
        front = tmp;
      }
      else{
        q = front;
        while (q->next != NULL && q->next->priority <= priority)
        {
          q = q->next;
        }
        tmp->next = q->next;
        q->next = tmp;
      }
    }
  	int deQueue(){
          Node *tmp;
          if(front == NULL){
              return -1;
          }
          else
          {
            tmp = front;
            int x = tmp->data;
            // cout<<tmp->data<<" ";
            front = front->next;
            free(tmp);
            return x;
          }
          return -1;		
    }
};


   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)




###############Sorting Module#####################

driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a12e62546765b2b63e34716");
time.sleep(2)

driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a12e7f046765b2b63e34748")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2)
driver.execute_script("arguments[0].click();",button[1])
time.sleep(2)

driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a12e94346765b2b63e34754")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2)

driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a12e8a046765b2b63e3474e")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2)

# driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a12ec9446765b2b63e34761")
# button = driver.find_elements_by_xpath("//a[text()='run']")
# driver.execute_script("arguments[0].click();",button[0])
# time.sleep(2);

# driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a12ea7a46765b2b63e3475a")
# button = driver.find_elements_by_xpath("//a[text()='run']")
# driver.execute_script("arguments[0].click();",button[0])
# time.sleep(2);





# MCQ1
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a488e3fb1afa55f38fed743")#link
driver.find_element_by_id("txtOutput0").send_keys("4")
driver.find_element_by_id("txtOutput1").send_keys("2")
driver.find_element_by_id("txtOutput2").send_keys("3")
driver.find_element_by_id("txtOutput3").send_keys("1")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

# MCQ1
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a488e6cb1afa55f38fed749")#link
driver.find_element_by_id("chkOpt1").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# MCQ2
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a488eb2b1afa55f38fed74a")#link
driver.find_element_by_id("chkOpt1").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a488ed8b1afa55f38fed74b")#link
driver.find_element_by_id("chkOpt1").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# MCQ4
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a488f09b1afa55f38fed74c")#link
driver.find_element_by_id("chkOpt1").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)



# c1

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a4fb6d87a3c1824dba9142b")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""
    # include<bits/stdc++.h>
using namespace std;
int numberOfSwaps(int *A,int n){
    int isSorted = 1;
    int swap(0);
    for (int i = 0; i < n-1; i++)
    {
        for (int j = 0; j < n-i-1; j++)
        {
            if(A[j]>A[j+1]){
                int temp = A[j];
                A[j] = A[j+1];
                A[j+1] = temp;
                isSorted = 0;
                swap++;
            }
        }
        if(isSorted){
            return swap;
        }
    }
    return swap;
}
int main(){
    int t;
    cin>>t;
    while(t--){
        int n;cin>>n;
        int arr[n];
        for (int i = 0; i < n; i++)
        {
            cin>>arr[i];
        }
        cout<<numberOfSwaps(arr,n)<<endl;
    }
    return 0;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# MCQ1
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a489029b1afa55f38fed752")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)
# MCQ2
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a489053b1afa55f38fed753")#link
driver.find_element_by_id("chkOpt1").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)
# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a489079b1afa55f38fed754")#link
driver.find_element_by_id("chkOpt1").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)
# MCQ4
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a48909bb1afa55f38fed755")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)
# MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a4890bbb1afa55f38fed756")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)


# c1

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a4fb7f57a3c1824dba9142e")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

# include<bits/stdc++.h>
using namespace std;
void swap(int *a,int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}
int swaps(int arr[],int n){
    int min_index;
    int cnt = 0;
    for (int i = 0; i < n-1; i++)
    {
        min_index = i;
        int c = 0;
        for (int j = i+1; j < n; j++)
        {
            if(arr[j]<arr[min_index]){
                min_index = j;
                c= 1;
            }
        }
        if(c == 1){
            cnt++;
            c = 0;
        }
        swap(&arr[min_index],&arr[i]);
    }
    return cnt;
}
int main(){
    int t;
    cin>>t;
    while(t--){
        int n;cin>>n;
        int arr[n];
        for (int i = 0; i < n; i++)
        {
            cin>>arr[i];
        }
        cout<<swaps(arr,n)<<endl;
    }
    return 0;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# MCQ1
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a488f53b1afa55f38fed74d")#link
driver.find_element_by_id("chkOpt3").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)
# MCQ2
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a488f8db1afa55f38fed74e")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)


# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a488fb6b1afa55f38fed74f")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)
# MCQ4
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a488fe0b1afa55f38fed750")#link
driver.find_element_by_id("chkOpt3").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)
# MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a489006b1afa55f38fed751")#link
driver.find_element_by_id("chkOpt3").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)


# c1

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5d88852cffddab5e789a0efd")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

    # include<bits/stdc++.h>
using namespace std;
int InsertionSort(int *A,int n){
    int cnt = 0;
    int key,j;
    for (int i = 1; i <= n-1; i++)
    {
        key = A[i];
        j = i-1;
        int in = 0;
        while (j>=0 && A[j]>key)
        {
            A[j+1] = A[j];
            j--;
            cnt++;
            in = 1;
        }
        if(in == 1){
            cnt++;
            in = 0;
        }
        A[j+1] = key;
    }
    return cnt;
}
int main(){
    int t;
    cin>>t;
    while (t--)
    {
        int n;
        cin>>n;
        int arr[n];
        for (int i = 0; i < n; i++)
        {
            cin>>arr[i];
        }
        cout<<InsertionSort(arr,n)<<endl;
    }
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)





# c2

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5c27689e1bc7780800776e36")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* This function picks an element as pivot, places the pivot element at its correct position in sorted array, and places all smaller (smaller than pivot) 
   to left of pivot and all greater elements to right of pivot */
void swap(int* a, int* b)    
{
  int t = *a;
  *a = *b;
  *b = t;
}
int partition (int array[], int low, int high) {
  int pivot = array[high];
    int i = low - 1;
    int j;
    for ( j = low; j <= high-1; j++)
    {
            if(array[j] <= pivot){
                i++;
                swap(&array[i],&array[j]);
            }
    }
    swap(&array[i + 1], &array[high]);
    return (i + 1);
}
/* low is for left index and high is right index of the sub-array of arr to be sorted */
void quickSort(int array[], int low, int high) {
  if (low < high)
  {
    int pivot_index;
    pivot_index = partition(array, low, high);
    quickSort(array, low, pivot_index - 1);
    quickSort(array, pivot_index + 1, high);
  }
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)




# c3

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5c2767981bc7780800776e11")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] and Second subarray is arr[m+1..r] 
void merge(int array[], int l, int m, int r) {
  int i,j,k,B[r+1];
    i = l;
    j = m + 1;
    k = l;
    while (i<=m && j<=r)
    {
        if(array[i] < array[j]){
            B[k] = array[i];
            i++;
            k++;
        }
        else{
            B[k] = array[j];
            j++;
            k++;
        }
    }
    while (i <= m)
    {
        B[k] = array[i];
        k++;
        i++;
    }
    while (j <= r)
    {
        B[k] = array[j];
        k++;
        j++;
    }
    for (int i = l; i <= r ; i++)
    {
        array[i] = B[i];
    }
}
/* l is for left index and r is right index of the sub-array of arr to be sorted */
void mergeSort(int array[], int l, int r) {
   int mid;
    if(l<r){
        mid = (l+r)/2;
        mergeSort(array,l,mid);
        mergeSort(array,mid+1,r);
        merge(array,l,mid,r);
    }
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)





#######################Binary Tree############################

# driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a76cbeea0bdb04eb16c4867")
# button = driver.find_elements_by_xpath("//a[text()='run']")
# driver.execute_script("arguments[0].click();",button[0])
# time.sleep(2)

# driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a76cc84a0bdb04eb16c487d")
# button = driver.find_elements_by_xpath("//a[text()='run']")
# driver.execute_script("arguments[0].click();",button[0])
# time.sleep(2)

# driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a76e2f2a0bdb04eb16c4970")
# button = driver.find_elements_by_xpath("//a[text()='run']")
# driver.execute_script("arguments[0].click();",button[0])
# time.sleep(2)

# driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a76e46fa0bdb04eb16c4985")
# button = driver.find_elements_by_xpath("//a[text()='run']")
# driver.execute_script("arguments[0].click();",button[0])
# time.sleep(2);
# driver.execute_script("arguments[0].click();",button[1])
# time.sleep(2)
# driver.execute_script("arguments[0].click();",button[2])
# time.sleep(2)


# MCQ1
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a76ea3ca0bdb04eb16c4a15")#link
driver.find_element_by_id("chkOpt4").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# MCQ2
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a76eac1a0bdb04eb16c4a18")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a76eb7ea0bdb04eb16c4a26")#link
driver.find_element_by_id("chkOpt1").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# MCQ4
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a76ebe4a0bdb04eb16c4a2c")#link
driver.find_element_by_id("chkOpt1").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)


# c1

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7c6b36ce59546fd7abfdad")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""
/* struct Node {
  int data;
  struct Node *left, *right;
};						
The above structure is used for tree node and the function below is also provided to build a new node with given data. 
struct Node* newNode(int data);
*/
struct Node * createBT(int arr[],Node *root,int i,int n){
    if(i<n){
        Node *temp = newNode(arr[i]);
        root = temp;
        root->left = createBT(arr,root->left,2*i+1,n);
        root->right = createBT(arr,root->right,2*i+2,n);
    }
    return root;
}
struct Node* buildTree(int t[], int n){
    int i = 0;
    Node *root = createBT(t,root,i,n);
    return root;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)


# c1

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a75d71da0bdb04eb16c3f35")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# c2

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7c6e1cce59546fd7abfdc6")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

   /* struct Node
{
  int data;
  struct Node *left, *right;
};
The above structure is used for tree node.
*/
# include<queue>
void printLevelWise(struct Node* root){
  	if (root == NULL){ 
        return;
    }
    queue<Node *> q;
    q.push(root);
    while (q.empty() == false)
    {
        int nodeCount = q.size();
        while (nodeCount>0)
        {
            Node *node = q.front();
            cout<<node->data;
          	if(nodeCount>1){
              cout<<" ";
            }
            q.pop();
            if(node->left != NULL){
                q.push(node->left);
            }
            if(node->right != NULL){
                q.push(node->right);
            }
            nodeCount--;
        }
        cout<<endl;
    }
}

 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# c3

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7c723c9fedba282eab5021")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
  int data;
  struct Node *left, *right;
};
The above structure is used for tree node.
*/
int height(Node *root){
    if(root == NULL){
        return 0;
    }
    else{
        int left_height = height(root->left);
        int right_height = height(root->right);
        return max(left_height,right_height)+1;
    }
}
void printGivenLevel(struct Node* root, int level)
{
    if (root == NULL)
        return;
    if (level == 1)
        printf("%d ", root->data);
    else if (level > 1)
    {
        printGivenLevel(root->left, level-1);
        printGivenLevel(root->right, level-1);
    }
}
void printOdd(struct Node* root)
{
	 int h = height(root);
	for (int i = 1; i <= h; i+=2)
	{
		printGivenLevel(root,i);
	}
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# c4

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7c767fd287a634f8535300")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""
/* struct Node
{
  int data;
  struct Node *left, *right;
};
The above structure is used for tree node. */
void printInorder(struct Node* root)
{
	if(root != NULL){
        printInorder(root->left);
        cout<<root->data<<" ";
        printInorder(root->right);
    }
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# c5

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7c77ecd287a634f853530e")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
  int data;
  Node *left, *right;
};
The above structure is used for tree node.
*/
void inorder(Node* root){
  if(root != NULL){
      inorder(root->left);
      printf("%d ",root->data);
      inorder(root->right);
  }
}
void preorder(Node* root){
  if(root != NULL){
      printf("%d ",root->data);
      preorder(root->left);
      preorder(root->right);
  }
}
void postorder(Node* root){
  if(root != NULL){
        postorder(root->left);
        postorder(root->right);
        printf("%d ",root->data);
    }
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# c6

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7c794fd287a634f8535319")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
  int data;
  struct Node *left, *right;
};
The above structure is used for tree node and the function below is also provided to build a new node with given data. 
struct Node* newNode(int data);
*/
int search(int arr[], int strt, int end, int value)
{
    int i;
    for (i = strt; i <= end; i++) {
        if (arr[i] == value)
            break;
    }
    return i;
}
Node *buildUtil(int in[],int post[],int inStrt,int inEnd,int *pIndex){
	if(inStrt > inEnd){
		return NULL;
	}
	Node *node = newNode(post[*pIndex]);
	(*pIndex)--;
	if(inStrt == inEnd){
		return node;
	}
	int inIndex = search(in ,  inStrt , inEnd , node->data);
	node->right = buildUtil(in, post, inIndex + 1, inEnd, pIndex);
    node->left = buildUtil(in, post, inStrt, inIndex - 1, pIndex);
    return node;
}
Node* buildTree(int in[], int post[], int N){
	int pIndex = N - 1;
	return buildUtil(in , post , 0 , N-1 , &pIndex);
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# c7

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7da2cad287a634f8535a33")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
  int data;
  struct Node *left, *right;
};
The above structure is used for tree node. */
int countLeafs(struct Node* root) 
{
	if (root == NULL)
    {
        return 0;
    }
    if (root->left == NULL && root->right == NULL)
    {
        return 1;
    }
    return countLeafs(root->left) + countLeafs(root->right);
}
int countNonLeafs(struct Node* root) 
{
	if(root == NULL || (root->left == NULL && root->right == NULL)){
        return 0;
    }
    return 1 + countNonLeafs(root->left) + countNonLeafs(root->right);
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# c8

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7da375d287a634f8535a48")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
  int data;
  Node *left, *right;
};
The above structure is used for tree node. */
void printArray(int ints[], int len)
{
	int i;
	for (i = 0; i < len; i++)
	{
		cout << ints[i] << " ";
	}
}
int x = 0;
void printPathsRecur(Node* node, int path[], int pathLen)
{
	if (node == NULL) return;
	path[pathLen] = node->data;
	pathLen++;
	if (node->left == NULL && node->right == NULL)
	{
      	x++;
		printArray(path, pathLen);
        cout<<(pathLen-1)<<endl;
	}
	else
	{
		printPathsRecur(node->left, path, pathLen);
		printPathsRecur(node->right, path, pathLen);
	}
}
void printAllPaths(Node* root) {
  	int path[1000];
	printPathsRecur(root, path, 0);
  if(root != NULL){
    cout<<x;
  }
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# c9

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7da3ffd287a634f8535a63")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
  int data;
  struct Node *left, *right;
};
The above structure is used for tree node and the function below is also provided to build a new node with given data. 
struct Node* newNode(int data);
*/
# include<queue>
Node * nextRight(Node *root ,int k){
    if(root == NULL){
        return 0;
    }
    queue<Node *> qn;
    queue<int> ql;
    int level = 0;
    qn.push(root);
    ql.push(level);
    while (qn.size())
    {
        Node *node = qn.front();
        level = ql.front();
        qn.pop();
        ql.pop();
        if(node->data == k){
            if(ql.size() == 0 || ql.front() != level){
                return NULL;
            }
            return qn.front();
        }
        if(node->left != NULL){
            qn.push(node->left);
            ql.push(level+1);
        }
        if(node->right != NULL){
            qn.push(node->right);
            ql.push(level+1);
        }
    }
    return NULL;
}
int findRightSibling(struct Node* root, int key){
  Node *nr = nextRight(root,key);
    if(nr != NULL){
        return nr->data;
    }
    return -1;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)




#######################Binary Tree############################

# driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a76e6cca0bdb04eb16c49b9")
# button = driver.find_elements_by_xpath("//a[text()='run']")
# driver.execute_script("arguments[0].click();",button[0])
# time.sleep(2);
# driver.execute_script("arguments[0].click();",button[1])
# time.sleep(2)

# driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a76e775a0bdb04eb16c49d8")
# button = driver.find_elements_by_xpath("//a[text()='run']")
# driver.execute_script("arguments[0].click();",button[0])
# time.sleep(2);

# driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a76e7f7a0bdb04eb16c49e5")
# button = driver.find_elements_by_xpath("//a[text()='run']")
# driver.execute_script("arguments[0].click();",button[0])
# time.sleep(2);

# MCQ1
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a76ec53a0bdb04eb16c4a34")#link
driver.find_element_by_id("chkOpt3").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# MCQ2
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a76eca4a0bdb04eb16c4a35")#link
driver.find_element_by_id("chkOpt4").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a76ed70a0bdb04eb16c4a4a")#link
driver.find_element_by_id("chkOpt3").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# MCQ4
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a76eda4a0bdb04eb16c4a4e")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a76edc8a0bdb04eb16c4a4f")#link
driver.find_element_by_id("chkOpt3").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# MCQ6
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a76ee36a0bdb04eb16c4a61")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# MCQ7
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a76ee68a0bdb04eb16c4a62")#link
driver.find_element_by_id("txtOutput0").send_keys("3")
driver.find_element_by_id("txtOutput1").send_keys("3")
driver.find_element_by_id("txtOutput2").send_keys("2")
driver.find_element_by_id("txtOutput3").send_keys("5")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)



# c1

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7dae0ad287a634f8535d3a")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
  int data;
  struct Node *left, *right;
};
The above structure is used for tree node. */
int isBinarySearchTree(struct Node* t1){
 	static struct Node *prev = NULL;
    if(t1 != NULL){
        if(!isBinarySearchTree(t1->left)){
            return 0;
        }
        if(prev != NULL && t1->data <= prev->data){
            return 0;
        }
        prev = t1;
        return isBinarySearchTree(t1->right);
    }
    else{
        return 1;
    }
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)



# c2

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7daefad287a634f8535d43")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
  int data;
  Node *left, *right;
};
The above structure is used for tree node. */
# include<bits/stdc++.h>
int x = 0;
int arr[100];
void makeArray(Node *t1,int k){
    if(t1 != NULL){
        arr[x] = t1->data;
        x++;
        makeArray(t1->left,k);
        makeArray(t1->right,k);
    }
}
int kSmallest(Node* t1, int k){
   makeArray(t1,k);
    sort(arr,arr+x); 
    int y = arr[k-1];
    return y;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)



# c3

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7db00bd287a634f8535dee")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

    /* struct Node
{
  int data;
  Node *left, *right;
};
The above structure is used for tree node and also one function to create a new node as below is provided. 
Node* newNode(int data); 	*/
struct Node * insert(Node *root,int key){
    if(root == NULL){
        Node *temp = newNode(key);
        return temp;
    }
    if(key < root->data){
        root->left = insert(root->left,key);
    }
    else if(key > root->data){
        root->right = insert(root->right,key);
    }
    return root;
}
Node* buildSearchTree(int t[], int n){
  if(n == 0){
    return NULL;
  }
    Node* root = newNode(t[0]);
    for (int i = 1; i < n; i++)
    {
        insert(root,t[i]);
    }
    return(root);
}

 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)



#############################Heap Module#############




driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a7dc61ad287a634f8535f39")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);





# MCQ1
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7dc881d287a634f8535ffe")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# MCQ2
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7dc8b8d287a634f8536005")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7dcac7d287a634f8536016")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# MCQ4
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7dcb4bd287a634f8536017")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7dcb9dd287a634f8536018")#link
driver.find_element_by_id("chkOpt3").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# MCQ6
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7dcbd9d287a634f8536019")#link
driver.find_element_by_id("txtOutput0").send_keys("No")
driver.find_element_by_id("txtOutput1").send_keys("Yes")
driver.find_element_by_id("txtOutput2").send_keys("No")
driver.find_element_by_id("txtOutput3").send_keys("Yes")
driver.find_element_by_id("txtOutput4").send_keys("No")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

# MCQ7
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7dcc73d287a634f8536020")#link
driver.find_element_by_id("chkOpt4").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# MCQ8
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7dcd18d287a634f8536021")#link
driver.find_element_by_id("txtOutput0").send_keys("4 5 9 14 10 8 6 12 7")
driver.find_element_by_id("txtOutput1").send_keys("14 10 9 8 5 12 7 6 4")

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)



# c1

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7ec9fbd287a634f85366ac")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

void printKLargest(int array[],int n,int k){
    sort(array , array + n);
    for (int i = n-1; i > n-1-k; i--)
    {
      cout<<array[i];
      if(i > (n-k )){
        cout<<" "; 
      }
    }
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# c2

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7eca50d287a634f85366af")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

void maxHeapify(int arr[] , int i , int n){
    int l = (2*i) + 1;
    int r = (2*i) + 2;
    int largest = i;
    if(l<n && arr[l] > arr[i]){
        largest = l;
    }
    if(r<n && arr[r] > arr[largest]){
        largest = r;
    }
    if(largest != i){
        swap(arr[i] , arr[largest]);
        maxHeapify(arr , largest , n);
    }
}
void modifyMintoMax(int a[], int n){
  	for (int i = (n-2)/2; i >= 0; --i)
    {
        maxHeapify(a , i , n);
    }
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# c3

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7eca9bd287a634f85366b2")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

int isMaxHeap(int array[], int n){
  for (int i = 0; i <= (n-2)/2; i++)
  {
      if(array[2*i+1] >  array[i]){
          return false;
      }
      if(2*i+2 < n && array[2*i+2] > array[i]){
        return false;
      }
  }
  return true;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# c4

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7ecaecd287a634f85366b5")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

int connectCost(int lengths[], int n){
  priority_queue<int ,vector<int> , greater<int>> pq;
  for (int i = 0; i < n; i++)
  {
    pq.push(lengths[i]);
  }
  int sum = 0;
  while (pq.size() != 1)
  {
    int x =  pq.top();
    pq.pop();
    int y =  pq.top();
    pq.pop();
    sum += (x+y);
    pq.push(x+y);
  }
	return sum;	
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)





#######################Graph############################
###1

driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a7ece1fd287a634f85367fd")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);
driver.execute_script("arguments[0].click();",button[1])
time.sleep(2)


###1
driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a7eced4d287a634f8536807")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);
###1
driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a7ecfd2d287a634f853680d")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);

###1

driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/6086873424ca04b987c99446")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);
driver.execute_script("arguments[0].click();",button[1])
time.sleep(2)

###1
driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/6086713324ca04b987c9940f")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);

# MCQ1
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5c755f719d2de26a8b769243")#link
driver.find_element_by_id("chkOpt3").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# MCQ2
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5c7561679d2de26a8b769245")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# MCQ3
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5c7565239d2de26a8b769266")#link
driver.find_element_by_id("chkOpt4").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# MCQ4
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5c7565989d2de26a8b769267")#link
driver.find_element_by_id("chkOpt1").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# MCQ5
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5c7566099d2de26a8b769268")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# MCQ6
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5c75671b9d2de26a8b769269")#link
driver.find_element_by_id("chkOpt4").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)


###1
driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/60868c7f24ca04b987c9947f")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);

###1
driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/60dc6fa7ccde02f8205964c8")
button = driver.find_elements_by_xpath("//a[text()='run']")
driver.execute_script("arguments[0].click();",button[0])
time.sleep(2);

time.sleep(120)
driver.quit()