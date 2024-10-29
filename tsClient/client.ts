import * as grpc from '@grpc/grpc-js';
import * as protoLoader from '@grpc/proto-loader';
import { CropMonitorClient } from './farm_services';

const PROTO_PATH = './farm_services.proto';

// Load the .proto file
const packageDefinition = protoLoader.loadSync(PROTO_PATH, {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true
});

const protoDescriptor = grpc.loadPackageDefinition(packageDefinition) as any;
const client = new protoDescriptor.CropMonitor(
  'localhost:50051',
  grpc.credentials.createInsecure()
);

// Call the gRPC method
client.GetCropData({ crop_name: 'Wheat' }, (err: any, response: any) => {
  if (err) {
    console.error(err);
  } else {
    console.log('Crop Data:', response);
  }
});
