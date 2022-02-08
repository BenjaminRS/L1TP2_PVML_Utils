import argparse
import tensorflow as tf

parser = argparse.ArgumentParser(description='Prints the shapes of TensorFlow Networks')
parser.add_argument('--i',help='Input Filename',required=True)
args = parser.parse_args()

def load_pb(path_to_pb):
  with tf.io.gfile.GFile(path_to_pb, 'rb') as f:
    graph_def = tf.compat.v1.GraphDef()
    graph_def.ParseFromString(f.read())
  with tf.Graph().as_default() as graph:
    tf.import_graph_def(graph_def, name='')
    return graph

tf_graph = load_pb(args.i)

for op in tf_graph.get_operations():
  print(op.values())
