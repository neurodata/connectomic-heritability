# Obtaining the data

The connectomes used in this analysis is freely available in AWS S3 bucket [Open Neurodata](https://registry.opendata.aws/open-neurodata/). The python script `download_hcp.py` included in this `data` folder will automatically download all available processed connectomes from the AWS data exchange.

To run the script, make sure your working directory is either in the root project `connectomic-heritability` or in `data` subfolder within the project. After installing all the necessary packages and setting up your environment, simply run:

```
python download_hcp.py
```

and it will automatically populate the `data` folder.
