import openai
import os

# 设置 API key 和 API base URL
# api_key = ""
# base_url = "https://api.nextapi.fun/v1"

api_key = "ak-PwFIRVCzKdlXP8DlbubRJEJaqwclps3yacyR9Qs5KxYihpoJ"
api_base = "https://api.nextapi.fun/v1"


client = openai.OpenAI(
    api_key=api_key,
    base_url=api_base,
)



system_msg = "You are a software testing assistant. " \
             "Please help me generate a whole JUnit test for the methods of the project under test. " \
             "I will provide the source code under test, including required dependencies to import. " \
             "I need you to create a whole unit test using JUnit 4, ensuring optimal branch coverage. " \
             "The test should include necessary imports for JUnit 4, compile without errors, " \
             "and use reflection to invoke private methods, preferably with necessary comments."

user_msg = "I am giving you the source code."

message = [{
    "role": "system", "content": system_msg,
    # "role": "user", "content": user_msg,
}]

number_to_word = {
    1: 'first',
    2: 'second',
    3: 'third',
    4: 'forth',
    5: 'fifth',
    6: 'sixth',
    7: 'seventh',
    8: 'eighth',
    9: 'ninth'
}


def generate_test(system_message, user_message, project_path):

    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": "你好\n你是谁？",
            }
        ],
    )
    print(chat_completion.choices[0].message.content)


if __name__ == '__main__':
    project_path = r"C:\YGL\科研\博士\论文\ChatGPT用例生成\往年全国大赛试题\2021\2021-3\2021总决赛\AVLTree_1637204418221\AVLTree"
    source_code_path = project_path + '/' + 'src/main/java/net/mooctest'
    # print(source_code_path)
    source_code_list = os.listdir(source_code_path)
    # print(source_code_list[0])
    # 将所有源代码发送给GPT
    # for i in range(len(source_code_list)):
    # with open(source_code_path + '/' + source_code_list[i], "r") as f:
    #     source_code = f.read()
    content = """package net.mooctest;

public class BigNumber {
    public static String bigNumberSimpleMulti(String f, String s) {  
        System.out.print("multi : \n" + f + "*" + s + "=");  
        char signA = f.charAt(0);  
        char signB = s.charAt(0);  
        char sign = '+';  
        if (signA == '+' || signA == '-') {  
            sign = signA;  
            f = f.substring(1);  
        }  
        if (signB == '+' || signB == '-') {  
            if (sign == signB) {  
                sign = '+';  
            } else {  
                sign = '-';  
            }  
            s = s.substring(1);  
        }  
        char[] a = new StringBuffer(f).reverse().toString().toCharArray();  
        char[] b = new StringBuffer(s).reverse().toString().toCharArray();  
        int lenA = a.length;  
        int lenB = b.length;  
        int len = lenA + lenB;  
        int[] result = new int[len];  
        for (int i = 0; i < a.length; i++) {  
            for (int j = 0; j < b.length; j++) {  
                result[i + j] += (int) (a[i] - '0') * (int) (b[j] - '0');  
            }  
        }  
        for (int i = 0; i < result.length; i++) {  
            if (result[i] > 10) {  
                result[i + 1] += result[i] / 10;  
                result[i] %= 10;  
            }  
        }  
        StringBuffer sb = new StringBuffer();  
        boolean flag = true;  
        for (int i = len - 1; i >= 0; i--) {  
            if (result[i] == 0 && flag) {  
                continue;  
            } else {  
                flag = false;  
            }  
            sb.append(result[i]);  
        }  
        if (!sb.toString().equals("")) {  
            if (sign == '-') {  
                sb.insert(0, sign);  
            }  
        } else {  
            sb.append(0);  
        }  
        System.out.println(sb.toString());  
        return sb.toString();
    }  
    
    public static String bigNumberAdd(String f, String s) {  
    	System.out.print("add : \n" + f + "+" + s + "=");  
        char[] a = new StringBuffer(f).reverse().toString().toCharArray();  
        char[] b = new StringBuffer(s).reverse().toString().toCharArray();  
        int lenA = a.length;  
        int lenB = b.length;  
        int len = lenA > lenB ? lenA : lenB;  
        int[] result = new int[len + 1];  
        for (int i = 0; i < len + 1; i++) {  
            int aint = i < lenA ? (a[i] - '0') : 0;  
            int bint = i < lenB ? (b[i] - '0') : 0;  
            result[i] = aint + bint;  
        }  
        for (int i = 0; i < result.length; i++) {  
            if (result[i] > 10) {  
                result[i + 1] += result[i] / 10;  
                result[i] %= 10;  
            }  
        }  
        StringBuffer sb = new StringBuffer();  
        boolean flag = true;  
        for (int i = len; i >= 0; i--) {  
            if (result[i] == 0 && flag) {  
                continue;  
            } else {  
                flag = false;  
            }  
            sb.append(result[i]);  
        }  
        System.out.println(sb.toString());  
        return sb.toString();  
    }  
    
    public static String bigNumberSub(String f, String s) {  
        System.out.print("sub : \n" + f + "-" + s + "=");  
        char[] a = new StringBuffer(f).reverse().toString().toCharArray();  
        char[] b = new StringBuffer(s).reverse().toString().toCharArray();  
        int lenA = a.length;  
        int lenB = b.length;  
        int len = lenA > lenB ? lenA : lenB;  
        int[] result = new int[len];  
        char sign = '+';  
        if (lenA < lenB) {  
            sign = '-';  
        } else if (lenA == lenB) {  
            int i = lenA - 1;  
            while (i > 0 && a[i] == b[i]) {  
                i--;  
            }  
            if (a[i] < b[i]) {  
                sign = '-';  
            }  
        }  
        for (int i = 0; i < len; i++) {  
            int aint = i < lenA ? (a[i] - '0') : 0;  
            int bint = i < lenB ? (b[i] - '0') : 0;  
            if (sign == '+') {  
                result[i] = aint - bint;  
            } else {  
                result[i] = bint - aint;  
            }  
        }  
        for (int i = 0; i < result.length - 1; i++) {  
            if (result[i] < 0) {  
                result[i + 1] -= 1;  
                result[i] += 10;  
            }  
        }  
  
        StringBuffer sb = new StringBuffer();  
        if (sign == '-') {  
            sb.append('-');  
        }  
        boolean flag = true;  
        for (int i = len - 1; i >= 0; i--) {  
            if (result[i] == 0 && flag) {  
                continue;  
            } else {  
                flag = false;  
            }  
            sb.append(result[i]);  
        }  
        if (sb.toString().equals("")) {  
            sb.append("0");  
        }  
        System.out.println(sb.toString());  
        return sb.toString();  
    } 
    
}
"""
    print(f'User: {content}')
    message.append({"role": "user",
                    "content": content})
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=message,
    )
    print(chat_completion.choices[0].message.content)


