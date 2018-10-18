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
          
GPU_UTILIZATION_METRIC_NAME = "gpu_utilization"
GPU_MEMORY_UTILIZATION_METRIC_NAME = "gpu_memory_utilization"

client = monitoring_v3.MetricServiceClient()
project_name = client.project_path(project_id)


def add_new_metrics(type, desc):
    descriptor = monitoring_v3.types.MetricDescriptor()
    descriptor.type = 'custom.googleapis.com/{type}'.format(
        type=type)
    descriptor.metric_kind = (
        monitoring_v3.enums.MetricDescriptor.MetricKind.GAUGE)
    descriptor.value_type = (
        monitoring_v3.enums.MetricDescriptor.ValueType.INT64)
    descriptor.description = desc
    descriptor = client.create_metric_descriptor(project_name, descriptor)
    print('Created {}.'.format(descriptor.name))


add_new_metrics(GPU_UTILIZATION_METRIC_NAME, 'Metric for GPU utilization.')
add_new_metrics(GPU_MEMORY_UTILIZATION_METRIC_NAME,
                'Metric for GPU memory utilization.')
