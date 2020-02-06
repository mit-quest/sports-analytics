from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.models import Sequential, load_model
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional_recurrent import ConvLSTM2D
from keras.layers import Dense, Reshape
from keras.layers.normalization import BatchNormalization

import matplotlib.pyplot as plt
from pathlib import Path
import yaml

from create_dataset import create_test_train


def _setup_results_dir():

    results_dir = Path('./results')
    if not results_dir.is_file():
        results_dir.mkdir(parents=True, exist_ok=True)

    return results_dir


def _plot_results(results_dir, history):

    # Plot training & validation accuracy values
    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.title('Model accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validate'], loc='upper left')
    plt.savefig(results_dir + '/accuracy.png')

    # Plot training & validation loss values
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Model loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validate'], loc='upper left')
    plt.savefig(results_dir + '/loss.png')


def _train_model():

    results_dir = _setup_results_dir()
    best_model_path = results_dir + '/' + dataset_id + '_best_model'

    x_train, y_train, x_test, y_test = test_train

    num_players = y_train.shape[2]
    if num_players == 2:
        loss = 'binary_crossentropy'
    else:
        loss = 'categorical_crossentropy'

    model = _build_model(num_players, x_train.shape[1], x_train.shape[2], 25, (5, 5))

    model.compile(loss=loss, optimizer='adam', metrics=['accuracy'])

    es = EarlyStopping(monitor='val_loss', mode='min', patience=20, verbose=1)
    mcp_save = ModelCheckpoint(best_model_path, save_best_only=True, monitor='val_loss', mode='min', verbose=1)

    # Train the network
    history = model.fit(x_train, y_train, batch_size=400, epochs=500,
                        validation_split=0.4, callbacks=[mcp_save, es])
    _plot_results(results_dir, history)

    # Testing the network
    best_model = load_model(best_model_path)
    score = best_model.evaluate(x_test, y_test, verbose=0)
    print('Test loss:', score[0])
    print('Test accuracy:', score[1])


def _build_model(num_players, n_samples, n_frames, filters, kernel_size):

    model = Sequential()

    # First layer takes as input pose configurations of shape
    # (samples, n_frames, rows, cols, channels)
    # Model outputs a classification of player ID

    model.add(ConvLSTM2D(filters=filters, kernel_size=kernel_size,
                         input_shape=(n_samples, n_frames, 1, 1),
                         padding='same', return_sequences=True))
    model.add(BatchNormalization())

    model.add(ConvLSTM2D(filters=filters, kernel_size=kernel_size,
                         padding='same', return_sequences=True))
    model.add(BatchNormalization())

    model.add(ConvLSTM2D(filters=filters, kernel_size=kernel_size,
                         padding='same', return_sequences=True))
    model.add(BatchNormalization())

    model.add(ConvLSTM2D(filters=filters, kernel_size=kernel_size,
                         padding='same', return_sequences=True))
    model.add(BatchNormalization())

    model.add(ConvLSTM2D(filters=filters, kernel_size=kernel_size,
                         padding='same', return_sequences=False))
    model.add(BatchNormalization())

    model.add(Conv2D(filters=1, kernel_size=kernel_size,
                     activation='sigmoid',
                     padding='same', data_format='channels_last'))

    model.add(Reshape((-1, n_frames)))

    model.add(Dense(units=num_players, activation='softmax'))

    return model


if __name__ == '__main__':

    with Path('../configs/openpose_config.yaml').open('r') as f:
        openpose_config = yaml.safe_load(f)['openpose_config']

    dataset_id = openpose_config["dataset_id"]

    # create test and train sets from keypoints csv
    formatted_csv_path = dataset_id + "_formatted.csv"
    test_train = create_test_train(formatted_csv_path)

    _train_model()
