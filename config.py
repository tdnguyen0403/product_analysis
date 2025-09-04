# config.py

# A simple dictionary to hold your Data Source Names.
DSN_CONFIG = {
    "v12live": "v12Live",
    "edw": "EDMEWAREAD"
}

# Define the facility to analyze - MF1
FACILITY_CODE = 'MF1'

## Define the facility to analyze - MF1
# FACILITY_CODE = 'VN1'

## Define the list of planning areas for the analysis - US Product
# PLANNING_AREA = [
#     'MP-5310', 'MP-5320', 'MP-5330', 'MP-5340', 'MP-5350', 'MP-5360'
# ]

# Define the list of planning areas for the analysis - PA level 2/5
PLANNING_AREA = [
    'MP-4117','MP-4210', 'MP-4220', 'MP-4230', 'MP-4240', 'MP-4250', 'MP-4260', 'MP-4270', 'MP-4310', 'MP-4320', 'MP-4330', 'MP-4540'
]

# # Define the list of planning areas for the analysis - Systems
# PLANNING_AREA = [
#     'MP-5710'
# ]
# # Define the list of planning areas for the analysis - Whole Vietnam
# PLANNING_AREA = [
#     'VP-5100','GL5_ATL','VP-5120', 'VP-5140', 'VP-5160', 'VP-5170', 'VP-5150', 'VP-5157', 'VP-5180', 'VP-5185',
#     'VP-5192', 'VP-5400', 'ASIG10_ATL', 'ASIG10_ATO', 'VP-5300', 'VARIKO_ATL', 'VP-5220', 'VP-5221', 'VP-5240',
#     'VP-5241', 'EMS1B__ATL', 'VP-5210', 'VP-5211', 'VP-5260', 'VP-5261', 'VP-5900', 'VP-5902', 'VP-5903', 'VP-5904', 'VP-5908',
#     'VP5920', 'VP6100'
# ]

RND_GROUP = {
    'ProductGroup': ['FA10', 'FA20', 'FA30', 'FA40', 'FA50', 'FA70', 'FA80', 'FA90', 'FB00', 'FC00', 'FC09', 'FC10', 'FC20', 'FC90', 'FD00', 'FD10', 'FD20', 'FE00', 'FF00', 'FH10', 'FH20', 'FH30', 'FH40', 'FJ00', 'FK00', 'FK10', 'FL00', 'FL05', 'FN00', 'FN10', 'FO00', 'FP00', 'FP90', 'PA10', 'PA11', 'PA30', 'PA31', 'PA41', 'PA60', 'PA80', 'PA91', 'PA95', 'PA96', 'PA99', 'PB70', 'PC60', 'PD52', 'PD61', 'PD75', 'PG71', 'PH60', 'PH61', 'PH62', 'PH71', 'PJ60', 'PJ62', 'PL70', 'PL71', 'PL72', 'PL73', 'PP70', 'PP71', 'PP72', 'PP73', 'PP75', 'PP76', 'PP77', 'PP78', 'PP79', 'PW10', 'FJ05'],
    'Product': ['Induktiv DC', 'Induktiv AC', 'Induktiv AC/DC', 'Induktiv Namur', 'Induktiv Rest', 'Induktiv Microswitch-Sensorik', 'Induktive Positionssensoren', 'Induktiv Wireless Systems WIS', 'Kapazitiv', 'FA-Optp Generally', 'FA-Opto Instruments', 'FA-Opto Entrance', 'FA-Opto Safety', 'FA-Opto Accessory', 'Ultraschall', 'USI-Safety', 'Radar', 'Magnet', 'Bus-Systeme', 'Ident induktiv', 'Ident Mikrowelle', 'Ident Opto', 'Ident Datamatrix', 'AS-Interface', 'Drehgeber inkremental', 'Drehgeber absolut', 'Zubehör', 'Kabel mit Stecker /Connectivity', 'Weg-Codier-System WCS', 'PCV/PGV', 'Neigungssensoren', 'Ind. Vision Components', 'Smart-Bridge', 'K-System Analog', 'H-System Analog', 'H-System Digital', 'K-System Digital', 'H-System Termination Boards', 'K-System Others', 'Signal Conditioners', 'HART Multiplexer', 'nonIS Termination Boards', 'Lightning Protection', 'Interface Legacy Products', 'E-Cards', 'WE-System', 'EX Terminal (MFT)', 'microZ Range', 'Zener Barriers', 'Power Supply', 'RPI', 'RIO Legacy Products (HiD3000)', 'LB modules', 'Serie 890, Charms, Yokogawa ISIS', 'IS RPI / FlexEx', 'FB modules', 'Field Connex Power Supplies', 'Field Connex Field distributors', 'Field Connex I/O', 'Field Connex Accessories', 'HMI Monitors', 'HMI PC/TC', 'HMI Operator Panels (Termex)', 'HMI Accessories', 'Operator Workstations & Panel PCs', 'Box Thin Clients & Other platforms', 'Software & Service', 'Peripherals & Universal Accessories', 'HMI Solutions & Customization', 'Wireless', 'IO-Link Master']
}

FILE_USER_DATA = {
    'fileuser': [152, 270, 964, 1337, 2539, 6091],
    'Name': [
        'Klauer, Sonja', 
        'Szekely, Beatrice', 
        'Kusche, Britta', 
        'Gosenheimer, Dieter', 
        'Reinig-Seidensticker, Carmen', 
        'Darm, Wenmarie'
    ]
}