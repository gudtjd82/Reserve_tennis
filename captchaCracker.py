import glob
import CaptchaCracker as cc
import os

#이미지 학습
def learn_img():
    img_path_list = glob.glob('./captchaCrack/imgs/training_set_1/labeled/*.png')#학습 데이터 이미지 경로 (파일명이 숫자와 같아야함)
    img_width = 236 #이미지 넓이
    img_height = 88 #이미지 높이
    CM = cc.CreateModel(img_path_list, img_width, img_height)   #학습모델 생성
    model = CM.train_model(epochs=100)  #반복 학습 시작
    model.save_weights('./captchaCrack/weights.h5')    #학습 결과 가중치 저장


#가중치로 결과 도출
def result_img(target_path):
    # target_img_path = './captchaCrack/target/target.png'    #타켓 이미지 경로
    target_img_path = target_path    #타켓 이미지 경로
    img_width = 236 #타켓 이미지 넓이
    img_height = 88 #타켓 이미지 높이
    img_length = 6  #타켓 이미지가 포함한 문자 수
    img_char = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}   #타켓 이미지안에 포함된 문자들
    weights_path = './captchaCrack/weights.h5' #학습 결과 가중치 경로
    AM = cc.ApplyModel(weights_path, img_width, img_height, img_length, img_char)   #결과 가중치를 가지는 모델 생성
    pred = AM.predict(target_img_path)  #결과 도출
    return pred

def evaluste_accuracy(target_dir):
    correct = 0;
    incorrections = []

    files = os.listdir(target_dir)

    target_files = [file for file in files if file.endswith('.png')]
    total_datas = len(target_files)

    for target in target_files:
        target_path = os.path.join(target_dir, target)
        pred = result_img(target_path)

        answer = target.replace('.png', '')
        print(f"Prediction: {pred}, Answer: {answer}")

        if pred == answer:
            correct += 1
        else:
            incorrections.append((answer, pred))
    print(f"Corrections: {correct} of {total_datas}")
    return float((correct/total_datas) *100), incorrections

# learn_img() #최초 가중치 생성을 위한 학습시 주석해제

# target_dir = './captchaCrack/imgs/test_set_1/labeled/'
# accuracy, incorrections = evaluste_accuracy(target_dir)
# print(f"Accuracy: {accuracy} %")
# print("============Incorrections============")
# for incorr in incorrections:
#     print(incorr)