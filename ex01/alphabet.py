import random
import datetime

alphabet = 26
target_st = 7
defect_st = 2
challenge = 2

def shutudai(AtoZ):
    quiz = random.sample(AtoZ,target_st)
    print("対象文字：")
    for c in sorted(quiz):
        print(c,end=" ")
    print()
    defect = random.sample(quiz,defect_st)
    print("表示文字：")
    for c in quiz:
        if c not in defect:
            print(c,end=" ")
    print()
    print("デバッグ用欠損文字：", defect)
    return defect_st

def kaito(seikai):
    num = int(input("欠損文字はいくつあるでしょうか？："))
    if num != defect_st:
        print("不正解です。")
    else:
        print("正解です。それでは、具体的に欠損文字を１つづつ入力してください")
        for i in range(num):
            c = input(f"{i+1}つ目の文字を入力してください：")
            #型がおかしいので要検討
            if c not in seikai:
                print("不正解です。またチャレンジしてください。")
                return False
            else:
                seikai.remove(c)
        else:
            print("欠損文字も含めて完全正解です。")
            return True
    return False


            


if __name__ == "__main__":
    AtoZ = [chr(i+65) for i in range(alphabet)]
    st = datetime.datetime.now()
    for a in range(challenge):
        defect = shutudai(AtoZ)
        ret = kaito(defect)
        if ret:
            break
        else :
            print("-"*20)
    ed = datetime.datetime.now()
    print(f"所要時間:{(ed-st).seconds}秒")
    