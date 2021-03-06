import numpy as np
from workflow_imaging.pipeline import imaging, scan

populate_settings = {'reserve_jobs': True, 'suppress_errors': True, 'display_progress': True}


def populate():
    # populate "dj.Imported" and "dj.Computed" tables
    scan.ScanInfo.populate(**populate_settings)
    imaging.Processing.populate(**populate_settings)
    imaging.MotionCorrection.populate(**populate_settings)
    imaging.Segmentation.populate(**populate_settings)
    imaging.MaskClassification.populate(**populate_settings)
    imaging.Fluorescence.populate(**populate_settings)
    imaging.Activity.populate(**populate_settings)


if __name__ == '__main__':
    populate()
