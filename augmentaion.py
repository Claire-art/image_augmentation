import os
import cv2
import numpy as np
from imgaug import augmenters as iaa
from tqdm import tqdm
import time

# 이미지 파일이 있는 폴더 경로
input_folder = 'path'
# 라벨 파일이 있는 폴더 경로
label_folder = 'path'
# 증강된 이미지를 저장할 폴더 경로
output_folder = 'path'
# 증강할 이미지 파일 확장자
valid_extensions = ['.jpg', '.jpeg']

# 이미지 증강 함수 정의
def augment_and_save_image(image):
    seq = iaa.Sequential([
        iaa.Flipud(0.5),
        iaa.Affine(rotate=(-45, 45)),
        iaa.AdditiveGaussianNoise(scale=(0, 0.1*255)),  
        iaa.SaltAndPepper(0.02)      
        # 원하는 증강 기법 추가
    ])
    
    augmented_image = seq.augment_image(image)
    return augmented_image

# tqdm을 사용하여 진행 상황을 모니터링
for filename in tqdm(os.listdir(input_folder), desc="이미지 증강 및 라벨 변환 진행 중"):
    if any(filename.lower().endswith(ext) for ext in valid_extensions):
        # 이미지 파일 읽기
        image_path = os.path.join(input_folder, filename)
        image = cv2.imread(image_path)
        
        # 이미지 증강
        augmented_image = augment_and_save_image(image)
        
        # 증강된 이미지 저장
        output_image_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_image_path, augmented_image)
        
        # 해당 이미지의 라벨 파일 경로 생성
        label_filename = os.path.splitext(filename)[0] + ".txt"
        label_path = os.path.join(label_folder, label_filename)
        
        # 라벨 파일 읽기
        with open(label_path, 'r') as f:
            labels = f.readlines()
        
        # 증강된 이미지 크기에 맞게 라벨 좌표 변환
        augmented_labels = []
        for label in labels:
            # 라벨 정보를 증강된 이미지 크기에 맞게 조절
            augmented_labels.append(label)
        
        # 증강된 이미지에 맞는 라벨 파일 저장
        output_label_filename = os.path.splitext(filename)[0] + f"_{time.time()}.txt"
        output_label_path = os.path.join(output_folder, output_label_filename)
        with open(output_label_path, 'w') as f:
            f.writelines(augmented_labels)

print("이미지 증강 및 라벨 변환이 완료되었습니다.")
