from astroquery.gaia import Gaia
import pandas as pd

# ==============================
# 1. Query a single star by ID
# ==============================
def query_star_by_gaia_id(gaia_id):
    query = f"""
        SELECT *
        FROM gaiadr3.gaia_source
        WHERE source_id = {gaia_id}
    """
    job = Gaia.launch_job_async(query)
    result = job.get_results()
    return result.to_pandas()


# ======================================
# 2. Query multiple stars by ID list
# ======================================
def query_multiple_gaia_ids(id_list):
    id_list_str = ",".join(map(str, id_list))

    query = f"""
        SELECT *
        FROM gaiadr3.gaia_source
        WHERE source_id IN ({id_list_str})
    """
    job = Gaia.launch_job_async(query)
    result = job.get_results()
    return result.to_pandas()


# ======================================
# 3. Query a region (RA, DEC, radius)
# ======================================
def query_region(ra, dec, radius_arcmin):
    query = f"""
        SELECT *
        FROM gaiadr3.gaia_source
        WHERE CONTAINS(
            POINT('ICRS', ra, dec),
            CIRCLE('ICRS', {ra}, {dec}, {radius_arcmin/60})
        ) = 1
    """

    job = Gaia.launch_job_async(query)
    result = job.get_results()
    return result.to_pandas()


# ======================================
# 4. Query by magnitude cutoff
# ======================================
def query_by_magnitude(max_g_mag=15):
    query = f"""
        SELECT source_id, ra, dec, phot_g_mean_mag, bp_rp
        FROM gaiadr3.gaia_source
        WHERE phot_g_mean_mag < {max_g_mag}
        ORDER BY phot_g_mean_mag ASC
        LIMIT 5000
    """
    job = Gaia.launch_job_async(query)
    result = job.get_results()
    return result.to_pandas()
