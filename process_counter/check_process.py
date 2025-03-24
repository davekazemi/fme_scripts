import fme
from fme import BaseTransformer
import fmeobjects
import os
import time
import psutil

# Helper methods to log to FME's native log system:
def fme_inform(msg: str):
    """Log an info-level message to the FME log."""
    fmeobjects.FMELogFile().logMessageString(msg, fmeobjects.FME_INFORM)

def fme_warn(msg: str):
    """Log a warning-level message to the FME log."""
    fmeobjects.FMELogFile().logMessageString(msg, fmeobjects.FME_WARN)

def get_process_count(process_name: str = 'fme.exe') -> int:
    """Return the number of matching processes currently running."""
    count = 0
    for proc in psutil.process_iter():
        try:
            if proc.name().lower() == process_name.lower():
                count += 1
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return count

def waiting_for_process(
    timeout: int = 60,
    checkinterval: int = 5,
    process_name: str = 'fme.exe',
    noExit: int = 1,
    forceKill: bool = False,
    wait_to_reach: bool = True
) -> bool:
    """Wait until no matching processes remain, or until the timeout expires."""
    start_time = time.time()

    while True:
        remaining_time = timeout - (time.time() - start_time)
        if remaining_time < 0 and wait_to_reach:
            fme_warn(f'Timeout reached. Exiting after {timeout} seconds.')
            if forceKill:
                fme_warn(f'Force killing all {process_name} processes.')
                os.system(f'taskkill /f /im {process_name}')
            return False

        process_count = get_process_count(process_name)
        if process_count == noExit:
            # Windows-specific notification
            os.system('msg * "Process completed"')
            os.system('rundll32 user32.dll,MessageBeep')
            fme_inform(f'All {process_name} processes have completed.')
            return True
        else:
            fme_inform(f'{process_count} {process_name} process(es) running. ')
            if not wait_to_reach:
                fme_inform(f'Waiting... {int(remaining_time)}s remaining.')
        time.sleep(checkinterval)

class FeatureProcessor(BaseTransformer):
    """
    This class inherits from 'fme.BaseTransformer' and is intended to be used
    with a PythonCaller transformer in FME.
    """

    def __init__(self):
        """Base constructor for class members."""
        pass

    def has_support_for(self, support_type: int):
        """Indicates that we support the feature-table shim."""
        return support_type == fmeobjects.FME_SUPPORT_FEATURE_TABLE_SHIM

    def input(self, feature: fmeobjects.FMEFeature):
        """
        Called for each feature which enters the PythonCaller.
        We'll wait for the target processes to finish before outputting.
        """
        
        waiting_for_process(
            timeout=int(feature.getAttribute('_timeout')),
            checkinterval=int(feature.getAttribute('_CheckingInterval')),
            process_name=feature.getAttribute('_process_name'),
            noExit=int(feature.getAttribute('_NoExit'))
        )

        # Pass the feature along unchanged
        self.pyoutput(feature, output_tag="PYOUTPUT")

    def close(self):
        """Called once all features have been processed."""
        pass

    def process_group(self):
        """Called by FME for each group if group processing mode is enabled."""
        pass

    def reject_feature(self, feature: fmeobjects.FMEFeature, code: str, message: str):
        """Send a feature to the <Rejected> port with a rejection code/message."""
        feature.setAttribute("fme_rejection_code", code)
        feature.setAttribute("fme_rejection_message", message)
        self.pyoutput(feature, output_tag="<Rejected>")
