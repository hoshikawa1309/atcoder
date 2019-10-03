#ノードクラスの定義
class Node:
    def __init__(self, data): #コンストラクタ
        self.data = data #ノードがもつ数値
        self.left = None #左エッジ
        self.right = None #右エッジ

if __name__ == '__main__':
    
