# config.py

# Dictionary to hold all your DSNs. This remains the same.
DSN_CONFIG = {
    "v12live": "v12Live",
    "edw": "EDMEWAREAD"
}

# Dictionary mapping our internal DSN names to the tables they should access.
# Updated based on the provided list.
# Note: The schema '' is assumed from your previous request.
# You may need to change or remove it depending on your database setup.
TABLE_MAPPING = {
    "v12live": [
        'MVXCDTA_CEAEMP',
        'MVXCDTA_MITBAL',
        'MVXCDTA_MITMAS',
        'MVXCDTA_MITSTA',
        'MVXCDTA_MPDHED',
        'MVXCDTA_MPDMAT',
        'MVXCDTA_MPDOPE',
        'MVXCDTA_MPDWCT',
        'PFXCDTA_SN5REQ',
        'PFXCDTA_SN5RHD',
        'PFXCDTA_SN5RLN',
        'PFXCDTA_SN5TYP'
    ],
    "edw": [
        'ADMEDP_EDM_DOCS',
        'ADMEDP_EDM_FILE_EXTENSION',
        'ADMEDP_EDM_FILES'
    ]
}