import random

def shutudai(quiz_list):
    n = random.choice(quiz_list)
    print("問題:" + n["quiz"])
    return n["answer"]

def kaito(ans_list):
    ans = input("解答：")
    if ans in ans_list:
        print("正解！！")
    else:
        print("不正解")

if __name__ == "__main__":
    quiz_list = [{"quiz":"サザエの旦那の名前は？","answer":["マスオ","ますお", "ますおさん","マスオさん"]},
            {"quiz":"カツオの妹の名前は？","answer":["ワカメ","わかめ","わかめちゃん"]},
            {"quiz":"タラオはカツオから見てどんな関係？","answer":["甥","おい", "甥っ子", "おいっこ"]}]

    ans_list = shutudai(quiz_list)
    kaito(ans_list)
    
