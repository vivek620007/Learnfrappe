# Copyright (c) 2024, Vivek Kumar and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):    
    columns = [
        {"fieldname": "make", "label": "Make", "fieldtype": "Data", "width": 150},
        {"fieldname": "revenue", "label": "Revenue", "fieldtype": "Currency", "width": 100},
    ]

    rides = frappe.get_all("Ride", fields=["vehicle", "total_amount", "vehicle.make"])

    revenue_by_make = {}

    for ride in rides:
        if ride.make in revenue_by_make:
            # pass
            print("kkk"*10, revenue_by_make[ride.make], ride.make)
            # revenue_by_make[ride.make] += ride.total_amount   
        else:
            revenue_by_make[ride.make] = ride.total_amount
            print("run 1", revenue_by_make)

    data = [{"make": make, "revenue": revenue} for make, revenue in revenue_by_make.items()]

    return columns, data



    

# Example code for a different report structure
# Uncomment if needed for alternative implementations
#
# def get_columns() -> list[dict]:
#     """Return columns for the report."""
#     return [
#         {
#             "label": _("Column 1"),
#             "fieldname": "column_1",
#             "fieldtype": "Data",
#         },
#         {
#             "label": _("Column 2"),
#             "fieldname": "column_2",
#             "fieldtype": "Int",
#         },
#     ]
#
# def get_data() -> list[list]:
#     """Return data for the report."""
#     return [
#         ["Row 1", 1],
#         ["Row 2", 2],
#     ]