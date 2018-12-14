import tensorflow as tf

from .config import (
    MAX_LEN,
)

def build_model (
    voc_size: int,
) -> tf.keras.models.Sequential:

    model = tf.keras.models.Sequential()
    model.add(
        tf.keras.layers.Embedding(
            input_dim=voc_size,
            output_dim=64,
            input_length=MAX_LEN,
        )
    )
    model.add(
        tf.keras.layers.Bidirectional(
            tf.keras.layers.LSTM(
                units=64,
                # activation='sigmoid',
                # inner_activation='hard_sigmoid',
                return_sequences=True,
            )
        )
    )
    model.add(tf.keras.layers.Dropout(0.2))
    model.add(
        tf.keras.layers.TimeDistributed(
            tf.keras.layers.Dense(
                1,
                activation='sigmoid'
            )
        )
    )

    model.compile(loss='binary_crossentropy', optimizer='adam')

    return model
