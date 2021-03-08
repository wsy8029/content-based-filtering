from __future__ import print_function

import grpc

import recommend_pb2
import recommend_pb2_grpc


def run(id):
    channel = grpc.insecure_channel('localhost:50051')
    stub = recommend_pb2_grpc.RecommenderStub(channel)
    # response = stub.GetRecommend(recommend_pb2.UserInfo(name='you'))
    response = stub.GetRecommend(recommend_pb2.UserInfo(name=str(id))) #처음 .proto에 reque로st를 str 형식의 name으로 설정
    print("Recommended movie ID: " + response.message)

if __name__ == '__main__':
    # run(239)
    while True:
        id = input("User ID: ")
        run(id)
