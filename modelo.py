import tensorflow as tf 
def model_fun():
    model = tf.keras.models.load_model('./models/conv_MLP_84.h5')
    return model