# -*- coding: utf-8 -*-

from __future__ import print_function

from evaluate import infer
from DB import Database

from color import Color
from daisy import Daisy
from edge  import Edge
from gabor import Gabor
from HOG   import HOG
from vggnet import VGGNetFeat
from resnet import ResNetFeat

depth = 5
d_type = 'cosine'
query_path = "/content/macaron.jpg"

if __name__ == '__main__':

  db = Database()
  # retrieve by color
  print("Color")
  method = Color()
  samples = method.make_samples(db)
  query = method.make_query(query_path)
  print(query['img'])
  result = infer(query, samples=samples, depth=depth, d_type=d_type)
  for ele in result:
    print(ele)

  # retrieve by daisy
  #method = Daisy()
  #samples = method.make_samples(db)
  #query = samples[query_idx]
  #_, result = infer(query, samples=samples, depth=depth, d_type=d_type)
  #print(result)

  # retrieve by edge
  #method = Edge()
  #samples = method.make_samples(db)
  #query = samples[query_idx]
  #_, result = infer(query, samples=samples, depth=depth, d_type=d_type)
  #print(result)

  # retrieve by gabor
  #method = Gabor()
  #samples = method.make_samples(db)
  #query = samples[query_idx]
  #_, result = infer(query, samples=samples, depth=depth, d_type=d_type)
  #print(result)

  # retrieve by HOG
  #method = HOG()
  #samples = method.make_samples(db)
  #query = samples[query_idx]
  #_, result = infer(query, samples=samples, depth=depth, d_type=d_type)
  #print(result)

  # retrieve by VGG
  print("VGG")
  method = VGGNetFeat()
  samples = method.make_samples(db)
  query = method.make_query(query_path)
  print(query['img'])
  result = infer(query, samples=samples, depth=depth, d_type=d_type)
  for ele in result:
    print(ele)


  # retrieve by resnet
  print("Resnet")
  method = ResNetFeat()
  samples = method.make_samples(db)
  query = method.make_query(query_path)
  print(query['img'])
  result = infer(query, samples=samples, depth=depth, d_type=d_type)
  for ele in result:
    print(ele)
