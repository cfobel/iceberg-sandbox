# %%
import boto3.session
from pyiceberg import __version__
import pyiceberg.exceptions
from timeit import default_timer as timer


__version__
# %%
from pyiceberg.catalog.glue import GlueCatalog

import boto3

profile_name = "AdministratorAccess-786727767884"
region_name = "us-east-1"

session = boto3.session.Session(profile_name=profile_name, region_name=region_name)
credentials = session.get_credentials()

catalog = GlueCatalog(
    "default",
    **{
        "profile_name": profile_name,
        "region_name": session.region_name,
        "s3.access-key-id": credentials.access_key,
        "s3.region": session.region_name,
        "s3.secret-access-key": credentials.secret_key,
        "s3.session-token": credentials.token,
    },
)
# %%
import pandas as pd
import pyarrow as pa


def create_sample_dataframe() -> pd.DataFrame:
    # Create sample data using Pandas
    data = {
        "id": [1, 2, 3, 4, 5],
        "name": ["Alice", "Bob", "Cathy", "David", "Eva"],
        "age": [25, 30, 22, 35, 28],
        "salary": [50000.0, 60000.0, 55000.0, 70000.0, 65000.0],
        "is_active": [True, False, True, True, False],
        "join_date": pd.to_datetime(
            [
                "2023-01-01 00:00:00",
                "2023-02-15 00:00:00",
                "2023-03-10 00:00:00",
                "2023-04-25 00:00:00",
                "2023-05-30 00:00:00",
            ]
        ).astype(
            "datetime64[ms]"
        ),  # Downcast to milliseconds
    }

    # Convert the dictionary to a Pandas DataFrame
    df = pd.DataFrame(data)

    return df


# %%
pa_table = pa.Table.from_pandas(create_sample_dataframe())
database_name = "iceberg_sandbox"
table_name = "foo"
try:
    table = catalog.create_table(
        (database_name, table_name),
        schema=pa_table.schema,
        location="s3://net-fobel-christian-iceberg-sandbox/iceberg_sandbox_catalog/table=foo/",
    )
except pyiceberg.exceptions.TableAlreadyExistsError as e:
    table = catalog.load_table((database_name, table_name))

# %%
start = timer()
table.append(pa_table)
end = timer()
print(f"Append took {end - start} seconds")
catalog.load_namespace_properties("iceberg_sandbox")

# %%
