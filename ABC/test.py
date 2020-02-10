from keras.layers import Conv2D, Input
from keras.models import Model
import numpy as np

def normal_conv_two():
    input = Input((3,3,2))
    layer = Conv2D(3, kernel_size=3, use_bias=False) # 計算を簡単にするためにバイアス項を抜く
    x = layer(input)
    model = Model(input, x)

    weights = layer.get_weights()
    print(weights)
    print(weights[0].shape)#(3,3,2,3) 末尾がフィルター数

    # weights = np.arange(1, 55).reshape(3,3,2,3).astype(np.float32)
    weights = np.arange(1, 55).reshape(3, 3, 2, 3).astype(np.float32)
    layer.set_weights([weights])

    print("weights")
    print(weights[:,:,0,0])
    print(weights[:,:,0,1])
    print(weights[:,:,0,2])
    print(weights[:,:,1,0])
    print(weights[:,:,1,1])
    print(weights[:,:,1,2])
    X = np.arange(1, 19).reshape(1,3,3,2) * 0.1
    print("input")
    print(X[0,:,:,0])
    print(X[0,:,:,1])
    result = model.predict(X)
    print("output")
    # print(result[0,:,:,0]) # weights[:,:,0,0]*X[0,:,:,0] + weights[:,:,1,0]*X[0,:,:,1]
    # print(result[0,:,:,1]) # weights[:,:,0,1]*X[0,:,:,0] + weights[:,:,1,1]*X[0,:,:,1]
    # print(result[0,:,:,2]) # weights[:,:,0,2]*X[0,:,:,0] + weights[:,:,1,2]*X[0,:,:,1]
    print(result)

if __name__ == "__main__":
    normal_conv_two()