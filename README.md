# Pattern Recognition
## pr_hw5_label.py
Split data to training and validation (80%:20%)

## pr_hw5_LeNet.py
Implement LeNet. Using ImageDataGenerator for data increasement.

## result.log
Ouput value of acc, loss, val_acc, val_loss.
## training_log.log
    Using Theano backend.
    Found 2262 images belonging to 80 classes.
    Found 589 images belonging to 80 classes.
    Epoch 1/32
    2262/2262 [==============================] - 6s - loss: 2.6841 - acc: 0.3501 - val_loss: 1.6604 - val_acc: 0.5739
    Epoch 2/32
    2262/2262 [==============================] - 6s - loss: 1.4127 - acc: 0.6269 - val_loss: 1.1472 - val_acc: 0.6927
    Epoch 3/32
    2262/2262 [==============================] - 5s - loss: 1.0151 - acc: 0.7184 - val_loss: 0.9587 - val_acc: 0.7674
    Epoch 4/32
    2262/2262 [==============================] - 5s - loss: 0.8085 - acc: 0.7719 - val_loss: 0.7824 - val_acc: 0.7895
    Epoch 5/32
    2262/2262 [==============================] - 5s - loss: 0.6973 - acc: 0.7975 - val_loss: 0.8557 - val_acc: 0.8132
    Epoch 6/32
    2262/2262 [==============================] - 6s - loss: 0.5814 - acc: 0.8280 - val_loss: 0.7764 - val_acc: 0.8234
    Epoch 7/32
    2262/2262 [==============================] - 6s - loss: 0.5229 - acc: 0.8400 - val_loss: 0.7075 - val_acc: 0.8285
    Epoch 8/32
    2262/2262 [==============================] - 6s - loss: 0.4445 - acc: 0.8740 - val_loss: 0.5437 - val_acc: 0.8421
    Epoch 9/32
    2262/2262 [==============================] - 5s - loss: 0.3952 - acc: 0.8851 - val_loss: 0.6255 - val_acc: 0.8676
    Epoch 10/32
    2262/2262 [==============================] - 5s - loss: 0.3848 - acc: 0.8811 - val_loss: 0.5763 - val_acc: 0.8591
    Epoch 11/32
    2262/2262 [==============================] - 5s - loss: 0.3058 - acc: 0.9010 - val_loss: 0.5547 - val_acc: 0.8744
    Epoch 12/32
    2262/2262 [==============================] - 5s - loss: 0.3172 - acc: 0.9063 - val_loss: 0.5933 - val_acc: 0.8744
    Epoch 13/32
    2262/2262 [==============================] - 5s - loss: 0.2779 - acc: 0.9138 - val_loss: 0.3460 - val_acc: 0.9219
    Epoch 14/32
    2262/2262 [==============================] - 5s - loss: 0.3166 - acc: 0.9063 - val_loss: 0.5360 - val_acc: 0.8812
    Epoch 15/32
    2262/2262 [==============================] - 5s - loss: 0.2643 - acc: 0.9120 - val_loss: 0.5125 - val_acc: 0.8930
    Epoch 16/32
    2262/2262 [==============================] - 5s - loss: 0.2216 - acc: 0.9302 - val_loss: 0.5976 - val_acc: 0.8778
    Epoch 17/32
    2262/2262 [==============================] - 5s - loss: 0.2429 - acc: 0.9244 - val_loss: 0.4773 - val_acc: 0.8812
    Epoch 18/32
    2262/2262 [==============================] - 5s - loss: 0.2016 - acc: 0.9332 - val_loss: 0.4441 - val_acc: 0.9151
    Epoch 19/32
    2262/2262 [==============================] - 5s - loss: 0.2070 - acc: 0.9350 - val_loss: 0.4689 - val_acc: 0.8862
    Epoch 20/32
    2262/2262 [==============================] - 5s - loss: 0.2079 - acc: 0.9302 - val_loss: 0.5013 - val_acc: 0.8795
    Epoch 21/32
    2262/2262 [==============================] - 5s - loss: 0.1856 - acc: 0.9341 - val_loss: 0.5784 - val_acc: 0.8761
    Epoch 22/32
    2262/2262 [==============================] - 5s - loss: 0.1866 - acc: 0.9390 - val_loss: 0.4850 - val_acc: 0.8913
    Epoch 23/32
    2262/2262 [==============================] - 5s - loss: 0.1877 - acc: 0.9434 - val_loss: 0.4759 - val_acc: 0.8998
    Epoch 24/32
    2262/2262 [==============================] - 5s - loss: 0.1563 - acc: 0.9456 - val_loss: 0.6445 - val_acc: 0.8659
    Epoch 25/32
    2262/2262 [==============================] - 5s - loss: 0.1705 - acc: 0.9492 - val_loss: 0.4443 - val_acc: 0.9117
    Epoch 26/32
    2262/2262 [==============================] - 5s - loss: 0.1557 - acc: 0.9478 - val_loss: 0.5921 - val_acc: 0.9032
    Epoch 27/32
    2262/2262 [==============================] - 5s - loss: 0.1619 - acc: 0.9474 - val_loss: 0.4172 - val_acc: 0.9100
    Epoch 28/32
    2262/2262 [==============================] - 5s - loss: 0.1236 - acc: 0.9527 - val_loss: 0.4204 - val_acc: 0.9304
    Epoch 29/32
    2262/2262 [==============================] - 5s - loss: 0.1410 - acc: 0.9531 - val_loss: 0.4320 - val_acc: 0.9083
    Epoch 30/32
    2262/2262 [==============================] - 5s - loss: 0.1538 - acc: 0.9478 - val_loss: 0.4387 - val_acc: 0.9219
    Epoch 31/32
    2262/2262 [==============================] - 5s - loss: 0.1571 - acc: 0.9505 - val_loss: 0.3499 - val_acc: 0.9304
    Epoch 32/32
    2262/2262 [==============================] - 5s - loss: 0.1466 - acc: 0.9545 - val_loss: 0.4368 - val_acc: 0.9015
