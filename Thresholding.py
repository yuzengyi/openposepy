import numpy as np
from sklearn.cluster import KMeans
def Kmeans_threshold(c):
    # 使数据为二维
    confidences_reshape = np.array(c).reshape(-1, 1)
    # 使用KMeans进行聚类，假设我们想要分为两类
    kmeans = KMeans(n_clusters=2, random_state=0).fit(confidences_reshape)
    # 找到阈值（两个聚类中心的平均值）
    threshold = np.mean(kmeans.cluster_centers_)
    return threshold