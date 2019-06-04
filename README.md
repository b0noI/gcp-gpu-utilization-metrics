# How To Use It

This repository provides simple way to monitor GPU utilization on GCP

It is very simple to use, just run agent on each of your instance:

```bash
git clone https://github.com/b0noI/gcp-gpu-utilization-metrics.git
cd gcp-gpu-utilization-metrics
pip install -r ./requirenments.txt
python ./report_gpu_metrics.py &
```

This will auto create the metrics. But if you need to create metrics first run the following commands:

```bash
git clone https://github.com/b0noI/gcp-gpu-utilization-metrics.git
cd gcp-gpu-utilization-metrics
pip install -r ./requirenments.txt
GOOGLE_CLOUD_PROJECT=<ID> python ./create_gpu_metrics.py
```


## Customizing the reporting frequency

By default, this agent reports the metrics every 5 seconds.
If you want to customize the frequency of reporting, you can do so with the --freq option while executing the agent as follows:

```bash
python ./report_gpu_metrics.py --freq=10s &
```

If you want to specify the frequency in minutes or hours, use 'm' or 'h' at the end.

```bash
python ./report_gpu_metrics.py --freq=10m &  #frequency in minutes

python ./report_gpu_metrics.py --freq=10h &  #frequency in hours

python ./report_gpu_metrics.py --freq=10 &   #if none amongst 's', 'm', or 'h' is specified,
					     #it is considered in seconds, by default
```

