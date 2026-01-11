"""
Modules and imports
"""

import Imports.grade_avg_service as grade_service

grades = {
    "h1" : 85,
    "h2" : 100,
    "h3" : 81
}

# Imports.grade_avg_service(grades)
grade_service.calc_homework(grades)