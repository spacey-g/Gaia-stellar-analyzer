from astroquery.gaia import Gaia
import pandas as pd

def query_star_by_gaia_id(gaia_id):
    """
    Query Gaia DR3 for a single star using its Gaia source_id.
    Returns a pandas DataFrame.
    """
    query = f"""
        SELECT *
        FROM gaiadr3.gaia_source
        WHERE source_id = {gaia_id}
        """
    job = Gaia.launch_job_async(query)
    result = job.get_results()

    # convert to pandas DataFrame
    df = result.to_pandas()
    return df

