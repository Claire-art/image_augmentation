이미지 증강 코드
<br/>
<br/>
**아래 코드에 적용 가능한 기법**

```python
def augment_and_save_image(image):
    seq = iaa.Sequential([
        iaa.Flipud(0.5),
        iaa.Affine(rotate=(-45, 45)),
        iaa.AdditiveGaussianNoise(scale=(0, 0.1*255)),  # 가우시안 노이즈
        iaa.SaltAndPepper(0.02)  # 소금-후추 노이즈      
        # 원하는 증강 기법 추가
    ])
```


<br/>

**이동 (Translate):** 이미지를 수평 또는 수직으로 이동시키는 기법
```python
iaa.Affine(translate_percent={"x": (-0.2, 0.2), "y": (-0.2, 0.2)})
```
<br/>

**확대/축소 (Scale):** 이미지를 확대하거나 축소시키는 기법
```python
iaa.Affine(scale=(0.5, 1.5))
```
<br/>

**회전 (Rotate):** 이미지를 회전시키는 기법
```python
iaa.Affine(rotate=(-45, 45))
```
<br/>

**좌우 반전 (Flip):** 이미지를 좌우로 반전시키는 기법
```python
iaa.Fliplr(0.5)
```
<br/>

**상하 반전 (Flip):** 이미지를 상하로 반전시키는 기법
```python
iaa.Flipud(0.5)
```
<br/>

**가우시안 노이즈 (Gaussian Noise):** 이미지에 가우시안 분포에 따른 노이즈를 추가
```python
iaa.AdditiveGaussianNoise(scale=(0, 0.1*255))
```
<br/>

**솔트-후추 노이즈 (Salt-and-Pepper Noise):** 이미지에 임의의 픽셀을 흰색 또는 검은색으로 변경하여 노이즈를 추가
```python
iaa.SaltAndPepper(0.02)
```
<br/>

**모션 블러 (Motion Blur):** 이미지에 모션 블러 효과를 추가
```python
iaa.MotionBlur(k=15)
```
<br/>

**콘트라스트 조정 (Contrast Adjustment):** 이미지의 콘트라스트를 조절
```python
iaa.contrast.LinearContrast(alpha=(0.5, 2.0))
```

<br/>

**색상 변환 (Color Transformation):** 이미지의 색상을 변환
```python
iaa.Sequential([
    iaa.ChangeColorspace(from_colorspace="RGB", to_colorspace="HSV"),
    iaa.WithChannels(0, iaa.Add((10, 50))),
    iaa.ChangeColorspace(from_colorspace="HSV", to_colorspace="RGB")
])
```
