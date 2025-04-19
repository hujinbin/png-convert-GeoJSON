import cv2
import numpy as np
from shapely.geometry import Polygon
import geojson

# 读取PNG图像并转换为灰度图
img = cv2.imread('map.jpg', 0)
print(img)  # 输出图像的形状
print(img.shape)  # 输出图像的形状
# 进行自适应阈值处理，将图像二值化
thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
# 寻找轮廓
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

features = []
for contour in contours:
    contour = contour.squeeze()  # 去除多余维度
    if len(contour) >= 4: 
        epsilon = 0.01 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        approx = approx.squeeze()
        
        # 确保 approx 至少有 4 个点，并且闭合
        if len(approx) >= 3:  # 至少 3 个点 + 1 个闭合点
            if not np.array_equal(approx[0], approx[-1]):
                approx = np.vstack([approx, approx[0]])  # 闭合多边形
            
            polygon = Polygon(approx)
            if polygon.is_valid:  # 检查多边形是否有效
                feature = geojson.Feature(geometry=polygon, properties={})
                features.append(feature)

feature_collection = geojson.FeatureCollection(features)
with open('mapData.json', 'w') as f:
    geojson.dump(feature_collection, f)