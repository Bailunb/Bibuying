import tensorflow as tf
from read_utils import TextConverter
from model import CharRNN
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from IPython import embed

FLAGS = tf.flags.FLAGS

tf.flags.DEFINE_integer('lstm_size', 128, 'size of hidden state of lstm')
tf.flags.DEFINE_integer('num_layers', 3, 'number of lstm layers')
tf.flags.DEFINE_boolean('use_embedding', True, 'whether to use embedding')
tf.flags.DEFINE_integer('embedding_size', 128, 'size of embedding')
tf.flags.DEFINE_string('converter_path', 'model/0/converter.pkl', 'model/name/converter.pkl')#gai1
tf.flags.DEFINE_string('checkpoint_path', 'model/0', 'checkpoint path')#gai2
tf.flags.DEFINE_string('start_string', '大街', 'use this string to start generating')
tf.flags.DEFINE_integer('max_length', 500, 'max length to generate')


def main(_,catalog, word):
    checkpoint_path='model/%d'%(catalog)
    FLAGS.start_string = FLAGS.start_string.encode('utf-8').decode('utf-8')
    converter = TextConverter(filename=FLAGS.converter_path)
    if os.path.isdir(FLAGS.checkpoint_path):
        FLAGS.checkpoint_path =\
            tf.train.latest_checkpoint(FLAGS.checkpoint_path)

    model = CharRNN(converter.vocab_size, sampling=True,
                    lstm_size=FLAGS.lstm_size, num_layers=FLAGS.num_layers,
                    use_embedding=FLAGS.use_embedding,
                    embedding_size=FLAGS.embedding_size)

    model.load(FLAGS.checkpoint_path)

    start = converter.text_to_arr(FLAGS.start_string)
    arr = model.sample(FLAGS.max_length, start, converter.vocab_size)
    print(converter.arr_to_text(arr))


def write_song(catalog=0, word=''):
    song_script = open('sample.txt', encoding='utf-8').read().split('\n')
    return song_script


if __name__ == '__main__':
    tf.app.run()
    # write_song()
