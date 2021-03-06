from hestia.unknown import UNKNOWN

from lifecycles.statuses import BaseStatuses, StatusOptions


class OperationStatuses(BaseStatuses):
    CREATED = StatusOptions.CREATED
    RETRYING = StatusOptions.RETRYING
    RESUMING = StatusOptions.RESUMING
    BUILDING = StatusOptions.BUILDING
    STARTING = StatusOptions.STARTING
    SCHEDULED = StatusOptions.SCHEDULED
    RUNNING = StatusOptions.RUNNING
    WARNING = StatusOptions.WARNING
    UNSCHEDULABLE = StatusOptions.UNSCHEDULABLE
    DONE = StatusOptions.DONE
    FAILED = StatusOptions.FAILED
    UPSTREAM_FAILED = StatusOptions.UPSTREAM_FAILED
    STOPPING = StatusOptions.STOPPING
    STOPPED = StatusOptions.STOPPED
    SKIPPED = StatusOptions.SKIPPED
    SUCCEEDED = StatusOptions.SUCCEEDED
    UNKNOWN = UNKNOWN

    HEARTBEAT_STATUS = {RUNNING, }
    WARNING_STATUS = {UNSCHEDULABLE, WARNING, }
    PENDING_STATUS = {CREATED, RESUMING, }
    STARTING_STATUS = {RETRYING, STARTING, BUILDING, }
    RUNNING_STATUS = {SCHEDULED, BUILDING, STARTING, RUNNING, STOPPING, }
    DONE_STATUS = {FAILED, UPSTREAM_FAILED, STOPPED, SKIPPED, SUCCEEDED, DONE, }
    FAILED_STATUS = {FAILED, UPSTREAM_FAILED, }
