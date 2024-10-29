import grpc
from concurrent import futures
import farm_services_pb2
import farm_services_pb2_grpc
import random

class CropMonitor(farm_services_pb2_grpc.CropMonitorServicer):
    def GetMoistureLevel(self, request, context):
        # In a real scenario, this would fetch data from actual sensors
        moisture = random.uniform(0, 100)
        return farm_services_pb2.MoistureResponse(moisture_level=moisture)

class WeatherStation(farm_services_pb2_grpc.WeatherStationServicer):
    def GetWeatherForecast(self, request, context):
        # In a real scenario, this would fetch data from a weather API
        temperature = random.uniform(0, 35)
        humidity = random.uniform(30, 100)
        conditions = random.choice(["Sunny", "Cloudy", "Rainy"])
        return farm_services_pb2.ForecastResponse(
            temperature=temperature,
            humidity=humidity,
            conditions=conditions
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    farm_services_pb2_grpc.add_CropMonitorServicer_to_server(CropMonitor(), server)
    farm_services_pb2_grpc.add_WeatherStationServicer_to_server(WeatherStation(), server)
    server.add_insecure_port('[::]:50051')
    print("Farm Tech Server starting on port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()