#!/usr/bin/env python3
#
#  MAKINAROCKS CONFIDENTIAL
#  ________________________
#
#  [2017] - [2021] MakinaRocks Co., Ltd.
#  All Rights Reserved.
#
#  NOTICE:  All information contained herein is, and remains
#  the property of MakinaRocks Co., Ltd. and its suppliers, if any.
#  The intellectual and technical concepts contained herein are
#  proprietary to MakinaRocks Co., Ltd. and its suppliers and may be
#  covered by U.S. and Foreign Patents, patents in process, and
#  are protected by trade secret or copyright law. Dissemination
#  of this information or reproduction of this material is
#  strictly forbidden unless prior written permission is obtained
#  from MakinaRocks Co., Ltd.

"""This module is test git action."""

i = 0  # test variable


class TestCls:  # pylint: disable=too-few-public-methods
    """Test class for git action."""

    def __init__(self: "TestCls"):
        """Initialize."""
        self.val1 = 0

    def test(self: "TestCls", val1: int) -> None:
        """Test method for git action."""
        print("hello world")
        self.val1 = val1
        print(self.val1 + 3)


b = TestCls()
b.test(i)
