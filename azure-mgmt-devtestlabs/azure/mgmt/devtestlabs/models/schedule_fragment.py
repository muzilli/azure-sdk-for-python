# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .update_resource import UpdateResource


class ScheduleFragment(UpdateResource):
    """A schedule.

    :param tags: The tags of the resource.
    :type tags: dict[str, str]
    :param status: The status of the schedule (i.e. Enabled, Disabled).
     Possible values include: 'Enabled', 'Disabled'
    :type status: str or ~azure.mgmt.devtestlabs.models.EnableStatus
    :param task_type: The task type of the schedule (e.g. LabVmsShutdownTask,
     LabVmAutoStart).
    :type task_type: str
    :param weekly_recurrence: If the schedule will occur only some days of the
     week, specify the weekly recurrence.
    :type weekly_recurrence:
     ~azure.mgmt.devtestlabs.models.WeekDetailsFragment
    :param daily_recurrence: If the schedule will occur once each day of the
     week, specify the daily recurrence.
    :type daily_recurrence: ~azure.mgmt.devtestlabs.models.DayDetailsFragment
    :param hourly_recurrence: If the schedule will occur multiple times a day,
     specify the hourly recurrence.
    :type hourly_recurrence:
     ~azure.mgmt.devtestlabs.models.HourDetailsFragment
    :param time_zone_id: The time zone ID (e.g. Pacific Standard time).
    :type time_zone_id: str
    :param notification_settings: Notification settings.
    :type notification_settings:
     ~azure.mgmt.devtestlabs.models.NotificationSettingsFragment
    :param target_resource_id: The resource ID to which the schedule belongs
    :type target_resource_id: str
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'task_type': {'key': 'properties.taskType', 'type': 'str'},
        'weekly_recurrence': {'key': 'properties.weeklyRecurrence', 'type': 'WeekDetailsFragment'},
        'daily_recurrence': {'key': 'properties.dailyRecurrence', 'type': 'DayDetailsFragment'},
        'hourly_recurrence': {'key': 'properties.hourlyRecurrence', 'type': 'HourDetailsFragment'},
        'time_zone_id': {'key': 'properties.timeZoneId', 'type': 'str'},
        'notification_settings': {'key': 'properties.notificationSettings', 'type': 'NotificationSettingsFragment'},
        'target_resource_id': {'key': 'properties.targetResourceId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ScheduleFragment, self).__init__(**kwargs)
        self.status = kwargs.get('status', None)
        self.task_type = kwargs.get('task_type', None)
        self.weekly_recurrence = kwargs.get('weekly_recurrence', None)
        self.daily_recurrence = kwargs.get('daily_recurrence', None)
        self.hourly_recurrence = kwargs.get('hourly_recurrence', None)
        self.time_zone_id = kwargs.get('time_zone_id', None)
        self.notification_settings = kwargs.get('notification_settings', None)
        self.target_resource_id = kwargs.get('target_resource_id', None)
