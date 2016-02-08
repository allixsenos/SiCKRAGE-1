#!/usr/bin/env python2

# Author: echel0n <sickrage.tv@gmail.com>
# URL: http://www.github.com/sickragetv/sickrage/
#
# This file is part of SickRage.
#
# SickRage is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# SickRage is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with SickRage.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals

import re
import unittest

import sickrage
from core.databases import main_db
from core.tv.show import TVShow
from tests import SiCKRAGETestDBCase


class XEMBasicTests(SiCKRAGETestDBCase):
    def loadShowsFromDB(self):
        """
        Populates the showList with shows from the database
        """

        sqlResults = main_db.MainDB().select("SELECT * FROM tv_shows")

        for sqlShow in sqlResults:
            try:
                curShow = TVShow(int(sqlShow[b"indexer"]), int(sqlShow[b"indexer_id"]))
                curShow.saveToDB()
                curShow.loadFromDB(skipNFO=True)
                sickrage.srCore.SHOWLIST.append(curShow)
            except Exception:
                pass

    def loadFromDB(self):
        """
        Populates the showList with shows from the database
        """

        sqlResults = main_db.MainDB().select("SELECT * FROM tv_shows")

        for sqlShow in sqlResults:
            try:
                curShow = TVShow(int(sqlShow[b"indexer"]), int(sqlShow[b"indexer_id"]))
                curShow.saveToDB()
                curShow.loadFromDB(skipNFO=True)
                sickrage.srCore.SHOWLIST.append(curShow)
            except Exception as e:
                print "There was an error creating the show"

    def test_formating(self):
        name = "Game.of.Thrones.S03.720p.HDTV.x264-CtrlHD"
        release = "Game of Thrones"

        # m = re.match('(?P<ep_ab_num>(?>\d{1,3})(?![ip])).+', name)

        escaped_name = re.sub('\\\\[\\s.-]', '\W+', re.escape(release))
        curRegex = '^' + escaped_name + '\W+(?:(?:S\d[\dE._ -])|(?:\d\d?x)|(?:\d{4}\W\d\d\W\d\d)|(?:(?:part|pt)[\._ -]?(\d|[ivx]))|Season\W+\d+\W+|E\d+\W+|(?:\d{1,3}.+\d{1,}[a-zA-Z]{2}\W+[a-zA-Z]{3,}\W+\d{4}.+))'
        # print(u"Checking if show " + name + " matches " + curRegex)

        match = re.search(curRegex, name, re.I)
        # if match:
        #     print(u"Matched " + curRegex + " to " + name)


if __name__ == "__main__":
    print "=================="
    print "STARTING - XEM SCENE NUMBERING TESTS"
    print "=================="
    print "######################################################################"
    unittest.main()