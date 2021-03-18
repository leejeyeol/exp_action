# -*- coding: utf-8 -*-
#
#  MAKINAROCKS CONFIDENTIAL
#  ________________________
#
#  [2017] - [2020] MakinaRocks Co., Ltd.
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
#
"""Dummy module to check unittest runs.
Author:
    Name: Jinwoo Park
    Email: jinwoo.park@makinarocks.ai
"""

from dummy import identity


class TestIntegerInput:
    """Test cases for integer inputs."""

    def test_identity_negative(self) -> None:
        """Test identity function works well."""
        assert identity(-1) == -1

    def test_identity_zero(self) -> None:
        """Test identity function works well."""
        assert identity(0) == 0

    def test_identity_positive(self) -> None:
        """Test identity function works well."""
        assert identity(1) == 1


class TestFloatInput:
    """Test cases for float inputs."""

    def test_identity_negative(self) -> None:
        """Test identity function works well."""
        assert identity(-1.0) == -1.0

    def test_identity_zero(self) -> None:
        """Test identity function works well."""
        assert identity(0.0) == 0.0

    def test_identity_positive(self) -> None:
        """Test identity function works well."""
        assert identity(1.0) == 1.0
