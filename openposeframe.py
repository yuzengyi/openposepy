import json
import numpy as np


def read_json_file(i, folder="output_jsons"):
    # 使用字符串格式化来生成文件名
    filename = f"{folder}/video_{i:012d}_keypoints.json"
    # 读取文件内容并返回
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
def openpose_i_j(i,j):
    data = read_json_file(i)
    if j < len(data["people"]):  # 仅处理第j个人的数据
        person = data["people"][j]
        pose_keypoints_2d = person['pose_keypoints_2d']
    else:
        pose_keypoints_2d = [-1] * 75
    # 从JSON数据中提取关键点数据
    keypoints = pose_keypoints_2d[:75]  # 只保留前75个值
    # 将关键点数据重塑为25行3列的矩阵
    keypoints_matrix = np.reshape(keypoints, (25, 3))
    return keypoints_matrix