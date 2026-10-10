import numpy as np
## import... 安装所需要的依赖库
def a1(t):
    return t[0]
def loo_eval(X, y, k):
    # 这部分为实验的核心代码
    right=0
    l=[]
    for i in range(1593):
        l.clear()
        ans=-1
        id=0
        num=[0,0,0,0,0,0,0,0,0,0]
        for j in range(1593):
            if j!=i:
                l.append([np.sqrt(np.sum(np.square(X[i]-X[j]))),y[j]])
        l=sorted(l, key=a1)
        for j in range(k):
            num[l[j][1]]+=1
        for j in range(10):
            if num[j]>=ans:
                ans=num[j]
                id=j
        if id==y[i]:
            right+=1
    acc=right/1593
    return acc

# 主流程
raw = np.loadtxt('semeion.data')
X, y = raw[:, :256], np.argmax(raw[:, 256:], 1)

for k in [1, 3, 5]:
    acc = loo_eval(X, y, k)
    print(f'k={k}  LOO 准确率 = {acc:.4f}')
