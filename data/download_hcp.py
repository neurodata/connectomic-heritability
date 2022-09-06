# %%
from pathlib import Path
import os

import boto3
from botocore import UNSIGNED
from botocore.config import Config


def get_all_subjects(bucket, prefix, client):
    def get_subjects():
        continuation_token = None

        while True:
            list_kwargs = dict(Bucket=bucket, Prefix=prefix, Delimiter="/")
            if continuation_token:
                list_kwargs["ContinuationToken"] = continuation_token
            response = client.list_objects_v2(**list_kwargs)
            yield from response.get("CommonPrefixes", [])
            if not response.get("IsTruncated"):  # At the end of the list?
                break
            continuation_token = response.get("NextContinuationToken")

    # Returns all the 6-digit subject codes in a given bucket
    subject_list = [d["Prefix"].split("/")[1] for d in get_subjects()]

    return subject_list


# %%

# Deals with anonymous login
s3 = boto3.client("s3", config=Config(signature_version=UNSIGNED))

bucket = "open-neurodata"
prefix = "hcp1200/"

subjects = get_all_subjects(bucket, prefix, s3)

# %%

# Check to make sure you are downloading to the package root level
CURRENT_PATH = Path(os.getcwd())
CURRENT_FOLDER = CURRENT_PATH.name

if CURRENT_FOLDER == "connectomic-heritability":
    p = Path("./data/graphs")
elif CURRENT_FOLDER == "data":
    p = Path("./graphs")
else:
    # Assume user is in one of subfolders otherwise
    p = Path("../data/graphs")

p.mkdir(parents=True, exist_ok=True)

for idx, sub in enumerate(subjects):
    prefix = f"hcp1200/{sub}/ses-1/connectomes/"
    list_kwargs = dict(Bucket=bucket, Prefix=prefix, Delimiter="/")
    folders = s3.list_objects_v2(**list_kwargs)["CommonPrefixes"]

    to_download = []

    for folder in folders:
        k = s3.list_objects_v2(Bucket=bucket, Prefix=folder["Prefix"], Delimiter="/")[
            "Contents"
        ]
        if "lost_roi" in k[0]["Key"]:
            continue
        to_download.append(k[0]["Key"])

    print(f"{idx} \t : Downloading {sub}", end="\r")
    for file in to_download:
        parc_folder = file.split("/")[-2]
        parc_path = p / parc_folder
        parc_path.mkdir(parents=True, exist_ok=True)

        filename = file.split("/")[-1]
        output_filename = p / parc_folder / filename

        s3.download_file(Bucket=bucket, Key=file, Filename=str(output_filename))
