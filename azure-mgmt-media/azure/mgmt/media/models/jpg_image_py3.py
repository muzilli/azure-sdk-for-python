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

from .image_py3 import Image


class JpgImage(Image):
    """Describes the properties for producing a series of JPEG images from the
    input video.

    All required parameters must be populated in order to send to Azure.

    :param label: An optional label for the codec. The label can be used to
     control muxing behavior.
    :type label: str
    :param odatatype: Required. Constant filled by server.
    :type odatatype: str
    :param key_frame_interval: The distance between two key frames, thereby
     defining a group of pictures (GOP). The value should be a non-zero integer
     in the range [1, 30] seconds, specified in ISO 8601 format. The default is
     2 seconds (PT2S).
    :type key_frame_interval: timedelta
    :param stretch_mode: The resizing mode - how the input video will be
     resized to fit the desired output resolution(s). Default is AutoSize.
     Possible values include: 'None', 'AutoSize', 'AutoFit'
    :type stretch_mode: str or ~azure.mgmt.media.models.StretchMode
    :param start: The position in the input video from where to start
     generating thumbnails. The value can be in absolute timestamp (ISO 8601,
     e.g: PT05S), or a frame count (For example, 10 for the 10th frame), or a
     relative value (For example, 1%). Also supports a macro {Best}, which
     tells the encoder to select the best thumbnail from the first few seconds
     of the video.
    :type start: str
    :param step: The intervals at which thumbnails are generated. The value
     can be in absolute timestamp (ISO 8601, e.g: PT05S for one image every 5
     seconds), or a frame count (For example, 30 for every 30 frames), or a
     relative value (For example, 1%).
    :type step: str
    :param range: The position in the input video at which to stop generating
     thumbnails. The value can be in absolute timestamp (ISO 8601, e.g: PT5M30S
     to stop at 5 minutes and 30 seconds), or a frame count (For example, 300
     to stop at the 300th frame), or a relative value (For example, 100%).
    :type range: str
    :param layers: A collection of output JPEG image layers to be produced by
     the encoder.
    :type layers: list[~azure.mgmt.media.models.JpgLayer]
    """

    _validation = {
        'odatatype': {'required': True},
    }

    _attribute_map = {
        'label': {'key': 'label', 'type': 'str'},
        'odatatype': {'key': '@odata\\.type', 'type': 'str'},
        'key_frame_interval': {'key': 'keyFrameInterval', 'type': 'duration'},
        'stretch_mode': {'key': 'stretchMode', 'type': 'str'},
        'start': {'key': 'start', 'type': 'str'},
        'step': {'key': 'step', 'type': 'str'},
        'range': {'key': 'range', 'type': 'str'},
        'layers': {'key': 'layers', 'type': '[JpgLayer]'},
    }

    def __init__(self, *, label: str=None, key_frame_interval=None, stretch_mode=None, start: str=None, step: str=None, range: str=None, layers=None, **kwargs) -> None:
        super(JpgImage, self).__init__(label=label, key_frame_interval=key_frame_interval, stretch_mode=stretch_mode, start=start, step=step, range=range, **kwargs)
        self.layers = layers
        self.odatatype = '#Microsoft.Media.JpgImage'
