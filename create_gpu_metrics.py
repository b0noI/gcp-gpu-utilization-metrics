import os

from google.cloud import monitoring_v3

project_id = (os.environ['GOOGLE_CLOUD_PROJECT'] or
              os.environ['GCLOUD_PROJECT'])
              
class MissingProjectIdError(Exception):
    pass
    
if not project_id:
    raise MissingProjectIdError(
          'Set the environment variable ' +
          'GCLOUD_PROJECT to your Google Cloud Project Id.')
          
GPU_UTILIZATION_METRIC_NAME = "gpu_utilization/{gpu_id}"

client = monitoring_v3.MetricServiceClient()
project_name = client.project_path(project_id)
for gpu_id in range(1, 9):
    descriptor = monitoring_v3.types.MetricDescriptor()
    type = GPU_UTILIZATION_METRIC_NAME.format(gpu_id=gpu_id)
    descriptor.type = 'custom.googleapis.com/{type}'.format(type=type)
    descriptor.metric_kind = (
        monitoring_v3.enums.MetricDescriptor.MetricKind.GAUGE)
    descriptor.value_type = (
        monitoring_v3.enums.MetricDescriptor.ValueType.INT)
    descriptor.description = 'Metric for GPU utilization. Id: {gpu_id}'.format(gpu_id)
    descriptor = client.create_metric_descriptor(project_name, descriptor)
    print('Created {}.'.format(descriptor.name))
