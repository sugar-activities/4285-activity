#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2008 One Laptop Per Child
# Copyright 2007 Gerard J. Cerchio <www.circlesoft.com>
# Copyright 2008 Andrés Ambrois <andresambrois@gmail.com>
# Copyright 2010 Marcos Orfila <www.marcosorfila.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import gtk
import pango
import os
import commands

from sugar.activity import activity
from sugar.graphics.toolbarbox import ToolbarBox
from sugar.activity.widgets import ActivityToolbarButton
from sugar.activity.widgets import StopButton

from gettext import gettext as _


class JreActivity(activity.Activity):

    def __init__(self, handle):
        activity.Activity.__init__(self, handle)
        self.max_participants = 1

        self.folder_path = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
        self.jre_folder = os.path.join(self.folder_path, "jre")
        self.ceibaljam_icon_path = os.path.join(self.folder_path, "images/ceibaljam.png")

        self.build_toolbar()
        self.build_canvas()
        self.show_all()

    def build_toolbar(self):

        toolbox = ToolbarBox()

        activity_button = ActivityToolbarButton(self)
        toolbox.toolbar.insert(activity_button, -1)
        activity_button.show()

        separator = gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(True)
        toolbox.toolbar.insert(separator, -1)

        stop_button = StopButton(self)
        stop_button.props.accelerator = _('<Ctrl>Q')
        toolbox.toolbar.insert(stop_button, -1)
        stop_button.show()

        self.set_toolbox(toolbox)

    def build_canvas(self):

        box_canvas = gtk.VBox(False, 0)

        # Title

        box_title = gtk.VBox(False, 0)
        label_title = gtk.Label(_("Java Runtime Environment"))
        label_title.set_justify(gtk.JUSTIFY_CENTER)
        label_title.modify_font(pango.FontDescription("Arial 18"))
        label_copyright1 = gtk.Label(_("Copyright © 2010 Sun Microsystems, Inc., 4150 Network Circle, Santa Clara,"))
        label_copyright2 = gtk.Label(_("California 95054, U.S.A.  All rights reserved."))
        label_copyright1.set_justify(gtk.JUSTIFY_CENTER)
        label_copyright2.set_justify(gtk.JUSTIFY_CENTER)

        box_title.add(gtk.Label(""))
        box_title.add(gtk.Label(""))
        box_title.add(label_title)
        box_title.add(gtk.Label(""))
        box_title.add(gtk.Label(""))
        box_title.add(label_copyright1)
        box_title.add(label_copyright2)
        box_title.add(gtk.Label(""))

        # Version

        box_version = gtk.VBox(False, 0)
        version_information = commands.getoutput(self.jre_folder + "/bin/java -version")
        label_version_info = gtk.Label(version_information)
        label_version_info.set_justify(gtk.JUSTIFY_CENTER)

        box_version.add(gtk.Label(""))
        box_version.add(label_version_info)
        box_version.add(gtk.Label(""))

        # Usage explanation

        box_usage = gtk.VBox(False, 0)
        label_usage1 = gtk.Label(_("To use this JRE in your activity, add the following line to your script:"))
        label_usage2 = gtk.Label('<b>PATH=' + self.jre_folder + '/bin:$PATH</b>')
        label_usage2.set_use_markup(True)
        label_usage1.set_justify(gtk.JUSTIFY_CENTER)
        label_usage2.set_justify(gtk.JUSTIFY_CENTER)
        box_usage.add(gtk.Label(""))
        box_usage.add(label_usage1)
        box_usage.add(label_usage2)
        box_usage.add(gtk.Label(""))

        # Credits

        box_credits = gtk.VBox(False, 0)
        box_credits.add(gtk.Label(""))
        box_credits.add(gtk.Label(_('Sugarized by %(THE_AUTHOR)s') % { 'THE_AUTHOR': 'Marcos Orfila' }))
        label_my_website = gtk.Label('<b>http://www.marcosorfila.com</b>')
        label_my_website.set_use_markup(True)
        box_credits.add(label_my_website)
        box_credits.add(gtk.Label(""))

        # Footer box (Activities on CeibalJAM! website)

        box_footer = gtk.VBox(False, 0)
        box_footer.add(gtk.Label(""))
        box_footer.add(gtk.Label(_('Find more activities on %(CEIBALJAM)s website:') % { 'CEIBALJAM': 'CeibalJAM!'}))
        label_ceibaljam_website = gtk.Label('<b>http://activities.ceibaljam.org</b>')
        label_ceibaljam_website.set_use_markup(True)
        box_footer.add(label_ceibaljam_website)
        box_footer.add(gtk.Label(""))

        # CeibalJAM! image

        box_ceibaljam_image = gtk.VBox(False, 0)
        image_ceibaljam = gtk.Image()
        image_ceibaljam.set_from_file(self.ceibaljam_icon_path)
        box_ceibaljam_image.pack_end(image_ceibaljam, False, False, 0)

        # Get all the boxes together

        box_canvas.pack_start(box_title, False, False, 0)
        box_canvas.pack_start(box_version, False, False, 0)
        box_canvas.pack_start(box_usage, False, False, 0)
        box_canvas.pack_end(box_footer, False, False, 0)
        box_canvas.pack_end(box_ceibaljam_image, False, False, 0)
        box_canvas.pack_end(box_credits, False, False, 0)

        self.set_canvas(box_canvas)

