import grpc
import farm_services_pb2
import farm_services_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        # CropMonitor service
        crop_stub = farm_services_pb2_grpc.CropMonitorStub(channel)
        moisture_response = crop_stub.GetMoistureLevel(farm_services_pb2.CropRequest(crop_id="corn_field_1"))
        print(f"Moisture level: {moisture_response.moisture_level:.2f}%")

        # WeatherStation service
        weather_stub = farm_services_pb2_grpc.WeatherStationStub(channel)
        forecast_response = weather_stub.GetWeatherForecast(farm_services_pb2.ForecastRequest(date="2023-06-01"))
        print(f"Weather forecast:")
        print(f"  Temperature: {forecast_response.temperature:.1f}°C")
        print(f"  Humidity: {forecast_response.humidity:.1f}%")
        print(f"  Conditions: {forecast_response.conditions}")

if __name__ == '__main__':
    run()