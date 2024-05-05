import pytest
import copy

from typing import Optional

from plum.jobs.utils.execution.recorder import (
    ExecutionRecorder,
    PrematureEndTimestampError,
    StartTimestampResetError,
    EndTimestampResetError
)

@pytest.fixture(scope = "module")
def create_execution_recorder():
    return ExecutionRecorder(job_id = "test_suite_00000")

@pytest.mark.unit
def test_set_start_timestamp(
    create_execution_recorder: ExecutionRecorder
):
    recorder: ExecutionRecorder = copy.deepcopy(create_execution_recorder)

    reset_err: Optional[StartTimestampResetError] = recorder.set_start_timestamp()
    assert reset_err == None, 'expected None returned due to first time setting timestamp but got exception'
    assert recorder.start_timestamp != None, 'expected datetime to be set on "start_timestamp" but was found to be None'

    reset_err: Optional[StartTimestampResetError] = recorder.set_start_timestamp()
    assert isinstance(reset_err, StartTimestampResetError), 'expected "StartTimestampResetError" due to second run of class method but got None'

@pytest.mark.unit
def test_set_end_timestamp(
    create_execution_recorder: ExecutionRecorder
):
    recorder: ExecutionRecorder = copy.deepcopy(create_execution_recorder)

    err: PrematureEndTimestampError = recorder.set_end_timestamp()
    assert isinstance(err, PrematureEndTimestampError), f'expected PrematureEndTimestampError, to be returned due to missing "start_timestamp"'

    reset_err: Optional[StartTimestampResetError] = recorder.set_start_timestamp()
    assert reset_err == None, 'expected None returned due to first time setting timestamp but got exception'
    
    err: Optional[PrematureEndTimestampError] = recorder.set_end_timestamp()
    assert err == None, 'expected no PrematureEndTimestampError to be returned, due to "start_timestamp" being provided'

    reset_err: Optional[StartTimestampResetError] = recorder.set_end_timestamp()
    assert isinstance(reset_err, EndTimestampResetError), 'expected "EndTimestampResetError" due to second run of class method but got None'