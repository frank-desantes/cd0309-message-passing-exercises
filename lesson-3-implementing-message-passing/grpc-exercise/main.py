import time
from concurrent import futures

import grpc
import order_pb2
import order_pb2_grpc


class OrderServicer(order_pb2_grpc.OrderServiceServicer):
    def Get(self, request, context):

        request_value_1 = order_pb2.OrderMessage(
            id="123",
            created_by="user123",
            status= order_pb2.OrderMessage.Status.QUEUED,
            created_at="18.3.2025 16:10:02",
            equipment= [order_pb2.OrderMessage.Equipment.KEYBOARD, order_pb2.OrderMessage.Equipment.MONITOR]
        )
        
        request_value_2 = order_pb2.OrderMessage(
            id="345",
            created_by="user345",
            status=order_pb2.OrderMessage.Status.COMPLETED,
            created_at="18.3.2025 16:10:02",
            equipment=[order_pb2.OrderMessage.Equipment.KEYBOARD, order_pb2.OrderMessage.Equipment.MONITOR]
        )

        #print(request_value_1)

        result =order_pb2.OrderMessageList()
        result.orders.extend([request_value_1, request_value_2])
        return result

    def Create(self, request, context):

        request_value = {
            "id": request.id,
            "created_by": request.created_by ,
            "status": request.status,
            "created_at": request.created_at,
            "equipment": ["KEYBOARD", "MONITOR"]
        }

        print(request_value)

        return order_pb2.OrderMessage(**request_value)


# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
order_pb2_grpc.add_OrderServiceServicer_to_server(OrderServicer(), server)


print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
