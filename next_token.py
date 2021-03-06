#!/usr/bin/env python

# Copyright 2011-2014, University of Amsterdam. This program is free software:
# you can redistribute it and/or modify it under the terms of the GNU Lesser 
# General Public License as published by the Free Software Foundation, either 
# version 3 of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or 
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License 
# for more details.
# 
# You should have received a copy of the GNU Lesser General Public License 
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from datetime import datetime, timedelta
import sys, re

token = sys.argv[1]
match = re.match("DDD!(.*T.*)\.(\d+)Z!!didl!0", token)
time = datetime.strptime(match.group(1), "%Y-%m-%dT%H:%M:%S") + timedelta(minutes=1)

if time < datetime.now():
    print "DDD!" + datetime.strftime(time, "%Y-%m-%dT%H:%M:%S") + "." + match.group(2) + "Z!!didl!0"

#DDD!2012-02-14T13:51:05.326Z!!didl!0
#2012-02-14T01:08:01.951Z

